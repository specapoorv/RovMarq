from PySide6.QtCore import QObject, Signal
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32, Int8, String
from nav_msgs.msg import Odometry
from rclpy.qos import QoSProfile, ReliabilityPolicy

""" monkey patching numpy here in newer versions np.float is deprecated """
import numpy as np
if not hasattr(np, 'float'):
    np.float = float

from tf_transformations import euler_from_quaternion
from frontend.Qwindow import MainWindow
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Float32MultiArray
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class CSVHandler(FileSystemEventHandler):
    def __init__(self, signal, csv_path):
        super().__init__()
        self.signal = signal
        self.csv_path = csv_path
        self.last_emit = 0

    def on_modified(self, event):
        if event.src_path == self.csv_path:
            now = time.time()
            if now - self.last_emit > 0.3:  # debounce
                self.last_emit = now
                self.signal.emit(self.csv_path)


class ROSQtBridge(Node, QObject):
    kill_signal = Signal(bool)
    colour_signal = Signal(str)
    '''
    bridge just pushes the signals from ros to Qt
    no processing, no blocking
    '''

    gps_updated = Signal(float, float)
    yaw_updated = Signal(float)
    odom_updated = Signal(float, float, float)
    battery_updated = Signal(float)
    latency_updated = Signal(float)
    steering_angles = Signal(float, float, float, float)
    config_updated = Signal(str)
    mode_updated = Signal(int)
    twist_updated = Signal(float, float)
    encoder_angles_updated = Signal(float, float, float, float)

    csv_changed = Signal(str)

    def __init__(self):
        Node.__init__(self, "ros_qt_bridge")
        QObject.__init__(self)

        self.best_effort = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.BEST_EFFORT
        )

        self.create_subscription(NavSatFix, "/gps_fix", self.gps_callback, 10)
        self.create_subscription(Float32, "/global_north", self.yaw_callback, 10)
        self.create_subscription(Odometry, "/rtabmap/odom", self.odom_callback, self.best_effort)
        self.create_subscription(Float32, "/battery_topic", self.battery_callback, 10)
        self.create_subscription(Float32MultiArray, "/enc_auto", self.steering_callback, 10)
        self.create_subscription(Int8, "/mode", self.mode_callback, 10)
        self.create_subscription(String, "/config", self.config_callback, 10)
        self.create_subscription(Float32MultiArray, "/vel", self.vel_callback, 10)

        self.motor_publisher = self.create_publisher(
            Int32MultiArray,
            "/motor_pwm",
            10
        )

        self.csv_observer = None

    # ===== CSV WATCHER START =====
    def start_csv_watcher(self, csv_path):
        handler = CSVHandler(self.csv_changed, csv_path)
        self.csv_observer = Observer()
        self.csv_observer.schedule(
            handler,
            path=csv_path.rsplit("/", 1)[0],
            recursive=False
        )
        self.csv_observer.start()

    # ===== ROS CALLBACKS =====
    def gps_callback(self, msg: NavSatFix):
        self.get_logger().info(f"{msg.latitude}, {msg.longitude}")
        self.gps_updated.emit(msg.latitude, msg.longitude)

    def yaw_callback(self, msg):
        yaw = msg.data
        self.yaw_updated.emit(yaw)

    def vel_callback(self, twist: Float32MultiArray):
        vel = twist.data[0]
        omega = twist.data[1]
        self.twist_updated.emit(vel, omega)

    def odom_callback(self, msg: Odometry):
        q = [
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w
        ]
        _, _, yaw = euler_from_quaternion(q)
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        self.odom_updated.emit(x, y, yaw)

    def battery_callback(self, msg):
        self.battery_updated.emit(msg.data)

    def mode_callback(self, mode: Int8):
        self.mode_updated.emit(mode.data)

    def config_callback(self, config: String):
        self.config_updated.emit(config.data)

    def kill_handler(self, killed):
        if killed:
            print("handling kill switch, ded")
            pwm_msg = Int32MultiArray()
            pwm_msg.data = [0, 0, 0, 0, 0, 0, 0, 0]
            self.motor_publisher.publish(pwm_msg)

    def colour_override_handler(self, colour_name):
        cmd = ["ros2", "param", "set", "/yolo_publisher", "colour_override", colour_name]
        try:
            subprocess.Popen(cmd)
            print(f"ROS2 param set called: {cmd}")
        except Exception as e:
            print("Failed to set ROS2 param:", e)


    def steering_callback(self, msg):
        data = msg.data
        fl = data[0]
        fr = data[1]
        bl = data[2]
        br = data[3]

        self.encoder_angles_updated.emit(fl, fr, bl, br)
        self.steering_angles.emit(fl, fr, bl, br)
