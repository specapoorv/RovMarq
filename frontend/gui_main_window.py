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
    QSlider, QStatusBar, QTableView, QWidget)

from components.NetMapWidget import NetMapWidget
from components.RoverWheelWidget import RoverWheelWidget

class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        if not guiMainWindow.objectName():
            guiMainWindow.setObjectName(u"guiMainWindow")
        guiMainWindow.resize(1325, 913)
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
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(20, 520, 621, 341))
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
        self.colorGroupBox.setGeometry(QRect(1010, 10, 161, 261))
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

        self.gridLayout.addWidget(self.orangeButton, 1, 0, 1, 1)

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

        self.gridLayout.addWidget(self.purpleButton, 2, 0, 1, 1)

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

        self.gridLayout.addWidget(self.yellowButton, 2, 1, 1, 1)

        self.BackRightEncoderText = QLabel(self.centralwidget)
        self.BackRightEncoderText.setObjectName(u"BackRightEncoderText")
        self.BackRightEncoderText.setGeometry(QRect(260, 350, 67, 17))
        self.BackRightEncoderText.setStyleSheet(u"color: rgb(227, 30, 3);\n"
"font: 1000 14pt \"FreeMono\";\n"
"/* qproperty-alignment: AlignCenter; */\n"
"background-color: transparent;")
        self.cameraPanel = QGroupBox(self.centralwidget)
        self.cameraPanel.setObjectName(u"cameraPanel")
        self.cameraPanel.setGeometry(QRect(660, 280, 511, 271))
        self.cameraPanel.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout_2 = QGridLayout(self.cameraPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.brightnessSlider1 = QSlider(self.cameraPanel)
        self.brightnessSlider1.setObjectName(u"brightnessSlider1")
        self.brightnessSlider1.setMaximumSize(QSize(100, 16777215))
        self.brightnessSlider1.setStyleSheet(u"\n"
"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"background: rgb(227, 30, 3);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"background: #575757;\n"
"border-radius: 4px;\n"
"}")
        self.brightnessSlider1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.brightnessSlider1, 1, 1, 1, 1)

        self.zoomLabel2 = QLabel(self.cameraPanel)
        self.zoomLabel2.setObjectName(u"zoomLabel2")
        self.zoomLabel2.setMinimumSize(QSize(0, 25))
        self.zoomLabel2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.zoomLabel2, 6, 0, 1, 1)

        self.brightnessLabel1 = QLabel(self.cameraPanel)
        self.brightnessLabel1.setObjectName(u"brightnessLabel1")
        self.brightnessLabel1.setMinimumSize(QSize(0, 25))
        self.brightnessLabel1.setMaximumSize(QSize(16777215, 35))
        self.brightnessLabel1.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.brightnessLabel1, 1, 0, 1, 1)

        self.contrastSlider2 = QSlider(self.cameraPanel)
        self.contrastSlider2.setObjectName(u"contrastSlider2")
        self.contrastSlider2.setMaximumSize(QSize(100, 16777215))
        self.contrastSlider2.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.contrastSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.contrastSlider2, 7, 1, 1, 1)

        self.zoomLabel1 = QLabel(self.cameraPanel)
        self.zoomLabel1.setObjectName(u"zoomLabel1")
        self.zoomLabel1.setMinimumSize(QSize(0, 25))
        self.zoomLabel1.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.zoomLabel1, 2, 0, 1, 1)

        self.brightnessSlider2 = QSlider(self.cameraPanel)
        self.brightnessSlider2.setObjectName(u"brightnessSlider2")
        self.brightnessSlider2.setMaximumSize(QSize(100, 16777215))
        self.brightnessSlider2.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.brightnessSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.brightnessSlider2, 5, 1, 1, 1)

        self.contrastLabel1 = QLabel(self.cameraPanel)
        self.contrastLabel1.setObjectName(u"contrastLabel1")
        self.contrastLabel1.setMinimumSize(QSize(0, 25))
        self.contrastLabel1.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.contrastLabel1, 3, 0, 1, 1)

        self.zoomSlider2 = QSlider(self.cameraPanel)
        self.zoomSlider2.setObjectName(u"zoomSlider2")
        self.zoomSlider2.setMaximumSize(QSize(100, 16777215))
        self.zoomSlider2.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.zoomSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.zoomSlider2, 6, 1, 1, 1)

        self.cameraTitleLabel2 = QLabel(self.cameraPanel)
        self.cameraTitleLabel2.setObjectName(u"cameraTitleLabel2")
        self.cameraTitleLabel2.setMinimumSize(QSize(0, 30))
        self.cameraTitleLabel2.setMaximumSize(QSize(16777215, 35))
        self.cameraTitleLabel2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft\n"
