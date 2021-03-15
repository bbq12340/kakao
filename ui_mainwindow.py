# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet(u".QMainWindow {\n"
"	background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelFrame = QFrame(self.centralwidget)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setStyleSheet(u".QFrame {\n"
"	border: none;\n"
"}")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.labelFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 391, 141))
        self.label.setPixmap(QPixmap(u"daum.png"))

        self.verticalLayout.addWidget(self.labelFrame)

        self.inputFrame = QFrame(self.centralwidget)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setStyleSheet(u".QFrame {\n"
"	background-color: lightgray;\n"
"	border-radius: 10px;\n"
"}")
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.inputFileButton = QPushButton(self.inputFrame)
        self.inputFileButton.setObjectName(u"inputFileButton")
        self.inputFileButton.setGeometry(QRect(20, 20, 113, 32))
        self.inputFileLabel = QLabel(self.inputFrame)
        self.inputFileLabel.setObjectName(u"inputFileLabel")
        self.inputFileLabel.setGeometry(QRect(160, 20, 113, 32))
        self.inputFileLabel.setAlignment(Qt.AlignCenter)
        self.delayLabel = QLabel(self.inputFrame)
        self.delayLabel.setObjectName(u"delayLabel")
        self.delayLabel.setGeometry(QRect(20, 90, 113, 32))
        self.delayLabel.setAlignment(Qt.AlignCenter)
        self.delaySpinBox = QDoubleSpinBox(self.inputFrame)
        self.delaySpinBox.setObjectName(u"delaySpinBox")
        self.delaySpinBox.setGeometry(QRect(160, 90, 113, 32))
        self.delaySpinBox.setStyleSheet(u".QDoubleSpinBox {\n"
"	border-radius: 5px;\n"
"}")
        self.delaySpinBox.setAlignment(Qt.AlignCenter)
        self.delaySpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.delaySpinBox.setDecimals(1)
        self.delaySpinBox.setSingleStep(0.500000000000000)

        self.verticalLayout.addWidget(self.inputFrame)

        self.buttonFrame = QFrame(self.centralwidget)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setStyleSheet(u".QFrame {\n"
"	background-color: lightgray;\n"
"	border-radius: 10px;\n"
"}")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.buttonFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 170, 461, 23))
        self.progressBar.setValue(0)
        self.startButton = QPushButton(self.buttonFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(80, 60, 113, 60))
        self.openButton = QPushButton(self.buttonFrame)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setGeometry(QRect(250, 60, 113, 60))

        self.verticalLayout.addWidget(self.buttonFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.inputFileButton.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc785\ub825", None))
        self.inputFileLabel.setText("")
        self.delayLabel.setText(QCoreApplication.translate("MainWindow", u"\ub51c\ub808\uc774", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
    # retranslateUi

