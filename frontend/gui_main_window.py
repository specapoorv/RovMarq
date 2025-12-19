# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiMain.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from components.BatteryProgressBar import BatteryProgressBar
from components.NetMapWidget import NetMapWidget
from components.RoverWheelWidget import RoverWheelWidget

class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        if not guiMainWindow.objectName():
            guiMainWindow.setObjectName(u"guiMainWindow")
        guiMainWindow.resize(1045, 953)
        guiMainWindow.setStyleSheet(u"background-color: rgb(24, 24, 29);")
        self.centralwidget = QWidget(guiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.roverwheelwidget = RoverWheelWidget(self.centralwidget)
        self.roverwheelwidget.setObjectName(u"roverwheelwidget")
        self.roverwheelwidget.setGeometry(QRect(90, 70, 301, 421))
        self.FrontLeftEncoderText = QLabel(self.roverwheelwidget)
        self.FrontLeftEncoderText.setObjectName(u"FrontLeftEncoderText")
        self.FrontLeftEncoderText.setGeometry(QRect(50, 40, 67, 17))
        self.FrontLeftEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;\n"
"")
        self.BackLeftEncoderText = QLabel(self.roverwheelwidget)
        self.BackLeftEncoderText.setObjectName(u"BackLeftEncoderText")
        self.BackLeftEncoderText.setGeometry(QRect(50, 340, 67, 17))
        self.BackLeftEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(480, 20, 321, 511))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CurrentRoverStatus = QGroupBox(self.layoutWidget)
        self.CurrentRoverStatus.setObjectName(u"CurrentRoverStatus")
        self.CurrentRoverStatus.setMaximumSize(QSize(160000, 150))
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
        self.VelocityNameLabel = QLabel(self.CurrentRoverStatus)
        self.VelocityNameLabel.setObjectName(u"VelocityNameLabel")
        self.VelocityNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.VelocityNameLabel, 1, 0, 1, 1)

        self.CurrentSettingNameLabel = QLabel(self.CurrentRoverStatus)
        self.CurrentSettingNameLabel.setObjectName(u"CurrentSettingNameLabel")
        self.CurrentSettingNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.CurrentSettingNameLabel, 3, 0, 1, 1)

        self.ModeValueLabel = QLabel(self.CurrentRoverStatus)
        self.ModeValueLabel.setObjectName(u"ModeValueLabel")
        self.ModeValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ModeValueLabel, 0, 1, 1, 1)

        self.ConfigValueLabel = QLabel(self.CurrentRoverStatus)
        self.ConfigValueLabel.setObjectName(u"ConfigValueLabel")
        self.ConfigValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ConfigValueLabel, 3, 1, 1, 1)

        self.ModeNameLabel = QLabel(self.CurrentRoverStatus)
        self.ModeNameLabel.setObjectName(u"ModeNameLabel")
        self.ModeNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ModeNameLabel, 0, 0, 1, 1)

        self.VelocityValueLabel = QLabel(self.CurrentRoverStatus)
        self.VelocityValueLabel.setObjectName(u"VelocityValueLabel")
        self.VelocityValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.VelocityValueLabel, 1, 1, 1, 1)

        self.OmegaNameLabel = QLabel(self.CurrentRoverStatus)
        self.OmegaNameLabel.setObjectName(u"OmegaNameLabel")
        self.OmegaNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OmegaNameLabel, 2, 0, 1, 1)

        self.OmegaValueLabel = QLabel(self.CurrentRoverStatus)
        self.OmegaValueLabel.setObjectName(u"OmegaValueLabel")
        self.OmegaValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OmegaValueLabel, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.CurrentRoverStatus)

        self.sensorDataPanel = QGroupBox(self.layoutWidget)
        self.sensorDataPanel.setObjectName(u"sensorDataPanel")
        self.sensorDataPanel.setMaximumSize(QSize(160000, 100))
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
        self.OdomValueLabel = QLabel(self.sensorDataPanel)
        self.OdomValueLabel.setObjectName(u"OdomValueLabel")
        self.OdomValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 14pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.OdomValueLabel, 2, 1, 1, 1)

        self.GPSValuesLabel = QLabel(self.sensorDataPanel)
        self.GPSValuesLabel.setObjectName(u"GPSValuesLabel")
        self.GPSValuesLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 14pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.GPSValuesLabel, 1, 1, 1, 1)

        self.BatteryNameLabel = QLabel(self.sensorDataPanel)
        self.BatteryNameLabel.setObjectName(u"BatteryNameLabel")
        self.BatteryNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.BatteryNameLabel, 3, 0, 1, 1)

        self.OdomNameLabel = QLabel(self.sensorDataPanel)
        self.OdomNameLabel.setObjectName(u"OdomNameLabel")
        self.OdomNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.OdomNameLabel, 2, 0, 1, 1)

        self.BatteryProgressBar = BatteryProgressBar(self.sensorDataPanel)
        self.BatteryProgressBar.setObjectName(u"BatteryProgressBar")
        self.BatteryProgressBar.setStyleSheet(u"QProgressBar {\n"
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
        self.BatteryProgressBar.setValue(24)

        self.gridLayout.addWidget(self.BatteryProgressBar, 3, 1, 1, 1)

        self.GPSNameLabel = QLabel(self.sensorDataPanel)
        self.GPSNameLabel.setObjectName(u"GPSNameLabel")
        self.GPSNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout.addWidget(self.GPSNameLabel, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.sensorDataPanel)

        self.NetMapWidgetWidget = NetMapWidget(self.layoutWidget)
        self.NetMapWidgetWidget.setObjectName(u"NetMapWidgetWidget")
        self.NetMapWidgetWidget.setStyleSheet(u"NetMapWidget {\n"
"    background-color: #1a1a1a;\n"
"    border: 2px solid #cc0000;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"NetMapWidget QFrame#headerFrame {\n"
"    background-color: rgb(227, 30, 3);\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"NetMapWidget QLabel#headerLabel {\n"
"    color: white;\n"
"	font: 1000 18pt \"Uroob\";\n"
"    font-size: 18pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"}\n"
"\n"
"NetMapWidget QFrame#deviceRow {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"NetMapWidget QLabel#deviceName {\n"
"	color: rgb(119, 118, 123);\n"
"	font: 1000 12pt \"FreeMono\";\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"NetMapWidget QLabel#deviceIP {\n"
"	color: rgb(119, 118, 123);\n"
"	font: 200 12pt \"FreeMono\";\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.NetMapWidgetWidget)

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

        self.FrontRightEncoderText = QLabel(self.centralwidget)
        self.FrontRightEncoderText.setObjectName(u"FrontRightEncoderText")
        self.FrontRightEncoderText.setGeometry(QRect(380, 110, 67, 17))
        self.FrontRightEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
        self.BackRightEncoderText = QLabel(self.centralwidget)
        self.BackRightEncoderText.setObjectName(u"BackRightEncoderText")
        self.BackRightEncoderText.setGeometry(QRect(380, 410, 67, 17))
        self.BackRightEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(80, 540, 721, 381))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        guiMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(guiMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        guiMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(guiMainWindow)

        QMetaObject.connectSlotsByName(guiMainWindow)
    # setupUi

    def retranslateUi(self, guiMainWindow):
        guiMainWindow.setWindowTitle(QCoreApplication.translate("guiMainWindow", u"MainWindow", None))
        self.FrontLeftEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.BackLeftEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.CurrentRoverStatus.setTitle(QCoreApplication.translate("guiMainWindow", u"Rover Status", None))
        self.VelocityNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Velocity", None))
        self.CurrentSettingNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Config", None))
        self.ModeValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.ConfigValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"Drive", None))
        self.ModeNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Mode", None))
        self.VelocityValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.OmegaNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Omega", None))
        self.OmegaValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.sensorDataPanel.setTitle(QCoreApplication.translate("guiMainWindow", u"Sensor Data", None))
        self.OdomValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.GPSValuesLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.BatteryNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"SOC", None))
        self.OdomNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Odom", None))
        self.GPSNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"GPS", None))
        self.KillSwitchButton.setText(QCoreApplication.translate("guiMainWindow", u"Kill", None))
        self.FrontRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.BackRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
    # retranslateUi

