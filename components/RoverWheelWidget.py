from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QBrush, QColor, QPen
from PySide6.QtCore import Qt, QRectF, QPointF

class RoverWheelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.wheel_angles = [0, 0, 0, 0]  # FL, FR, BL, BR angles
        self.setMinimumSize(400, 400)
        
    def set_wheel_angles(self, fl, fr, bl, br):
        """Update wheel angles from ROS2 subscriber"""
        self.wheel_angles = [fl, fr, bl, br]
        self.update()  # Trigger repaint
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw center rover body (gray rectangle)
        body_rect = QRectF(100, 100, 200, 200)
        painter.fillRect(body_rect, QColor(160, 160, 160))
        
        # Wheel positions: [x, y, angle_index]
        wheel_positions = [
            (80, 50, 0),   # Front-left
            (320, 50, 1),   # Front-right
            (80, 350, 2),  # Back-left
            (320, 350, 3)   # Back-right
        ]
        
        for x, y, angle_idx in wheel_positions:
            self.draw_wheel_assembly(painter, x, y, self.wheel_angles[angle_idx])

        self.draw_side_bars(painter=painter, wheel_position_1=wheel_positions[0], wheel_position_2=wheel_positions[2])
        self.draw_side_bars(painter=painter, wheel_position_1=wheel_positions[1], wheel_position_2=wheel_positions[3])
            
    def draw_wheel_assembly(self, painter: QPainter, x, y, angle):
        """Draw wheel assembly with rotation"""
        painter.save()
        
        # Translate to wheel center for rotation
        center = QPointF(x, y)
        painter.translate(center)
        painter.rotate(angle)  # Rotate by angle from ROS2
        painter.translate(-center)
        
        # Draw black rotating rectangle (the wheel module)
        wheel_rect = QRectF(x - 17, y - 42, 34, 84)
        painter.fillRect(wheel_rect, QColor(200, 200, 200))
        wheel_rect = QRectF(x - 15, y - 40, 30, 80)
        painter.fillRect(wheel_rect, QColor(0, 0, 0))
        
        # Draw gray box with "0" label
        label_rect = QRectF(x - 12, y - 15, 24, 30)
        painter.fillRect(label_rect, QColor(120, 120, 120))
        
        painter.restore()
        
        # Draw curved arrow indicator (non-rotating)
        painter.setPen(QPen(Qt.GlobalColor.white, 2))
        # Add arrow drawing code here if needed


    def draw_side_bars(self, painter: QPainter, wheel_position_1, wheel_position_2):
        painter.save()
        bar_rect = QRectF(wheel_position_1[0] - 5, wheel_position_1[1] - 15, 10, wheel_position_2[1] - wheel_position_1[1])
        painter.fillRect(bar_rect, QColor(120, 120, 120))
        painter.restore()