";")

        self.gridLayout_2.addWidget(self.cameraTitleLabel2, 4, 0, 1, 1)

        self.zoomSlider1 = QSlider(self.cameraPanel)
        self.zoomSlider1.setObjectName(u"zoomSlider1")
        self.zoomSlider1.setMaximumSize(QSize(100, 16777215))
        self.zoomSlider1.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.zoomSlider1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.zoomSlider1, 2, 1, 1, 1)

        self.brightnessLabel3 = QLabel(self.cameraPanel)
        self.brightnessLabel3.setObjectName(u"brightnessLabel3")
        self.brightnessLabel3.setMinimumSize(QSize(0, 25))
        self.brightnessLabel3.setMaximumSize(QSize(16777215, 30))
        self.brightnessLabel3.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.brightnessLabel3, 1, 2, 1, 1)

        self.cameraTitleLabel1 = QLabel(self.cameraPanel)
        self.cameraTitleLabel1.setObjectName(u"cameraTitleLabel1")
        self.cameraTitleLabel1.setMinimumSize(QSize(0, 30))
        self.cameraTitleLabel1.setMaximumSize(QSize(16777215, 35))
        self.cameraTitleLabel1.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft\n"
";")

        self.gridLayout_2.addWidget(self.cameraTitleLabel1, 0, 0, 1, 1)

        self.contrastLabel3 = QLabel(self.cameraPanel)
        self.contrastLabel3.setObjectName(u"contrastLabel3")
        self.contrastLabel3.setMinimumSize(QSize(0, 25))
        self.contrastLabel3.setMaximumSize(QSize(16777215, 30))
        self.contrastLabel3.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.contrastLabel3, 3, 2, 1, 1)

        self.contrastSlider1 = QSlider(self.cameraPanel)
        self.contrastSlider1.setObjectName(u"contrastSlider1")
        self.contrastSlider1.setMaximumSize(QSize(100, 16777215))
        self.contrastSlider1.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.contrastSlider1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.contrastSlider1, 3, 1, 1, 1)

        self.cameraTitleLabel3 = QLabel(self.cameraPanel)
        self.cameraTitleLabel3.setObjectName(u"cameraTitleLabel3")
        self.cameraTitleLabel3.setMinimumSize(QSize(0, 30))
        self.cameraTitleLabel3.setMaximumSize(QSize(16777215, 35))
        self.cameraTitleLabel3.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft\n"
";")

        self.gridLayout_2.addWidget(self.cameraTitleLabel3, 0, 2, 1, 1)

        self.zoomLabel3 = QLabel(self.cameraPanel)
        self.zoomLabel3.setObjectName(u"zoomLabel3")
        self.zoomLabel3.setMinimumSize(QSize(0, 25))
        self.zoomLabel3.setMaximumSize(QSize(16777215, 30))
        self.zoomLabel3.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.zoomLabel3, 2, 2, 1, 1)

        self.brightnessLabel2 = QLabel(self.cameraPanel)
        self.brightnessLabel2.setObjectName(u"brightnessLabel2")
        self.brightnessLabel2.setMinimumSize(QSize(0, 25))
        self.brightnessLabel2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.brightnessLabel2, 5, 0, 1, 1)

        self.contrastLabel2 = QLabel(self.cameraPanel)
        self.contrastLabel2.setObjectName(u"contrastLabel2")
        self.contrastLabel2.setMinimumSize(QSize(0, 25))
        self.contrastLabel2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.contrastLabel2, 7, 0, 1, 1)

        self.brightnessSlider3 = QSlider(self.cameraPanel)
        self.brightnessSlider3.setObjectName(u"brightnessSlider3")
        self.brightnessSlider3.setMaximumSize(QSize(100, 16777215))
        self.brightnessSlider3.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.brightnessSlider3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.brightnessSlider3, 1, 3, 1, 1)

        self.zoomSlider3 = QSlider(self.cameraPanel)
        self.zoomSlider3.setObjectName(u"zoomSlider3")
        self.zoomSlider3.setMaximumSize(QSize(100, 16777215))
        self.zoomSlider3.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.zoomSlider3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.zoomSlider3, 2, 3, 1, 1)

        self.contrastSlider3 = QSlider(self.cameraPanel)
        self.contrastSlider3.setObjectName(u"contrastSlider3")
        self.contrastSlider3.setMaximumSize(QSize(100, 16777215))
        self.contrastSlider3.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.contrastSlider3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.contrastSlider3, 3, 3, 1, 1)

        self.cameraTitleLabel4 = QLabel(self.cameraPanel)
        self.cameraTitleLabel4.setObjectName(u"cameraTitleLabel4")
        self.cameraTitleLabel4.setMinimumSize(QSize(0, 30))
        self.cameraTitleLabel4.setMaximumSize(QSize(16777215, 35))
        self.cameraTitleLabel4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft\n"
