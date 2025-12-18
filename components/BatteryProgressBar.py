from PySide6.QtWidgets import QProgressBar, QStyleOptionProgressBar, QStyle
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect

class BatteryProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextVisible(True)
        
    def paintEvent(self, event):
        # Draw the standard progress bar
        super().paintEvent(event)
        
        # Now draw the text with two colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Get the progress bar rectangle
        rect = self.rect()
        
        # Calculate how much of the bar is filled
        progress_percent = (self.value() - self.minimum()) / (self.maximum() - self.minimum())
        filled_width = int(rect.width() * progress_percent)
        
        # Text to display
        text = self.text()
        
        # Draw text in white on the filled portion (left side)
        if filled_width > 0:
            painter.setClipRect(0, 0, filled_width, rect.height())
            painter.setPen(QColor(24, 24, 29))  # Color on filled chunk
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)
        
        # Draw text in black on the unfilled portion (right side)
        if filled_width < rect.width():
            painter.setClipRect(filled_width, 0, rect.width() - filled_width, rect.height())
            painter.setPen(QColor(119, 118, 123))  # Color on unfilled background
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)
