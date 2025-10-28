from frontend.gui_main_window import Ui_guiMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal


class MainWindow(QMainWindow):  
    can_setting = Signal(bool, bool) #set, reset 
    kill_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)

        self.kill_variable = False

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
        #you can connect to can_status to update this
        pass
        

    # Buttons functions
    def can_reset_clicked(self):
        self.can_setting.emit(False, True)
        pass

    def can_set_clicked(self):
        self.can_setting.emit(True, False)
        pass

    def kill_switch_clicked(self):
        print("killing signal initiated")
        self.kill_signal.emit(True)
        pass