";")

        self.gridLayout_2.addWidget(self.cameraTitleLabel4, 4, 2, 1, 1)

        self.brightnessLabel4 = QLabel(self.cameraPanel)
        self.brightnessLabel4.setObjectName(u"brightnessLabel4")
        self.brightnessLabel4.setMinimumSize(QSize(0, 25))
        self.brightnessLabel4.setMaximumSize(QSize(16777215, 30))
        self.brightnessLabel4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.brightnessLabel4, 5, 2, 1, 1)

        self.zoomLabel4 = QLabel(self.cameraPanel)
        self.zoomLabel4.setObjectName(u"zoomLabel4")
        self.zoomLabel4.setMinimumSize(QSize(0, 25))
        self.zoomLabel4.setMaximumSize(QSize(16777215, 30))
        self.zoomLabel4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.zoomLabel4, 6, 2, 1, 1)

        self.contrastLabel4 = QLabel(self.cameraPanel)
        self.contrastLabel4.setObjectName(u"contrastLabel4")
        self.contrastLabel4.setMinimumSize(QSize(0, 25))
        self.contrastLabel4.setMaximumSize(QSize(16777215, 30))
        self.contrastLabel4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 500 15pt \"FreeMono\";\n"
"qproperty-alignment: AlignLeft;")

        self.gridLayout_2.addWidget(self.contrastLabel4, 7, 2, 1, 1)

        self.brightnessSlider4 = QSlider(self.cameraPanel)
        self.brightnessSlider4.setObjectName(u"brightnessSlider4")
        self.brightnessSlider4.setMaximumSize(QSize(100, 16777215))
        self.brightnessSlider4.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.brightnessSlider4.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.brightnessSlider4, 5, 3, 1, 1)

        self.zoomSlider4 = QSlider(self.cameraPanel)
        self.zoomSlider4.setObjectName(u"zoomSlider4")
        self.zoomSlider4.setMaximumSize(QSize(100, 16777215))
        self.zoomSlider4.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.zoomSlider4.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.zoomSlider4, 6, 3, 1, 1)

        self.contrastSlider4 = QSlider(self.cameraPanel)
        self.contrastSlider4.setObjectName(u"contrastSlider4")
        self.contrastSlider4.setMaximumSize(QSize(100, 16777215))
        self.contrastSlider4.setStyleSheet(u"/* The filled part (left of handle) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(227, 30, 3); /* Darker green fill */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The unfilled part (right of handle) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #575757;\n"
"    border-radius: 4px;\n"
"}")
        self.contrastSlider4.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.contrastSlider4, 7, 3, 1, 1)

        self.CurrentRoverStatus = QGroupBox(self.centralwidget)
        self.CurrentRoverStatus.setObjectName(u"CurrentRoverStatus")
        self.CurrentRoverStatus.setGeometry(QRect(340, 0, 291, 250))
        self.CurrentRoverStatus.setMinimumSize(QSize(0, 200))
        self.CurrentRoverStatus.setMaximumSize(QSize(160000, 250))
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

        self.frequencyValueLabel = QLabel(self.CurrentRoverStatus)
        self.frequencyValueLabel.setObjectName(u"frequencyValueLabel")
        self.frequencyValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.frequencyValueLabel, 7, 1, 1, 1)

        self.GPSNameLabel = QLabel(self.CurrentRoverStatus)
        self.GPSNameLabel.setObjectName(u"GPSNameLabel")
        self.GPSNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.GPSNameLabel, 4, 0, 1, 1)

        self.GPSValuesLabel = QLabel(self.CurrentRoverStatus)
        self.GPSValuesLabel.setObjectName(u"GPSValuesLabel")
        self.GPSValuesLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 14pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.GPSValuesLabel, 4, 1, 1, 1)

        self.ModeNameLabel = QLabel(self.CurrentRoverStatus)
        self.ModeNameLabel.setObjectName(u"ModeNameLabel")
        self.ModeNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.ModeNameLabel, 0, 0, 1, 1)

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

        self.OmegaValueLabel = QLabel(self.CurrentRoverStatus)
        self.OmegaValueLabel.setObjectName(u"OmegaValueLabel")
        self.OmegaValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OmegaValueLabel, 2, 1, 1, 1)

        self.OdomNameLabel = QLabel(self.CurrentRoverStatus)
        self.OdomNameLabel.setObjectName(u"OdomNameLabel")
        self.OdomNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.OdomNameLabel, 6, 0, 1, 1)

        self.VelocityValueLabel = QLabel(self.CurrentRoverStatus)
        self.VelocityValueLabel.setObjectName(u"VelocityValueLabel")
        self.VelocityValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.VelocityValueLabel, 1, 1, 1, 1)

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

        self.frequencyNameLabel = QLabel(self.CurrentRoverStatus)
        self.frequencyNameLabel.setObjectName(u"frequencyNameLabel")
        self.frequencyNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.frequencyNameLabel, 7, 0, 1, 1)

        self.noiseValueLabel = QLabel(self.CurrentRoverStatus)
        self.noiseValueLabel.setObjectName(u"noiseValueLabel")
        self.noiseValueLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.noiseValueLabel, 8, 1, 1, 1)

        self.noiseNameLabel = QLabel(self.CurrentRoverStatus)
        self.noiseNameLabel.setObjectName(u"noiseNameLabel")
        self.noiseNameLabel.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"font: 1000 18pt \"FreeMono\";\n"
