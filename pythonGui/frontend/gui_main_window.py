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

from components.BatteryProgressBar import BatteryProgressBar
from components.RoverWheelWidget import RoverWheelWidget

class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        if not guiMainWindow.objectName():
            guiMainWindow.setObjectName(u"guiMainWindow")
        guiMainWindow.resize(938, 640)
        guiMainWindow.setStyleSheet(u"background-color: rgb(24, 24, 29);")
        self.centralwidget = QWidget(guiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.roverwheelwidget = RoverWheelWidget(self.centralwidget)
        self.roverwheelwidget.setObjectName(u"roverwheelwidget")
        self.roverwheelwidget.setGeometry(QRect(90, 70, 301, 421))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(500, 20, 361, 531))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CurrentRoverStatus = QGroupBox(self.layoutWidget)
        self.CurrentRoverStatus.setObjectName(u"CurrentRoverStatus")
        self.CurrentRoverStatus.setStyleSheet(u"QGroupBox {\n"
"	border: 2px solid rgb(227, 30, 3);\n"
"	border-radius: 10px;\n"
"	margin-top: 0.5ex;\n"
"	font-size: 24px;\n"
"	font-weight: bold;\n"
"	font: 700 20pt \"Uroob\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: rgb(227, 30, 3);\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top-left;\n"
"	padding: 0 10px;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.CurrentRoverStatus)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.modeNameLabel = QLabel(self.CurrentRoverStatus)
        self.modeNameLabel.setObjectName(u"modeNameLabel")
        self.modeNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.modeNameLabel, 0, 0, 1, 1)

        self.currentSettingNameLabel = QLabel(self.CurrentRoverStatus)
        self.currentSettingNameLabel.setObjectName(u"currentSettingNameLabel")
        self.currentSettingNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.currentSettingNameLabel, 2, 0, 1, 1)

        self.label = QLabel(self.CurrentRoverStatus)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.CurrentRoverStatus)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.CurrentRoverStatus)

        self.sensorDataPanel = QGroupBox(self.layoutWidget)
        self.sensorDataPanel.setObjectName(u"sensorDataPanel")
        self.sensorDataPanel.setStyleSheet(u"QGroupBox {\n"
"	border: 2px solid rgb(227, 30, 3);\n"
"	border-radius: 10px;\n"
"	margin-top: 0.5ex;\n"
"	font-size: 24px;\n"
"	font-weight: bold;\n"
"	font: 700 20pt \"Uroob\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: rgb(227, 30, 3);\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top-left;\n"
"	padding: 0 10px;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout = QGridLayout(self.sensorDataPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.yawNameLabel = QLabel(self.sensorDataPanel)
        self.yawNameLabel.setObjectName(u"yawNameLabel")
        self.yawNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.yawNameLabel, 1, 0, 1, 1)

        self.LatencyNameLabel = QLabel(self.sensorDataPanel)
        self.LatencyNameLabel.setObjectName(u"LatencyNameLabel")
        self.LatencyNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.LatencyNameLabel, 2, 0, 1, 1)

        self.GPSValuesLabel = QLabel(self.sensorDataPanel)
        self.GPSValuesLabel.setObjectName(u"GPSValuesLabel")
        self.GPSValuesLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.GPSValuesLabel, 0, 1, 1, 1)

        self.GPSNameLabel = QLabel(self.sensorDataPanel)
        self.GPSNameLabel.setObjectName(u"GPSNameLabel")
        self.GPSNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.GPSNameLabel, 0, 0, 1, 1)

        self.batteryProgressBar = BatteryProgressBar(self.sensorDataPanel)
        self.batteryProgressBar.setObjectName(u"batteryProgressBar")
        self.batteryProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"	border-color: rgb(119, 118, 123);\n"
