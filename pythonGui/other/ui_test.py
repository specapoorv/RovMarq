import sys
import os

# Add the parent directory (pythonGui) to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QMainWindow
from frontend.gui_main_window import Ui_guiMainWindow  # Import your converted UI class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_guiMainWindow()
        self.ui.setupUi(self)  # Setup the UI on this window instance

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
