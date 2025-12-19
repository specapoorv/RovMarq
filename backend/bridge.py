from PySide6.QtCore import QObject, Signal
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32, Int8, String
from nav_msgs.msg import Odometry
from rclpy.qos import QoSProfile, ReliabilityPolicy
"""monkey patching numpy here in newer versions np.float is deprecated, and who tf uses it"""
import numpy as np
if not hasattr(np, 'float'):
    np.float = float

from tf_transformations import euler_from_quaternion
from frontend.Qwindow import MainWindow
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Float32MultiArray
import subprocess


class ROSQtBridge(Node, QObject):
    kill_signal = Signal(bool)
    '''
    bridge just pushes the signals from ros to Qt, we assign a worker that pushes the signals without blocking Qt
    this does no processing nothing, just raw data directly streamed with near zero latency 
    '''
    gps_updated = Signal(float, float)
    odom_updated = Signal(float, float, float)
    battery_updated = Signal(float)
    latency_updated = Signal(float)
    steering_angles = Signal(float, float, float, float)
    config_updated = Signal(str)
    mode_updated = Signal(int)
    twist_updated = Signal(float, float)
    encoder_angles_updated = Signal(float, float, float, float)

    def __init__(self):
        Node.__init__(self, "ros_qt_bridge")
        QObject.__init__(self)

        self.best_effort = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.create_subscription(NavSatFix, "/gps/fix", self.gps_callback, 10)
        #fix imu to take from odom
        self.create_subscription(Odometry, "/rtabmap/odom", self.odom_callback, self.best_effort)
        self.create_subscription(Float32, "/battery_topic", self.battery_callback, 10)
        # self.create_subscription(Float32, "/latency_topic", self.latency_callback, 10)
        self.create_subscription(Float32MultiArray, "/enc_auto", self.steering_callback, 10)
        self.create_subscription(Int8, "/mode", self.mode_callback, 10)
        self.create_subscription(String, "/config", self.config_callback, 10)
        self.create_subscription(Float32MultiArray, "/vel", self.vel_callback, 10)
        self.motor_publisher = self.create_publisher(Int32MultiArray, "/motor_pwm", 10)


    def gps_callback(self, msg: NavSatFix):
        self.get_logger().info(f"{msg.latitude}, {msg.longitude}")
        self.gps_updated.emit(msg.latitude, msg.longitude)

    def vel_callback(self, twist: Float32MultiArray):
        vel = twist.data[0]
        omega = twist.data[1]

        self.twist_updated.emit(vel, omega)

    def odom_callback(self, msg: Odometry):
        q = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
             msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
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

    # def latency_callback(self, msg):
    #     self.latency_updated.emit(msg.data)

    def kill_handler(self, killed):
        if killed:
            print("handling kill switch, ded")
            pwm_msg = Int32MultiArray()
            pwm_msg.data = [0,0,0,0,0,0,0,0]
            self.motor_publisher.publish(pwm_msg)


    def steering_callback(self, msg):
        data = msg.data
        #self.get_logger().info(f"{len(data)}")
 
        fl = data[0]    # Front Left
        fr = data[1]    # Front Right
        bl = data[2]    # Back Left
        br = data[3]    # Back Right

        self.encoder_angles_updated.emit(fl, fr, bl, br)
        self.steering_angles.emit(fl, fr, bl, br)




 