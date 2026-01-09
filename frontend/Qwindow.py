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
from PySide6.QtWebChannel import QWebChannel
from components.csvFileComponent import csvFileComponent
from backend.csv_manager import CSVLogger
from backend.qwebchannel import MapBackend
from pathlib import Path
import os


class MainWindow(QMainWindow):
    kill_signal = Signal(bool)
    colour_signal = Signal(str)
    autolog_signal = Signal(bool)

    brightness_signal = Signal(int, int)  # cam_id, value
    contrast_signal   = Signal(int, int)
    zoom_signal       = Signal(int, int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)

        # Buttons
        self.ui.KillSwitchButton.clicked.connect(self.kill_switch_clicked)
        self.colour_buttons = {
            "red": self.ui.redButton,
            "green": self.ui.greenButton,
            "blue": self.ui.blueButton,
            "yellow": self.ui.yellowButton,
            "orange": self.ui.orangeButton,
            "purple": self.ui.purpleButton
        }
        self.ui.autologButton.toggled.connect(self.autologbtn_toggled)
        for name, btn in self.colour_buttons.items():
            btn.clicked.connect(lambda checked, n=name: self.colour_button_clicked(n))

        # ===== BRIGHTNESS SLIDERS =====
        self.ui.brightnessSlider1.valueChanged.connect(lambda v: self.on_brightness_changed(1, v))
        self.ui.brightnessSlider2.valueChanged.connect(lambda v: self.on_brightness_changed(2, v))
        self.ui.brightnessSlider3.valueChanged.connect(lambda v: self.on_brightness_changed(3, v))
        self.ui.brightnessSlider4.valueChanged.connect(lambda v: self.on_brightness_changed(4, v))

        # ===== CONTRAST SLIDERS =====
        self.ui.contrastSlider1.valueChanged.connect(lambda v: self.on_contrast_changed(1, v))
        self.ui.contrastSlider2.valueChanged.connect(lambda v: self.on_contrast_changed(2, v))
        self.ui.contrastSlider3.valueChanged.connect(lambda v: self.on_contrast_changed(3, v))
        self.ui.contrastSlider4.valueChanged.connect(lambda v: self.on_contrast_changed(4, v))

        # ===== ZOOM SLIDERS =====
        self.ui.zoomSlider1.valueChanged.connect(lambda v: self.on_zoom_changed(1, v))
        self.ui.zoomSlider2.valueChanged.connect(lambda v: self.on_zoom_changed(2, v))
        self.ui.zoomSlider3.valueChanged.connect(lambda v: self.on_zoom_changed(3, v))
        self.ui.zoomSlider4.valueChanged.connect(lambda v: self.on_zoom_changed(4, v))

        # CSV viewer
        self.csv_file_path = "waypoints.csv"
        self.waypoint_log_file_path = "push_into_ananth.csv"
        self.csv_viewer = csvFileComponent(self.csv_file_path)
        self.ui.csvFile.setModel(self.csv_viewer)
        header = self.ui.csvFile.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Map
        map_path = Path(__file__).parent.parent / "offline_map/map.html"
        print("Loading map from:", map_path)
        print("Exists?", os.path.exists(map_path))
        
        self.map_backend = MapBackend(csv_path=self.csv_file_path, waypoint_log_csv=self.waypoint_log_file_path)
        self.channel = QWebChannel()
        self.channel.registerObject("mapBackend", self.map_backend)
        self.ui.webEngineView.page().setWebChannel(self.channel)
        self.ui.webEngineView.load(QUrl.fromLocalFile(str(map_path)))
        self.ui.webEngineView.loadFinished.connect(self.on_map_loaded)

        self.current_yaw = 0.0 

    def on_map_loaded(self):
        print("Map loaded, loading waypoints")
        self.load_waypoints()
    
    def load_waypoints(self, csv_path=None):
        try:
            waypoints = self.map_backend.get_waypoints_for_map()

            js = f"""
            clearMarkers();
            addMarkers({json.dumps(waypoints)});
            drawConnectionsFromMarkers();
            """
            self.ui.webEngineView.page().runJavaScript(js)

        except Exception as e:
            print("Error loading waypoints:", e)

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

    def update_mode(self, mode):
        self.ui.ModeValueLabel.setText(f"{mode}")

    def update_config(self, config):
        self.ui.ConfigValueLabel.setText(config)

    def update_twist(self, vel, omega):
        self.ui.VelocityValueLabel.setText(f"{vel:.2f}")
        self.ui.OmegaValueLabel.setText(f"{omega:.2f}")

    def update_encoder_angles(self, fl, fr, bl, br):
        self.ui.FrontLeftEncoderText.setText(f"{fl}")
        self.ui.FrontRightEncoderText.setText(f"{fr}")
        self.ui.BackLeftEncoderText.setText(f"{bl}")
        self.ui.BackRightEncoderText.setText(f"{br}")

    
    def update_frequency(self, frequency):
        self.ui.frequencyValueLabel.setText(f"{frequency} GHz")
        
    def update_noise(self, noise):
        self.ui.noiseValueLabel.setText(f"{noise}")

    def on_brightness_changed(self, cam_id, value):
        print(f"Brightness cam {cam_id}: {value}")
        self.brightness_signal.emit(cam_id, value)

    def on_contrast_changed(self, cam_id, value):
        print(f"Contrast cam {cam_id}: {value}")
        self.contrast_signal.emit(cam_id, value)

    def on_zoom_changed(self, cam_id, value):
        print(f"Zoom cam {cam_id}: {value}")
        self.zoom_signal.emit(cam_id, value)

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

    def autologbtn_toggled(self, checked):
        self.autolog_signal.emit(checked)
        if checked: 
            self.ui.autologButton.setText("AUTOLOG ON")
        else:
            self.ui.autologButton.setText("AUTOLOG OFF")