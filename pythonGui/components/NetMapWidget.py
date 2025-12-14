from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import QTimer, Qt, QThread, Signal
from PySide6.QtGui import QPainter, QColor
import subprocess

DEVICES = [
    {"name": "Base Mikrotik", "ip": "10.42.0.99"},
    {"name": "Rover Mikrotik", "ip": "10.42.0.100"},
    {"name": "Jetson Orin", "ip": "10.42.0.253"},
    {"name": "Imou Camera", "ip": "10.42.0.69"},
    # {"name": "Adeesh's Laptop", "ip": "10.42.0.7"},
    # {"name": "Shri Hari's Laptop", "ip": "10.42.0.2"},
    # {"name": "Srivatsan's Laptop", "ip": "10.42.0.254"},
    # {"name": "Ananth's Laptop", "ip": "10.42.0.11"},
]


class StatusIndicator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(128, 128, 128)
        self.setFixedSize(20, 20)
    
    def set_color(self, color):
        self.color = QColor(color)
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        # use correct RenderHint enum
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        # use explicit PenStyle enum
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(3, 3, 14, 14)


class PingWorker(QThread):
    result = Signal(str, bool)
    
    def __init__(self):
        super().__init__()
        self.devices = DEVICES
        self.running = True
    
    def ping(self, ip):
        try:
            return subprocess.call(['ping', '-c', '1', '-W', '1', ip],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL) == 0
        except:
            return False
    
    def run(self):
        while self.running:
            for dev in self.devices:
                ip = dev["ip"]
                is_up = self.ping(ip)
                self.result.emit(ip, is_up)
            # call msleep as QThread static method to avoid attribute issues
            QThread.msleep(1000)
    
    def stop(self):
        self.running = False
        self.wait()


class NetMapWidget(QWidget):
    """Network Status Monitor matching Rover GUI theme"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.devices = DEVICES
        self.indicators = {}
        
        self.setup_ui()
        self.start_monitoring()
    
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # REMOVE: self.setStyleSheet(...) - now in Designer!
        
        # Header
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")  # ADD THIS
        # REMOVE: header_frame.setStyleSheet(...)
        
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(5, 8, 5, 8)
        
        header = QLabel("Network Status")
        header.setObjectName("headerLabel")  # ADD THIS
        # REMOVE: header.setStyleSheet(...)
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)
        main_layout.addWidget(header_frame)
        
        # Device list container
        devices_container = QWidget()
        # REMOVE: devices_container.setStyleSheet(...)
        devices_layout = QVBoxLayout(devices_container)
        devices_layout.setContentsMargins(10, 10, 10, 10)
        devices_layout.setSpacing(5)
        
        for dev in self.devices:
            device_frame = self.create_device_row(dev)
            devices_layout.addWidget(device_frame)
        
        devices_layout.addStretch()
        main_layout.addWidget(devices_container)

    def create_device_row(self, device):
        frame = QFrame()
        frame.setObjectName("deviceRow")  # ADD THIS    
        # REMOVE: frame.setStyleSheet(...)
        
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(8, 5, 8, 5)
        
        # Device name
        name_label = QLabel(device["name"])
        name_label.setObjectName("deviceName")  # ADD THIS
        # REMOVE: name_label.setStyleSheet(...)
        name_label.setFixedWidth(150)
        layout.addWidget(name_label)
        
        # IP address
        ip_label = QLabel(device["ip"])
        ip_label.setObjectName("deviceIP")  # ADD THIS
        # REMOVE: ip_label.setStyleSheet(...)
        ip_label.setFixedWidth(120)
        layout.addWidget(ip_label)
        
        layout.addStretch()
        
        indicator = StatusIndicator()
        layout.addWidget(indicator)
        
        self.indicators[device["ip"]] = indicator
        
        return frame

    
    def start_monitoring(self):
        self.worker = PingWorker()
        self.worker.result.connect(self.update_status)
        self.worker.start()
    
    def update_status(self, ip, is_up):
        if ip in self.indicators:
            color = "#00FF00" if is_up else "#FF0000"
            self.indicators[ip].set_color(color)
    
    def closeEvent(self, event):
        if hasattr(self, 'worker'):
            self.worker.stop()
        event.accept()
