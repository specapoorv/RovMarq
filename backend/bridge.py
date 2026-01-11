from PySide6.QtCore import QObject, Signal
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PoseArray
from std_msgs.msg import Float32, Int8, String, Float64
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
import csv
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from backend.csv_manager import CSVLogger
from backend.term import SSHSession

ssh = SSHSession(
    host="10.42.0.51",
    user="nvidia",
    password="nvidia",
)

time.sleep(3)

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
                print("emitting signals")
                self.signal.emit(self.csv_path)


class ROSQtBridge(Node, QObject):
    kill_signal = Signal(bool)
    colour_signal = Signal(str)
    autolog_signal = Signal(bool)
    brightness_signal = Signal(int, int)  # cam_id, value
    contrast_signal   = Signal(int, int)
    zoom_signal       = Signal(int, int)
    send_signal = Signal(bool)
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
    frequency_updated = Signal(float)
    noise_updated = Signal(float)

    csv_changed = Signal(str)

    def __init__(self):
        Node.__init__(self, "ros_qt_bridge")
        QObject.__init__(self)


        self.csv_observer = None
        self.csv_file_path = "waypoints.csv"

        self.latest_gps = None # (lat, lon)
        self.vel = None  
        self.waypoint_id = 0
        self.last_waypoint_id = None
        self.csv_logger = CSVLogger(self.csv_file_path)
        self.last_auto_wp_id = None
        self.gps_timestamp = None
        self.vel_timestamp = None


        self.best_effort = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.BEST_EFFORT
        )

        self.reliable = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE
        )

        self.create_subscription(NavSatFix, "/mobile_sensor/gps", self.gps_callback, 10)
        self.create_subscription(Float64, "/global_north", self.yaw_callback, 10)
        self.create_subscription(Odometry, "/zed/zed_node/odom", self.odom_callback, self.best_effort)
        self.create_subscription(Float32, "/battery_topic", self.battery_callback, 10)
        self.create_subscription(Float32MultiArray, "/enc_auto", self.steering_callback, self.reliable)
        self.create_subscription(Int8, "/mode", self.mode_callback, self.reliable)
        self.create_subscription(String, "/config", self.config_callback, self.reliable)
        self.create_subscription(Float32MultiArray, "/vel", self.vel_callback, self.reliable)
        self.create_subscription(Float32MultiArray, "/mikrotik_info", self.mikrotik_info_callback, 10)
        self.motor_publisher = self.create_publisher(Int32MultiArray, "/motor_pwm", 10)

        self.autolog_timer = self.create_timer(5.0, self.autolog_waypoint)
        self.autolog_flag = False

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
        self.latest_gps = (msg.latitude, msg.longitude)
        self.gps_timestamp = time.time()
        self.gps_updated.emit(msg.latitude, msg.longitude)

    def yaw_callback(self, msg):
        yaw = msg.data
        yaw = yaw - 180
        print("updating yaw")
        self.yaw_updated.emit(yaw)

    def vel_callback(self, twist: Float32MultiArray):
        vel = twist.data[0]
        omega = twist.data[1]
        self.vel = vel
        self.vel_timestamp = time.time()
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

    def mikrotik_info_callback(self, info: Float32MultiArray):
        self.frequency_updated.emit(info.data[0])
        self.noise_updated.emit(info.data[1])

    def kill_handler(self, killed):
        if killed:
            print("handling kill switch, ded")
            pwm_msg = Int32MultiArray()
            pwm_msg.data = [0, 0, 0, 0, 0, 0, 0, 0]
            self.motor_publisher.publish(pwm_msg)

    
    def send_handler(self, sent: bool):
        if sent:
            pass
        # Add the functionality here i guess or change

    def colour_override_handler(self, colour_name):
        # subprocess.run(['sshpass -p "anveshak" ssh orin@10.42.0.253', "echo 'hello'", f"ros2 param set /yolo_publisher colour_override {colour_name}", "exit"], shell=True)
        print(f"[BACKEND] setting parameter {colour_name}")
        # ssh.run('echo hello')
        # ssh.run('ros2 topic list')
        # time.sleep(2)
        subprocess.run(f'ros2 param set /yolo_publisher colour_override {colour_name}')
        # subprocess.run("exit", shell=True)
    
    def cam_setting_handler(self, cam_index, type, value):
        device_id = cam_index - 1
        device = f"/dev/video{device_id}"

        if type == "brightness":
            ctrl = "brightness"
        elif type == "contrast":
            ctrl = "contrast"
        elif type == "zoom":
            ctrl = "zoom_absolute"
        else:
            print(f"Unknown camera setting type: {type}")
            return

        cmd = f"v4l2-ctl -d {device} -c {ctrl}={value}"
        print(f"[CAM {cam_index}] {cmd}")

        try:
            ssh.run(cmd)
        except Exception as e:
            print(f"Failed to run camera command: {e}")

        

    def steering_callback(self, msg):
        data = msg.data
        fl = data[0]
        fr = data[1]
        bl = -data[2]
        br = -data[3]

        self.encoder_angles_updated.emit(fl, fr, bl, br)
        self.steering_angles.emit(fl, fr, bl, br)

    def autolog_handler(self, checked):
        self.autolog_flag = checked

    def autolog_waypoint(self):
        if not self.autolog_flag:
            print("STOPPED LOGGING, too much cock you are showing ah")
            return
        else:
            print("autologgin on")

        
        # if self.gps_timestamp or self.vel_timestamp is None:
        #     return
        
        # if (time.time() - self.gps_timestamp) or (time.time() - self.vel_timestamp) > 1.0:
        #     self.latest_gps = None
        #     self.vel = None

        # if self.latest_gps or self.vel is None:
        #     return
        if self.latest_gps is None:
            return
        
        lat, lon = self.latest_gps

        new_id = self.csv_logger.add_marker(
            lat=lat,
            lon=lon,
            label="waypoint"   # visual / semantic label only
        )

        # 2. Connect to previous auto-logged marker
        if self.last_auto_wp_id is not None:
            self.csv_logger.add_connection(self.last_auto_wp_id, new_id)

        self.last_auto_wp_id = new_id

