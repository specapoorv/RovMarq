from PySide6.QtCore import QThread, Signal
from influxdb_client import InfluxDBClient
import time

class gpsFetcher(QThread):
    gps_fetched = Signal(float, float, float)  # lat, lon, alt

    def __init__(self, influx_url, token, org, bucket, poll_interval=0.5, parent=None):
        super().__init__(parent)
        self.client = InfluxDBClient(url=influx_url, token=token, org=org)
        self.token = token
        self.query_api = self.client.query_api()
        self.bucket = bucket
        self.poll_interval = poll_interval
        self.running = True


    def run(self):
        while self.running:
            query = f'''
            from(bucket:"{self.bucket}")
            |> range(start: -2s)
            |> filter(fn: (r) => r["_measurement"] == "sensor_data")
            |> filter(fn: (r) => r["_field"] == "latitude" or r["_field"] == "longitude")
            '''


            try:
                tables = self.query_api.query(query)
                lat = lon = alt = None
                for table in tables:
                    for record in table.records:
                        if record.get_field() == "lat":
                            lat = record.get_value()
                        elif record.get_field() == "lon":
                            lon = record.get_value()
                        elif record.get_field() == "alt":
                            alt = record.get_value()
                self.gps_fetched.emit(lat, lon, alt)
            except Exception as e:
                print("gpsFetcher error:", e)
            
            time.sleep(self.poll_interval)


    def stop(self):
        self.running = False
        self.wait()
        self.client.close()
