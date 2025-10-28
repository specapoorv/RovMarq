from PyQt6.QtCore import QThread, pyqtSignal
from influxdb_client import InfluxDBClient
import numpy as np
import time

class imuFetcher(QThread):
    orientation_ready = pyqtSignal(float, float, float)  # roll, pitch, yaw

    def __init__(self, influx_url, token, org, bucket, poll_interval=0.5, parent=None):
        super().__init__(parent)
        self.client = InfluxDBClient(url=influx_url, token=token, org=org)
        self.query_api = self.client.query_api()
        self.bucket = bucket
        self.poll_interval = poll_interval
        self.running = True

    def run(self):
        while self.running:
            query = f'''
                from(bucket:"{self.bucket}")
                |> range(start: -500ms)
                |> filter(fn: (r) => r["_measurement"] == "sensor_data")
                |> filter(fn: (r) => r["_field"] == "roll" or r["_field"] == "pitch" or r["_field"] == "yaw")
                |> mean()
            '''

            #we are writing in our database every 500 ms so we can look behind 500ms or we can do it 600 ms as well, if freuency is 30hz then we will have 15 data points always 
            try:
                tables = self.query_api.query(query)
                roll = pitch = yaw = None
                for table in tables:
                    for record in table.records:
                        if record.get_field() == "roll":
                            roll = record.get_value()
                        elif record.get_field() == "pitch":
                            pitch = record.get_value()
                        elif record.get_field() == "yaw":
                            yaw = record.get_value()
                self.orientation_ready.emit(roll, pitch, yaw)
            except Exception as e:
                print("Fetcher error:", e)

            time.sleep(self.poll_interval)

    def stop(self):
        self.running = False
        self.wait()
        self.client.close()
