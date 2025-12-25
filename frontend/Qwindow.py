from frontend.gui_main_window import Ui_guiMainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, QUrl
import csv
import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtCore import Signal
import math
from PySide6.QtCore import QUrl
from components.csvFileComponent import csvFileComponent

class MainWindow(QMainWindow):
    kill_signal = Signal(bool)
    colour_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)

        # Buttons
        self.ui.KillSwitchButton.clicked.connect(self.kill_switch_clicked)
        self.colour_buttons = {
        "red": self.ui.RedButton,
        "green": self.ui.GreenButton,
        "blue": self.ui.BlueButton,
        "yellow": self.ui.YellowButton,
        "orange": self.ui.OrangeButton,
        "purple": self.ui.PurpleButton
        }

    # Connect all buttons to handler with their name
        for name, btn in self.colour_buttons.items():
            btn.clicked.connect(lambda checked, n=name: self.colour_button_clicked(n))

        # build absolute path relative to this file
        self.ui.webEngineView.load(QUrl("http://localhost:8000/map.html"))
        
        # CSV viewer
        self.csv_file_path = "waypoints.csv"
        self.csv_viewer = csvFileComponent(self.csv_file_path)
        self.ui.csvFile.setModel(self.csv_viewer)
        header = self.ui.csvFile.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Load Leaflet map
        self.ui.webEngineView.load(QUrl("http://localhost:8000/map.html"))
        self.ui.webEngineView.loadFinished.connect(self.on_map_loaded)

        self.current_yaw = 0.0 


    # ===============================
    # MAP / WAYPOINT HANDLING
    # ===============================

    def on_map_loaded(self):
        print("Map loaded, loading waypoints")
        self.load_waypoints("/home/specapoorv/pythonGui/waypoints.csv")

    def load_waypoints(self, csv_path):
        waypoints = []
        try:
            with open(csv_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    waypoints.append({
                        "lat": float(row["lat"]),
                        "lon": float(row["lon"]),
                        "label": row.get("label", "")
                    })

            js = f"""
            clearMarkers();
            addMarkers({json.dumps(waypoints)});
            """
            self.ui.webEngineView.page().runJavaScript(js)

        except Exception as e:
            print("Error loading waypoints:", e)

    # ===============================
    # ROS → UI UPDATERS
    # ===============================

    def update_gps(self, latitude, longitude):
        self.ui.GPSValuesLabel.setText(f"{latitude:.6f}, {longitude:.6f}")
        
        js = f"updateRoverPosition({latitude}, {longitude});"
        self.ui.webEngineView.page().runJavaScript(js)

    def update_yaw(self, yaw):
        self.yaw = yaw

        js = f"updateRoverYaw({yaw});"
        self.ui.webEngineView.page().runJavaScript(js)


    def update_odom(self, x, y, yaw):
        self.current_yaw = yaw
        self.ui.OdomValueLabel.setText(f"{x:.2f} {y:.2f} {yaw:.2f}")
        
        # yaw_deg = math.degrees(yaw)
        # yaw_deg -= 90  # adjust if needed
        
        # js = f"updateRoverYaw({yaw_deg});"
        # self.ui.webEngineView.page().runJavaScript(js)

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

    # ===============================
    # UI ACTIONS
    # ===============================

    def kill_switch_clicked(self):
        print("killing signal initiated")
        self.kill_signal.emit(True)

    def colour_button_clicked(self, colour_name):
        #depending on button
        print(f"COLOUR OVERRIDE INITIATED: {colour_name}")
        self.colour_signal.emit(colour_name)
