import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                              QDockWidget, QSplitter, QTabWidget, QStackedWidget,
                              QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                              QTextEdit, QListWidget, QProgressBar, QLCDNumber)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPalette, QColor

class RoverGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rover Control Interface")
        self.setGeometry(100, 100, 1400, 900)
        
        # Set up the main interface
        self.setup_ui()
        
        # Optional: Add some demo data updates
        self.setup_demo_timer()
    
    def setup_ui(self):
        """Set up the main user interface with different panel approaches"""
        
        # APPROACH 1: Central widget with splitters (good for camera feeds)
        self.setup_central_area()
        
        # APPROACH 2: Dockable panels (good for telemetry, controls)
        self.setup_dockable_panels()
        
        # APPROACH 3: Tabbed interface (alternative organization)
        # Uncomment the line below to try tabs instead of splitters
        # self.setup_tabbed_interface()
    
    def setup_central_area(self):
        """Create main content area with splitters for camera feeds"""
        
        # Create camera feed placeholders
        self.camera1 = QLabel("Camera Feed 1\n(Front Camera)")
        self.camera1.setStyleSheet("QLabel { background-color: #2b2b2b; color: white; font-size: 16px; }")
        self.camera1.setAlignment(Qt.AlignCenter)
        self.camera1.setMinimumSize(400, 300)
        
        self.camera2 = QLabel("Camera Feed 2\n(Rear Camera)")
        self.camera2.setStyleSheet("QLabel { background-color: #2b2b2b; color: white; font-size: 16px; }")
        self.camera2.setAlignment(Qt.AlignCenter)
        self.camera2.setMinimumSize(400, 300)
        
        # Create horizontal splitter for side-by-side cameras
        camera_splitter = QSplitter(Qt.Horizontal)
        camera_splitter.addWidget(self.camera1)
        camera_splitter.addWidget(self.camera2)
        camera_splitter.setSizes([700, 700])  # Equal initial sizes
        
        # Create control panel for the center
        control_panel = self.create_control_panel()
        
        # Create vertical splitter to stack cameras above controls
        main_splitter = QSplitter(Qt.Vertical)
        main_splitter.addWidget(camera_splitter)
        main_splitter.addWidget(control_panel)
        main_splitter.setSizes([600, 200])  # Cameras get more space
        
        # Set as central widget
        self.setCentralWidget(main_splitter)
    
    def create_control_panel(self):
        """Create a control panel with kill button and basic controls"""
        
        control_widget = QWidget()
        layout = QHBoxLayout(control_widget)
        
        # Kill button (emergency stop)
        self.kill_button = QPushButton("🛑 EMERGENCY STOP")
        self.kill_button.setStyleSheet("""
            QPushButton {
                background-color: #cc0000;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
                border: 3px solid #ff0000;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #ff0000;
            }
            QPushButton:pressed {
                background-color: #990000;
            }
        """)
        self.kill_button.clicked.connect(self.emergency_stop)
        
        # Status indicators
        status_widget = QWidget()
        status_layout = QVBoxLayout(status_widget)
        
        status_layout.addWidget(QLabel("System Status:"))
        self.battery_bar = QProgressBar()
        self.battery_bar.setValue(85)
        self.battery_bar.setFormat("Battery: %p%")
        
        self.signal_bar = QProgressBar()
        self.signal_bar.setValue(70)
        self.signal_bar.setFormat("Signal: %p%")
        
        status_layout.addWidget(self.battery_bar)
        status_layout.addWidget(self.signal_bar)
        
        # Add to main layout
        layout.addWidget(self.kill_button)
        layout.addWidget(status_widget)
        layout.addStretch()  # Push everything to the left
        
        return control_widget
    
    def setup_dockable_panels(self):
        """Create dockable panels for telemetry and additional controls"""
        
        # Left panel: Telemetry data
        telemetry_dock = QDockWidget("Telemetry", self)
        telemetry_widget = QWidget()
        telemetry_layout = QVBoxLayout(telemetry_widget)
        
        # Add telemetry displays
        telemetry_layout.addWidget(QLabel("GPS Coordinates:"))
        self.gps_display = QLabel("Lat: 12.9716° N\nLon: 77.5946° E")
        self.gps_display.setStyleSheet("QLabel { background-color: #f0f0f0; padding: 5px; }")
        
        telemetry_layout.addWidget(QLabel("Speed:"))
        self.speed_lcd = QLCDNumber()
        self.speed_lcd.display(0.0)
        
        telemetry_layout.addWidget(QLabel("System Log:"))
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(150)
        self.log_display.append("System initialized...")
        self.log_display.append("Cameras connected...")
        self.log_display.append("Ready for operation...")
        
        telemetry_layout.addWidget(self.gps_display)
        telemetry_layout.addWidget(self.speed_lcd)
        telemetry_layout.addWidget(self.log_display)
        telemetry_layout.addStretch()
        
        telemetry_dock.setWidget(telemetry_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, telemetry_dock)
        
        # Right panel: Mission controls
        mission_dock = QDockWidget("Mission Control", self)
        mission_widget = QWidget()
        mission_layout = QVBoxLayout(mission_widget)
        
        # Mission buttons
        self.start_mission_btn = QPushButton("Start Mission")
        self.start_mission_btn.setStyleSheet("QPushButton { background-color: #009900; color: white; padding: 8px; }")
        
        self.pause_mission_btn = QPushButton("Pause Mission")
        self.pause_mission_btn.setStyleSheet("QPushButton { background-color: #ff9900; color: white; padding: 8px; }")
        
        self.return_home_btn = QPushButton("Return to Base")
        self.return_home_btn.setStyleSheet("QPushButton { background-color: #0066cc; color: white; padding: 8px; }")
        
        mission_layout.addWidget(QLabel("Mission Controls:"))
        mission_layout.addWidget(self.start_mission_btn)
        mission_layout.addWidget(self.pause_mission_btn)
        mission_layout.addWidget(self.return_home_btn)
        mission_layout.addStretch()
        
        mission_dock.setWidget(mission_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, mission_dock)
    
    def setup_tabbed_interface(self):
        """Alternative: Create a tabbed interface instead of splitters"""
        
        tab_widget = QTabWidget()
        
        # Tab 1: Camera feeds
        camera_tab = QWidget()
        camera_layout = QHBoxLayout(camera_tab)
        
        cam1 = QLabel("Camera 1 Feed")
        cam1.setStyleSheet("QLabel { background-color: #2b2b2b; color: white; }")
        cam1.setAlignment(Qt.AlignCenter)
        cam1.setMinimumSize(400, 300)
        
        cam2 = QLabel("Camera 2 Feed")
        cam2.setStyleSheet("QLabel { background-color: #2b2b2b; color: white; }")
        cam2.setAlignment(Qt.AlignCenter)
        cam2.setMinimumSize(400, 300)
        
        camera_layout.addWidget(cam1)
        camera_layout.addWidget(cam2)
        
        # Tab 2: Telemetry
        telemetry_tab = QWidget()
        telemetry_tab_layout = QVBoxLayout(telemetry_tab)
        telemetry_tab_layout.addWidget(QLabel("Detailed telemetry data would go here..."))
        
        # Tab 3: Controls
        controls_tab = QWidget()
        controls_tab_layout = QVBoxLayout(controls_tab)
        controls_tab_layout.addWidget(self.create_control_panel())
        
        # Add tabs
        tab_widget.addTab(camera_tab, "📹 Cameras")
        tab_widget.addTab(telemetry_tab, "📊 Telemetry")
        tab_widget.addTab(controls_tab, "🎮 Controls")
        
        # Uncomment this line to use tabs instead of splitters
        # self.setCentralWidget(tab_widget)
    
    def setup_demo_timer(self):
        """Set up a timer to simulate live data updates"""
        
        self.demo_timer = QTimer()
        self.demo_timer.timeout.connect(self.update_demo_data)
        self.demo_timer.start(2000)  # Update every 2 seconds
        
        self.demo_counter = 0
    
    def update_demo_data(self):
        """Update demo data to simulate live telemetry"""
        
        self.demo_counter += 1
        
        # Update speed display
        import random
        speed = random.uniform(0, 15.5)
        self.speed_lcd.display(speed)
        
        # Update battery (slowly decreasing)
        current_battery = self.battery_bar.value()
        if current_battery > 0:
            self.battery_bar.setValue(max(0, current_battery - 1))
        
        # Add log entries
        log_messages = [
            f"Speed: {speed:.1f} m/s",
            f"Battery: {self.battery_bar.value()}%",
            "Navigation system OK",
            "Communication link stable",
            "Sensors operational"
        ]
        
        if self.demo_counter % 3 == 0:  # Every third update
            message = random.choice(log_messages)
            self.log_display.append(f"[{self.demo_counter:03d}] {message}")
    
    def emergency_stop(self):
        """Handle emergency stop button"""
        
        print("🚨 EMERGENCY STOP ACTIVATED!")
        self.log_display.append("⚠️  EMERGENCY STOP ACTIVATED!")
        
        # In a real application, this would send stop commands to the rover
        # For now, just show a visual indication
        self.kill_button.setText("🛑 STOPPED")
        self.kill_button.setStyleSheet("""
            QPushButton {
                background-color: #990000;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
                border: 3px solid #cc0000;
                border-radius: 10px;
            }
        """)

def main():
    """Main application entry point"""
    
    app = QApplication(sys.argv)
    
    # Set application-wide style
    app.setStyle('Fusion')  # Modern cross-platform style
    
    # Create and show the main window
    rover_gui = RoverGUI()
    rover_gui.show()
    
    # Start the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
