from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt, QTimer, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QColor, QPalette

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from pyqttoast import Toast, ToastPreset

class Notifier:
    """
    A simple toast notification manager for PySide6/PyQt6.
    Usage:
        notifier = Notifier(parent_widget)
        notifier.success("SCP transfer completed!")
        notifier.error("Failed to send file.")
        notifier.info("Starting transfer...")
    """
    

    def __init__(self, parent: QWidget):
        self.parent = parent
        print("toast initiated")
        print(self.parent)

    def success(self, message: str, title: str = "Success", duration: int = 3000):
        self._show_toast(message, title, ToastPreset.SUCCESS, duration)

    def error(self, message: str, title: str = "Error", duration: int = 3000):
        print("i am called")
        self._show_toast(message, title, ToastPreset.ERROR, duration)

    def info(self, message: str, title: str = "Info", duration: int = 3000):
        self._show_toast(message, title, ToastPreset.INFO, duration)

    def _show_toast(self, message: str, title: str, preset: ToastPreset, duration: int):
        """
        Internal: shows a toast safely from any thread using QTimer.singleShot.
        """
        # Ensure GUI thread
        QTimer.singleShot(0, lambda: self._create_toast(message, title, preset, duration))

    def _create_toast(self, message: str, title: str, preset: ToastPreset, duration: int):
        toast = Toast(self.parent)
        toast.setDuration(duration)
        toast.setTitle("some message please read")
        toast.setText("some message")
        toast.applyPreset(preset)
        toast.show()
        toast.raise_()
        toast.activateWindow()
