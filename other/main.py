# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from fetchers import GPSFetcher, InfluxDBFetcher
from rover3d_widget import Rover3DWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rover Dashboard")
        self.resize(1200, 800)

        # --- 3D Rover widget ---
        self.rover3d = Rover3DWidget()
        self.setCentralWidget(self.rover3d)

        # --- GPS Fetcher ---
        self.gps_fetcher = GPSFetcher(
            influx_url="http://localhost:8086",
            token="my-token",
            org="my-org",
            bucket="rover_data",
            sensor_id="gps1",
            poll_interval=0.5,
            parent=self
        )
        self.gps_fetcher.gps_ready.connect(self.rover3d.update_rover_position)
        self.gps_fetcher.start()

        # --- Orientation Fetcher ---
        self.orientation_fetcher = InfluxDBFetcher(
            influx_url="http://localhost:8086",
            token="my-token",
            org="my-org",
            bucket="rover_data",
            poll_interval=0.033,  # ~30Hz
            parent=self
        )
        self.orientation_fetcher.orientation_ready.connect(self.rover3d.update_orientation)
        self.orientation_fetcher.start()

    def closeEvent(self, event):
        # stop threads cleanly
        self.gps_fetcher.stop()
        self.orientation_fetcher.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



# main.py
import sys
from PyQt6.QtWidgets import QApplication
from frontend.main_window import MainWindow
from fetchers import GPSFetcher, InfluxDBFetcher

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # --- GPS Fetcher ---
    gps_fetcher = GPSFetcher(...)
    gps_fetcher.gps_ready.connect(window.update_gps)
    gps_fetcher.start()

    # --- Orientation Fetcher ---
    imu_fetcher = InfluxDBFetcher(...)
    imu_fetcher.orientation_ready.connect(window.update_yaw)
    imu_fetcher.start()

    window.show()

    # Graceful cleanup
    exit_code = app.exec()
    gps_fetcher.stop()
    imu_fetcher.stop()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