"qproperty-alignment: AlignCenter;")

        self.gridLayout_3.addWidget(self.noiseNameLabel, 8, 0, 1, 1)

        self.NetMapWidgetWidget = NetMapWidget(self.centralwidget)
        self.NetMapWidgetWidget.setObjectName(u"NetMapWidgetWidget")
        self.NetMapWidgetWidget.setGeometry(QRect(338, 250, 291, 258))
        self.NetMapWidgetWidget.setMinimumSize(QSize(250, 200))
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
"	font: 1000 10pt \"FreeMono\";\n"
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
"\n"
"QWidget {\n"
"    border: 2px solid rgb(227, 30, 3);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.KillSwitchButton = QPushButton(self.centralwidget)
        self.KillSwitchButton.setObjectName(u"KillSwitchButton")
        self.KillSwitchButton.setGeometry(QRect(310, 870, 299, 29))
        self.KillSwitchButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(241, 8, 8);\n"
"    color:  white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    border: 1px solid rgb(119, 118, 123);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(24, 24, 29);\n"
"    color: rgb(241, 8, 8);\n"
"}")
        self.autologButton = QPushButton(self.centralwidget)
        self.autologButton.setObjectName(u"autologButton")
        self.autologButton.setGeometry(QRect(20, 870, 131, 31))
        self.autologButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(227, 30, 3);\n"
"    color:  rgb(24, 24, 29);\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    border: 3px solid rgb(119, 118, 123);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color:  rgb(24, 24, 29);\n"
"    color: rgb(227, 30, 3);\n"
"\n"
"}\n"
"\n"
"")
        self.autologButton.setCheckable(True)
        self.autologButton.setChecked(False)
        self.statusbar = QStatusBar(self.centralwidget)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(160, 870, 131, 31))
        self.sendButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(8, 46, 244);\n"
