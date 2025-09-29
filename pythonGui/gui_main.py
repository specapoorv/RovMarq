from gui_main_window import Ui_guiMainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, Signal, QTimer

import rclpy as r
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, Imu
from std_msgs.msg import Float32
from tf_transformations import euler_from_quaternion

class GUIUpdaterNode(Node, QObject):
    # Class attributes here itseems i dont know why but looks cool
    gps_updated = Signal(float, float)
    yaw_updated = Signal(float)
    battery_updated = Signal(float)
    latency_updated = Signal(float)
    can_status_updated = Signal(float) # Change this based on the topic?

    def __init__(self):
        Node.__init__(self, "gui_update_node")
        QObject.__init__(self)

        # Subscribers
        self.create_subscription(NavSatFix, "/gps_topic", self.gps_callback, 10)
        self.create_subscription(Imu, "/imu_topic", self.imu_callback, 10)
        self.create_subscription(Float32, "/battery_topic", self.battery_callback, 10)
        self.create_subscription(Float32, "/latency_topic", self.latency_callback, 10)
        self.create_subscription(Float32, "/can_status_topic", self.can_status_callback, 10)


    def gps_callback(self, gps_msg: NavSatFix):
        self.gps_updated.emit(gps_msg.latitude, gps_msg.longitude)


    def imu_callback(self, imu_msg: Imu):
        quaternion = [imu_msg.orientation.x, imu_msg.orientation.y, imu_msg.orientation.z, imu_msg.orientation.w]
        _, _, yaw = euler_from_quaternion(quaternion)
        self.yaw_updated.emit(yaw)


    def battery_callback(self, battery_msg: Float32):
        self.battery_updated.emit(battery_msg.data)


    def latency_callback(self, latency_msg: Float32):
        self.latency_updated.emit(latency_msg.data)


    def can_status_callback(self, can_status_msg: Float32):
        self.can_status_updated.emit(can_status_msg.data)


class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)

        # Button Clicks
        self.ui.canResetButton.clicked.connect(self.can_reset_clicked)
        self.ui.canSetButton.clicked.connect(self.can_set_clicked)
        self.ui.KillSwitchButton.clicked.connect(self.kill_switch_clicked)


    # Updater functions
    def update_gps(self, latitude, longitude):
        self.ui.GPSValuesLabel.setText(f"{latitude:.2f}, {longitude:.2f}")
    

    def update_yaw(self, yaw):
        self.ui.YawValueLabel.setText(f"{yaw:.2f} deg")

    
    def update_battery(self, battery):
        self.ui.batteryValueLabel.setText(f"{battery:.2f}%")


    def update_latency(self, latency):
        self.ui.LatencyValueLabel.setText(f"{latency:.2f} ms")


    def update_can_status(self, can_status):
        # How are can statuses given?
        pass
        
    

    # Buttons functions
    def can_reset_clicked(self):
        # CAN reset logic here
        pass

    def can_set_clicked(self):
        # CAN set logic goes here
        pass

    def kill_switch_clicked(self):
        # Wonder what all I will have to do to kill from here
        pass

    
if __name__ == "__main__":
    r.init()  # Initialize ROS2 Python
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    gui_node = GUIUpdaterNode()

    gui_node.gps_updated.connect(window.update_gps)
    gui_node.yaw_updated.connect(window.update_yaw)
    gui_node.battery_updated.connect(window.update_battery)

    # QTimer to periodically call rclpy.spin_once without blocking Qt loop
    ros_timer = QTimer()
    ros_timer.timeout.connect(lambda: r.spin_once(gui_node, timeout_sec=0))
    ros_timer.start(10)  # Call every 10 ms, adjust as needed

    exit_code = app.exec()

    gui_node.destroy_node()
    r.shutdown()
    sys.exit(exit_code)
