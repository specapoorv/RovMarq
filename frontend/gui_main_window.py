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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

from components.NetMapWidget import NetMapWidget
from components.RoverWheelWidget import RoverWheelWidget

class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        if not guiMainWindow.objectName():
            guiMainWindow.setObjectName(u"guiMainWindow")
        guiMainWindow.resize(1180, 883)
        guiMainWindow.setStyleSheet(u"background-color: rgb(24, 24, 29);")
        self.centralwidget = QWidget(guiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.roverwheelwidget = RoverWheelWidget(self.centralwidget)
        self.roverwheelwidget.setObjectName(u"roverwheelwidget")
        self.roverwheelwidget.setGeometry(QRect(-30, 10, 301, 421))
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
        self.FrontRightEncoderText = QLabel(self.roverwheelwidget)
        self.FrontRightEncoderText.setObjectName(u"FrontRightEncoderText")
        self.FrontRightEncoderText.setGeometry(QRect(290, 40, 67, 17))
        self.FrontRightEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(340, 0, 301, 441))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CurrentRoverStatus = QGroupBox(self.layoutWidget)
        self.CurrentRoverStatus.setObjectName(u"CurrentRoverStatus")
        self.CurrentRoverStatus.setMaximumSize(QSize(160000, 175))
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
        self.GPSNameLabel = QLabel(self.CurrentRoverStatus)
        self.GPSNameLabel.setObjectName(u"GPSNameLabel")
        self.GPSNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.GPSNameLabel, 4, 0, 1, 1)

        self.CurrentSettingNameLabel = QLabel(self.CurrentRoverStatus)
        self.CurrentSettingNameLabel.setObjectName(u"CurrentSettingNameLabel")
        self.CurrentSettingNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.CurrentSettingNameLabel, 3, 0, 1, 1)

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

        self.ConfigValueLabel = QLabel(self.CurrentRoverStatus)
        self.ConfigValueLabel.setObjectName(u"ConfigValueLabel")
        self.ConfigValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ConfigValueLabel, 3, 1, 1, 1)

        self.OdomNameLabel = QLabel(self.CurrentRoverStatus)
        self.OdomNameLabel.setObjectName(u"OdomNameLabel")
        self.OdomNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OdomNameLabel, 6, 0, 1, 1)

        self.VelocityNameLabel = QLabel(self.CurrentRoverStatus)
        self.VelocityNameLabel.setObjectName(u"VelocityNameLabel")
        self.VelocityNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.VelocityNameLabel, 1, 0, 1, 1)

        self.ModeNameLabel = QLabel(self.CurrentRoverStatus)
        self.ModeNameLabel.setObjectName(u"ModeNameLabel")
        self.ModeNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ModeNameLabel, 0, 0, 1, 1)

        self.GPSValuesLabel = QLabel(self.CurrentRoverStatus)
        self.GPSValuesLabel.setObjectName(u"GPSValuesLabel")
        self.GPSValuesLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 14pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.GPSValuesLabel, 4, 1, 1, 1)

        self.OmegaValueLabel = QLabel(self.CurrentRoverStatus)
        self.OmegaValueLabel.setObjectName(u"OmegaValueLabel")
        self.OmegaValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OmegaValueLabel, 2, 1, 1, 1)

        self.ModeValueLabel = QLabel(self.CurrentRoverStatus)
        self.ModeValueLabel.setObjectName(u"ModeValueLabel")
        self.ModeValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ModeValueLabel, 0, 1, 1, 1)

        self.OdomValueLabel = QLabel(self.CurrentRoverStatus)
        self.OdomValueLabel.setObjectName(u"OdomValueLabel")
        self.OdomValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 14pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OdomValueLabel, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.CurrentRoverStatus)

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
"	font: 1000 8pt \"FreeMono\";\n"
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

        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(20, 460, 621, 401))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.csvFile = QTableView(self.centralwidget)
        self.csvFile.setObjectName(u"csvFile")
        self.csvFile.setGeometry(QRect(650, 10, 351, 261))
        self.csvFile.setStyleSheet(u"QTableView {            \n"
"    gridline-color: transparent;        /* Grid lines between cells */\n"
"    selection-color: rgb(119, 118, 123);          /* Selected cell text */\n"
"    border: 2px solid rgb(227, 30, 3);          /* Border around entire table */\n"
"	font: 1000 10pt \"FreeMono\";\n"
"   border-radius: 10px;\n"
"}\n"
"\n"
"QTableView:item {\n"
"	color: rgb(227, 30, 3); \n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: rgb(227, 30, 3);\n"
"    color: rgb(119, 118, 123);                      \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(119, 118, 123);        /* Background color */\n"
"   	color: rgb(24, 24, 29);                   /* Text color */\n"
"	font: 1200 12pt \"FreeMono\";\n"
"    text-align: center;               /* Text alignment */\n"
"}\n"
"\n"
"QTableView QLineEdit {\n"
"    background-color: rgb(227, 30, 3);\n"
"    color: rgb(24, 24, 29);\n"
"    border: 2px solid #555;\n"
"    selection-background-color: #ff6b6b;\n"
"}\n"
"")
        self.colorGroupBox = QGroupBox(self.centralwidget)
        self.colorGroupBox.setObjectName(u"colorGroupBox")
        self.colorGroupBox.setGeometry(QRect(1020, 0, 131, 271))
        self.colorGroupBox.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout = QGridLayout(self.colorGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.blueButton = QPushButton(self.colorGroupBox)
        self.blueButton.setObjectName(u"blueButton")
        self.blueButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(8, 46, 244);\n"
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

        self.gridLayout.addWidget(self.blueButton, 1, 1, 1, 1)

        self.yellowButton = QPushButton(self.colorGroupBox)
        self.yellowButton.setObjectName(u"yellowButton")
        self.yellowButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 243, 14);\n"
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

        self.gridLayout.addWidget(self.yellowButton, 1, 0, 1, 1)

        self.greenButton = QPushButton(self.colorGroupBox)
        self.greenButton.setObjectName(u"greenButton")
        self.greenButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(31, 249, 12);\n"
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

        self.gridLayout.addWidget(self.greenButton, 0, 1, 1, 1)

        self.redButton = QPushButton(self.colorGroupBox)
        self.redButton.setObjectName(u"redButton")
        self.redButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.redButton, 0, 0, 1, 1)

        self.orangeButton = QPushButton(self.colorGroupBox)
        self.orangeButton.setObjectName(u"orangeButton")
        self.orangeButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(251, 130, 5);\n"
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

        self.gridLayout.addWidget(self.orangeButton, 2, 0, 1, 1)

        self.purpleButton = QPushButton(self.colorGroupBox)
        self.purpleButton.setObjectName(u"purpleButton")
        self.purpleButton.setStyleSheet(u"QPushButton {\n"
"    background-color:rgb(198, 19, 227);\n"
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

        self.gridLayout.addWidget(self.purpleButton, 2, 1, 1, 1)

        self.BackRightEncoderText = QLabel(self.centralwidget)
        self.BackRightEncoderText.setObjectName(u"BackRightEncoderText")
        self.BackRightEncoderText.setGeometry(QRect(260, 350, 67, 17))
        self.BackRightEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
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
        self.FrontRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.CurrentRoverStatus.setTitle(QCoreApplication.translate("guiMainWindow", u"Rover Info", None))
        self.GPSNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"GPS", None))
        self.CurrentSettingNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Config", None))
        self.VelocityValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.OmegaNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Omega", None))
        self.ConfigValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"DRIVE", None))
        self.OdomNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Odom", None))
        self.VelocityNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Velocity", None))
        self.ModeNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Mode", None))
        self.GPSValuesLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.OmegaValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.ModeValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.OdomValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.KillSwitchButton.setText(QCoreApplication.translate("guiMainWindow", u"Kill", None))
        self.colorGroupBox.setTitle(QCoreApplication.translate("guiMainWindow", u"Color", None))
        self.blueButton.setText("")
        self.yellowButton.setText("")
        self.greenButton.setText("")
        self.redButton.setText("")
        self.orangeButton.setText("")
        self.purpleButton.setText("")
        self.BackRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
    # retranslateUi