"    text-align: center;\n"
"    background-color: rgb(26, 28, 32);	\n"
"	font: 600 12pt \"FreeMono\";\n"
"	/*color: rgb(119, 118, 123);*/\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(250, 118, 23);\n"
"    width: 20px;\n"
"}\n"
"")
        self.batteryProgressBar.setValue(24)

        self.gridLayout.addWidget(self.batteryProgressBar, 3, 1, 1, 1)

        self.batteryNameLabel = QLabel(self.sensorDataPanel)
        self.batteryNameLabel.setObjectName(u"batteryNameLabel")
        self.batteryNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.batteryNameLabel, 3, 0, 1, 1)

        self.LatencyValueLabel = QLabel(self.sensorDataPanel)
        self.LatencyValueLabel.setObjectName(u"LatencyValueLabel")
        self.LatencyValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.LatencyValueLabel, 2, 1, 1, 1)

        self.YawValueLabel = QLabel(self.sensorDataPanel)
        self.YawValueLabel.setObjectName(u"YawValueLabel")
        self.YawValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.YawValueLabel, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.sensorDataPanel)

        self.canGroupBox = QGroupBox(self.layoutWidget)
        self.canGroupBox.setObjectName(u"canGroupBox")
        self.canGroupBox.setStyleSheet(u"QGroupBox {\n"
"	border: 2px solid rgb(227, 30, 3);\n"
"	border-radius: 10px;\n"
"	margin-top: 0.5ex;\n"
"	font-size: 24px;\n"
"	font-weight: bold;\n"
"	font: 700 20pt \"Uroob\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: rgb(227, 30, 3);\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top-left;\n"
"	padding: 0 10px;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.canGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.canStatusNameLabel = QLabel(self.canGroupBox)
        self.canStatusNameLabel.setObjectName(u"canStatusNameLabel")
        self.canStatusNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_2.addWidget(self.canStatusNameLabel, 0, 0, 1, 1)

        self.canSetButton = QPushButton(self.canGroupBox)
        self.canSetButton.setObjectName(u"canSetButton")
        self.canSetButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(33, 35, 39);\n"
"    color: rgb(119, 118, 123);\n"
"    font: bold 14px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	font: 700 14pt \"FreeMono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(119, 118, 123);\n"
"	color: rgb(244, 37, 14);\n"
"    border-style: inset;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.canSetButton, 1, 0, 1, 1)

        self.canResetButton = QPushButton(self.canGroupBox)
        self.canResetButton.setObjectName(u"canResetButton")
        self.canResetButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(33, 35, 39);\n"
"    color: rgb(119, 118, 123);\n"
"    font: bold 14px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	font: 700 14pt \"FreeMono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(119, 118, 123);\n"
"	color: rgb(244, 37, 14);\n"
"    border-style: inset;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.canResetButton, 1, 1, 1, 1)

        self.canStatusValueLabel = QLabel(self.canGroupBox)
        self.canStatusValueLabel.setObjectName(u"canStatusValueLabel")
        self.canStatusValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_2.addWidget(self.canStatusValueLabel, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.canGroupBox)

        self.KillSwitchButton = QPushButton(self.layoutWidget)
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
        self.modeNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Mode", None))
        self.currentSettingNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Config", None))
        self.label.setText(QCoreApplication.translate("guiMainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("guiMainWindow", u"Drive", None))
        self.sensorDataPanel.setTitle(QCoreApplication.translate("guiMainWindow", u"Sensor Data", None))
        self.yawNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Yaw", None))
        self.LatencyNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Latency", None))
        self.GPSValuesLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.GPSNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"GPS Coords", None))
        self.batteryNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"SOC", None))
        self.LatencyValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0 ms", None))
        self.YawValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0 deg", None))
        self.canGroupBox.setTitle(QCoreApplication.translate("guiMainWindow", u"CAN", None))
        self.canStatusNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"CAN Status:", None))
        self.canSetButton.setText(QCoreApplication.translate("guiMainWindow", u"SET", None))
        self.canResetButton.setText(QCoreApplication.translate("guiMainWindow", u"RESET", None))
        self.canStatusValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"UP", None))
        self.KillSwitchButton.setText(QCoreApplication.translate("guiMainWindow", u"Kill", None))
    # retranslateUi

