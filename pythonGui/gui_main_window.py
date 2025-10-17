# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiMain.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from components.RoverWheelWidget import RoverWheelWidget

class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        if not guiMainWindow.objectName():
            guiMainWindow.setObjectName(u"guiMainWindow")
        guiMainWindow.resize(802, 600)
        self.centralwidget = QWidget(guiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = RoverWheelWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 70, 301, 421))
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(500, 20, 271, 531))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CurrentRoverStatus = QGroupBox(self.widget1)
        self.CurrentRoverStatus.setObjectName(u"CurrentRoverStatus")
        self.gridLayout_3 = QGridLayout(self.CurrentRoverStatus)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.CurrentRoverStatus)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 2, 1, 1)

        self.currentSettingNameLabel = QLabel(self.CurrentRoverStatus)
        self.currentSettingNameLabel.setObjectName(u"currentSettingNameLabel")

        self.gridLayout_3.addWidget(self.currentSettingNameLabel, 2, 0, 1, 2)

        self.modeNameLabel = QLabel(self.CurrentRoverStatus)
        self.modeNameLabel.setObjectName(u"modeNameLabel")

        self.gridLayout_3.addWidget(self.modeNameLabel, 0, 0, 1, 1)

        self.label = QLabel(self.CurrentRoverStatus)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.CurrentRoverStatus)

        self.sensorDataPanel = QGroupBox(self.widget1)
        self.sensorDataPanel.setObjectName(u"sensorDataPanel")
        self.gridLayout = QGridLayout(self.sensorDataPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.batteryNameLabel = QLabel(self.sensorDataPanel)
        self.batteryNameLabel.setObjectName(u"batteryNameLabel")

        self.gridLayout.addWidget(self.batteryNameLabel, 4, 0, 1, 1)

        self.batteryValueLabel = QLabel(self.sensorDataPanel)
        self.batteryValueLabel.setObjectName(u"batteryValueLabel")

        self.gridLayout.addWidget(self.batteryValueLabel, 4, 1, 1, 1)

        self.LatencyNameLabel = QLabel(self.sensorDataPanel)
        self.LatencyNameLabel.setObjectName(u"LatencyNameLabel")

        self.gridLayout.addWidget(self.LatencyNameLabel, 3, 0, 1, 1)

        self.LatencyValueLabel = QLabel(self.sensorDataPanel)
        self.LatencyValueLabel.setObjectName(u"LatencyValueLabel")

        self.gridLayout.addWidget(self.LatencyValueLabel, 3, 1, 1, 1)

        self.GPSNameLabel = QLabel(self.sensorDataPanel)
        self.GPSNameLabel.setObjectName(u"GPSNameLabel")

        self.gridLayout.addWidget(self.GPSNameLabel, 0, 0, 1, 1)

        self.LinearXNameLabel = QLabel(self.sensorDataPanel)
        self.LinearXNameLabel.setObjectName(u"LinearXNameLabel")

        self.gridLayout.addWidget(self.LinearXNameLabel, 2, 0, 1, 1)

        self.YawValueLabel = QLabel(self.sensorDataPanel)
        self.YawValueLabel.setObjectName(u"YawValueLabel")

        self.gridLayout.addWidget(self.YawValueLabel, 1, 1, 1, 1)

        self.yawNameLabel = QLabel(self.sensorDataPanel)
        self.yawNameLabel.setObjectName(u"yawNameLabel")

        self.gridLayout.addWidget(self.yawNameLabel, 1, 0, 1, 1)

        self.LinearXValueLabel = QLabel(self.sensorDataPanel)
        self.LinearXValueLabel.setObjectName(u"LinearXValueLabel")

        self.gridLayout.addWidget(self.LinearXValueLabel, 2, 1, 1, 1)

        self.GPSValuesLabel = QLabel(self.sensorDataPanel)
        self.GPSValuesLabel.setObjectName(u"GPSValuesLabel")

        self.gridLayout.addWidget(self.GPSValuesLabel, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.sensorDataPanel)

        self.canGroupBox = QGroupBox(self.widget1)
        self.canGroupBox.setObjectName(u"canGroupBox")
        self.gridLayout_2 = QGridLayout(self.canGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.canStatusNameLabel = QLabel(self.canGroupBox)
        self.canStatusNameLabel.setObjectName(u"canStatusNameLabel")

        self.gridLayout_2.addWidget(self.canStatusNameLabel, 0, 0, 1, 1)

        self.canSetButton = QPushButton(self.canGroupBox)
        self.canSetButton.setObjectName(u"canSetButton")

        self.gridLayout_2.addWidget(self.canSetButton, 1, 0, 1, 1)

        self.canResetButton = QPushButton(self.canGroupBox)
        self.canResetButton.setObjectName(u"canResetButton")

        self.gridLayout_2.addWidget(self.canResetButton, 1, 1, 1, 1)

        self.canStatusValueLabel = QLabel(self.canGroupBox)
        self.canStatusValueLabel.setObjectName(u"canStatusValueLabel")

        self.gridLayout_2.addWidget(self.canStatusValueLabel, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.canGroupBox)

        self.KillSwitchButton = QPushButton(self.widget1)
        self.KillSwitchButton.setObjectName(u"KillSwitchButton")
        self.KillSwitchButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(246, 11, 11);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.KillSwitchButton)

        guiMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(guiMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        guiMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(guiMainWindow)

        QMetaObject.connectSlotsByName(guiMainWindow)
    # setupUi

    def retranslateUi(self, guiMainWindow):
        guiMainWindow.setWindowTitle(QCoreApplication.translate("guiMainWindow", u"MainWindow", None))
        self.CurrentRoverStatus.setTitle(QCoreApplication.translate("guiMainWindow", u"Rover Status", None))
        self.label_2.setText(QCoreApplication.translate("guiMainWindow", u"TextLabel", None))
        self.currentSettingNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Current Setting:", None))
        self.modeNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Mode:", None))
        self.label.setText(QCoreApplication.translate("guiMainWindow", u"TextLabel", None))
        self.sensorDataPanel.setTitle(QCoreApplication.translate("guiMainWindow", u"Sensor Data", None))
        self.batteryNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Battery:", None))
        self.batteryValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"?", None))
        self.LatencyNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Latency:", None))
        self.LatencyValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0 ms", None))
        self.GPSNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"GPS Coordinates:", None))
        self.LinearXNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Linear_x:", None))
        self.YawValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0 deg", None))
        self.yawNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Yaw:", None))
        self.LinearXValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0 m/s", None))
        self.GPSValuesLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.canGroupBox.setTitle(QCoreApplication.translate("guiMainWindow", u"CAN", None))
        self.canStatusNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"CAN Status:", None))
        self.canSetButton.setText(QCoreApplication.translate("guiMainWindow", u"CAN Set", None))
        self.canResetButton.setText(QCoreApplication.translate("guiMainWindow", u"CAN Reset", None))
        self.canStatusValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"UP", None))
        self.KillSwitchButton.setText(QCoreApplication.translate("guiMainWindow", u"Kill", None))
    # retranslateUi

