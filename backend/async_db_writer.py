# influx_writer.py
from PySide6.QtCore import QThread, Signal
from influxdb_client import InfluxDBClient, Point, WriteOptions
import time
import queue

class InfluxDBWriter(QThread):
    # Optional: emit signal on successful write
    flushed = Signal(int)  # number of points written

    def __init__(self, influx_url, token, org, bucket, flush_interval=1.0, parent=None):
        super().__init__(parent)
        self.client = InfluxDBClient(url=influx_url, token=token, org=org)
        self.write_api = self.client.write_api(
            write_options=WriteOptions(batch_size=500, flush_interval=flush_interval*1000)
        )
        self.bucket = bucket
        self.queue = queue.Queue()
        self.running = True

    def run(self):
        print("[InfluxDBWriter] Thread started.")
        while self.running:
            batch = []
            try:
                while not self.queue.empty():
                    batch.append(self.queue.get_nowait())
            except queue.Empty:
                pass

            if batch:
                points = [Point("sensor_data").field(k, v) for msg in batch for k, v in msg.items()]
                self.write_api.write(bucket=self.bucket, record=points)
                self.flushed.emit(len(points))
            time.sleep(0.5)  # adjust flush interval

    def enqueue(self, msg: dict):
        """Call this from main.py or any signal callback to queue data for writing"""
        self.queue.put(msg)

    def stop(self):
        self.running = False
        self.wait()
        self.client.close()
