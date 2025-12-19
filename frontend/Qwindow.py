from frontend.gui_main_window import Ui_guiMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal
import os
from PySide6.QtCore import QUrl


class MainWindow(QMainWindow):  
    kill_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)

        self.kill_variable = False

        # Buttons
        self.ui.KillSwitchButton.clicked.connect(self.kill_switch_clicked)
        # build absolute path relative to this file
        self.ui.webEngineView.load(QUrl("http://localhost:8000/map.html"))

    # Updater functions
    def update_gps(self, latitude, longitude):
        self.ui.GPSValuesLabel.setText(f"{latitude:.6f}, {longitude:.6f}")
        self.ui.webEngineView.page().runJavaScript(f"updateRover({latitude}, {longitude});")

    
    def update_odom(self, x, y, yaw):
        self.ui.OdomValueLabel.setText(f"{x:.2f} {y:.2f} {yaw:.2f}")
    
    def update_battery(self, battery):
        # self.ui.batteryValueLabel.setText(f"{battery:.2f}%")
        pass

    def update_mode(self, mode):
        self.ui.ModeValueLabel.setText(f"{mode}")

    def update_config(self, config):
        self.ui.ConfigValueLabel.setText(config)

    def update_twist(self, vel, omega):
        self.ui.VelocityValueLabel.setText(f"{vel}")
        self.ui.OmegaValueLabel.setText(f"{omega}")

    def update_encoder_angles(self, fl, fr, bl, br):
        self.ui.FrontLeftEncoderText.setText(f"{fl}")
        self.ui.FrontRightEncoderText.setText(f"{fr}")
        self.ui.BackLeftEncoderText.setText(f"{bl}")
        self.ui.BackRightEncoderText.setText(f"{br}")

    # Buttons functions
    def kill_switch_clicked(self):
        print("killing signal initiated")
        self.kill_signal.emit(True)
        pass