from PySide6.QtCore import QObject, Signal
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, Imu
from std_msgs.msg import Float32
"""monkey patching numpy here in newer versions np.float is deprecated, and tf uses it"""
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
    yaw_updated = Signal(float)
    battery_updated = Signal(float)
    latency_updated = Signal(float)
    can_status = Signal(bool)
    steering_angles = Signal(float, float, float, float)

    imu_data_received = Signal(object)
       # Will send imu_msg to db_writer, remove no need

    def __init__(self):
        Node.__init__(self, "ros_qt_bridge")
        QObject.__init__(self)

        self.create_subscription(NavSatFix, "/gps/fix", self.gps_callback, 10)
        #fix imu to take from odom
        self.create_subscription(Imu, "/imu_topic", self.imu_callback, 10)
        self.create_subscription(Float32, "/battery_topic", self.battery_callback, 10)
        self.create_subscription(Float32, "/latency_topic", self.latency_callback, 10)
        self.create_subscription(Float32, "/can_status_topic", self.can_status_callback, 10)
        self.create_subscription(Float32MultiArray, "/enc_auto", self.steering_callback, 10)

        self.create_subscription(Imu, "/imu_topic", self.imu_log_callback, 10)

        self.motor_publisher = self.create_publisher(Int32MultiArray, "/motor_pwm", 10)


    def gps_callback(self, msg: NavSatFix):
        
        self.gps_updated.emit(msg.latitude, msg.longitude)

    def imu_callback(self, msg: Imu):
        q = [msg.orientation.x, msg.orientation.y,
             msg.orientation.z, msg.orientation.w]
        _, _, yaw = euler_from_quaternion(q)
        self.yaw_updated.emit(yaw)

    def battery_callback(self, msg):
        self.battery_updated.emit(msg.data)

    def latency_callback(self, msg):
        self.latency_updated.emit(msg.data)

    def can_status_callback(self, msg):
        self.can_status_updated.emit(msg.data)

    def imu_log_callback(self, msg):
        self.imu_data_received.emit(msg)

    def kill_handler(self, killed):
        if killed:
            print("handling kill switch, ded")
            pwm_msg = Int32MultiArray()
            pwm_msg.data = [0,0,0,0,0,0,0,0]
            self.motor_publisher.publish(pwm_msg)

    #runnin in ros thread?
    def get_can_status(self):
        try:
            output = subprocess.check_output(
                ["ip", "-details", "link", "show", "can0"], text=True
            )
            if "state UP" in output:
                return True
            else:
                return False
        except subprocess.CalledProcessError:
            return False

    def can_handler(self, set_flag, reset_flag):
        print(f"set_flag : {set_flag}, reset_flag : {reset_flag}")
        if set_flag:
            subprocess.run(["sudo", "ifconfig", "can0", "up"])
        elif reset_flag:
            subprocess.run(["sudo", "ifconfig", "can0", "down"])
            subprocess.run(["sudo", "ifconfig", "can0", "up"])


        is_running = self.get_can_status()
        print("can is running?...")
        print(is_running)
        self.can_status.emit(is_running) #emits true if its running

    def steering_callback(self, msg):
        data = msg.data
        #self.get_logger().info(f"{len(data)}")
 
        fl = data[1]   # Front Left
        fr = -data[4]  # Front Right
        bl = data[0]   # Back Left
        br = data[5]   # Back Right

        self.steering_angles.emit(fl, fr, bl, br)




 