"    color:  rgb(24, 24, 29);\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    border: 3px solid rgb(119, 118, 123);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color:  rgb(24, 24, 29);\n"
"    color: rgb(227, 30, 3);\n"
"\n"
"}\n"
"\n"
"")
        self.directionLabel = QLabel(self.centralwidget)
        self.directionLabel.setObjectName(u"directionLabel")
        self.directionLabel.setGeometry(QRect(100, 470, 161, 17))
        self.directionLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(227, 30, 3);\n"
"	font: 1000 18pt \"FreeMono\";\n"
"}")
        guiMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(guiMainWindow)

        QMetaObject.connectSlotsByName(guiMainWindow)
    # setupUi

    def retranslateUi(self, guiMainWindow):
        guiMainWindow.setWindowTitle(QCoreApplication.translate("guiMainWindow", u"MainWindow", None))
        self.FrontLeftEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.BackLeftEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.FrontRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.colorGroupBox.setTitle(QCoreApplication.translate("guiMainWindow", u"Color", None))
        self.greenButton.setText("")
        self.redButton.setText("")
        self.blueButton.setText("")
        self.orangeButton.setText("")
        self.purpleButton.setText("")
        self.yellowButton.setText("")
        self.BackRightEncoderText.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.cameraPanel.setTitle(QCoreApplication.translate("guiMainWindow", u"Camera Panel", None))
        self.zoomLabel2.setText(QCoreApplication.translate("guiMainWindow", u"Zoom", None))
        self.brightnessLabel1.setText(QCoreApplication.translate("guiMainWindow", u"Brightness", None))
        self.zoomLabel1.setText(QCoreApplication.translate("guiMainWindow", u"Zoom", None))
        self.contrastLabel1.setText(QCoreApplication.translate("guiMainWindow", u"Contrast", None))
        self.cameraTitleLabel2.setText(QCoreApplication.translate("guiMainWindow", u"Camera 2", None))
        self.brightnessLabel3.setText(QCoreApplication.translate("guiMainWindow", u"Brightness", None))
        self.cameraTitleLabel1.setText(QCoreApplication.translate("guiMainWindow", u"Camera 1", None))
        self.contrastLabel3.setText(QCoreApplication.translate("guiMainWindow", u"Contrast", None))
        self.cameraTitleLabel3.setText(QCoreApplication.translate("guiMainWindow", u"Camera 3", None))
        self.zoomLabel3.setText(QCoreApplication.translate("guiMainWindow", u"Zoom", None))
        self.brightnessLabel2.setText(QCoreApplication.translate("guiMainWindow", u"Brightness", None))
        self.contrastLabel2.setText(QCoreApplication.translate("guiMainWindow", u"Contrast", None))
        self.cameraTitleLabel4.setText(QCoreApplication.translate("guiMainWindow", u"Camera 4", None))
        self.brightnessLabel4.setText(QCoreApplication.translate("guiMainWindow", u"Brightness", None))
        self.zoomLabel4.setText(QCoreApplication.translate("guiMainWindow", u"Zoom", None))
        self.contrastLabel4.setText(QCoreApplication.translate("guiMainWindow", u"Contrast", None))
        self.CurrentRoverStatus.setTitle(QCoreApplication.translate("guiMainWindow", u"Rover Info", None))
        self.OmegaNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Omega", None))
        self.ConfigValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"DRIVE", None))
        self.frequencyValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"? GHz", None))
        self.GPSNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"GPS", None))
        self.GPSValuesLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.ModeNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Mode", None))
        self.ModeValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0", None))
        self.OdomValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.OmegaValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.OdomNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Odom", None))
        self.VelocityValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"0.0", None))
        self.VelocityNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Velocity", None))
        self.CurrentSettingNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Config", None))
        self.frequencyNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Frequency", None))
        self.noiseValueLabel.setText(QCoreApplication.translate("guiMainWindow", u"-", None))
        self.noiseNameLabel.setText(QCoreApplication.translate("guiMainWindow", u"Noise", None))
        self.KillSwitchButton.setText(QCoreApplication.translate("guiMainWindow", u"Kill Switch", None))
        self.autologButton.setText(QCoreApplication.translate("guiMainWindow", u"AUTOLOG", None))
        self.sendButton.setText(QCoreApplication.translate("guiMainWindow", u"SEND", None))
        self.directionLabel.setText(QCoreApplication.translate("guiMainWindow", u"ARM FORWARD", None))
    # retranslateUi

