from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

class SimpleMapWidget(QWidget):
    def __init__(self, width=400, height=400):
        super().__init__()
        self.setFixedSize(width, height)
        self.path = []  # list of (lat, lon)
        self.rover_pos = None  # latest rover position
        self.lat_min, self.lat_max = 12.97, 12.98
        self.lon_min, self.lon_max = 77.59, 77.60

    def update_from_db(self, lat, lon):
        """Call this whenever a new point is fetched from DB/fetcher"""
        self.rover_pos = (lat, lon)
        self.path.append((lat, lon))
        self.update()  # repaint widget

    def paintEvent(self, event):
        if not self.rover_pos:
            return

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("white"))

        pen = QPen(Qt.blue, 2)
        painter.setPen(pen)
        for i in range(1, len(self.path)):
            x1, y1 = self.latlon_to_xy(*self.path[i-1])
            x2, y2 = self.latlon_to_xy(*self.path[i])
            painter.drawLine(x1, y1, x2, y2)

        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        painter.setBrush(QColor("red"))
        x, y = self.latlon_to_xy(*self.rover_pos)
        painter.drawEllipse(x-5, y-5, 10, 10)

    def latlon_to_xy(self, lat, lon):
        x = (lon - self.lon_min) / (self.lon_max - self.lon_min) * self.width()
        y = self.height() - (lat - self.lat_min) / (self.lat_max - self.lat_min) * self.height()
        return int(x), int(y)
