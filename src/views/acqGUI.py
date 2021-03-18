# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acquisition.ui'
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
        MainWindow.resize(1012, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonStop = QPushButton(self.centralwidget)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setGeometry(QRect(390, 530, 51, 41))
        self.frameDisplayImage = QFrame(self.centralwidget)
        self.frameDisplayImage.setObjectName(u"frameDisplayImage")
        self.frameDisplayImage.setGeometry(QRect(40, 40, 811, 481))
        self.frameDisplayImage.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayImage.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frameDisplayImage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 811, 481))
        self.layoutShowImage = QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutShowImage.setObjectName(u"layoutShowImage")
        self.layoutShowImage.setContentsMargins(0, 0, 0, 0)
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(30, 0, 171, 31))
        self.pushButtonInit = QPushButton(self.centralwidget)
        self.pushButtonInit.setObjectName(u"pushButtonInit")
        self.pushButtonInit.setGeometry(QRect(180, 530, 51, 41))
        self.pushButtonCapture = QPushButton(self.centralwidget)
        self.pushButtonCapture.setObjectName(u"pushButtonCapture")
        self.pushButtonCapture.setGeometry(QRect(250, 530, 51, 41))
        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(320, 530, 51, 41))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(860, 30, 131, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEditNoImages = QLineEdit(self.frame)
        self.lineEditNoImages.setObjectName(u"lineEditNoImages")
        self.lineEditNoImages.setGeometry(QRect(10, 100, 113, 20))
        self.pushButtonPlay = QPushButton(self.frame)
        self.pushButtonPlay.setObjectName(u"pushButtonPlay")
        self.pushButtonPlay.setGeometry(QRect(10, 130, 111, 41))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 91, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 71, 20))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 61, 16))
        self.labelImagesCapt = QLabel(self.frame)
        self.labelImagesCapt.setObjectName(u"labelImagesCapt")
        self.labelImagesCapt.setGeometry(QRect(80, 190, 31, 16))
        self.progressBarAcq = QProgressBar(self.frame)
        self.progressBarAcq.setObjectName(u"progressBarAcq")
        self.progressBarAcq.setGeometry(QRect(10, 220, 111, 23))
        self.progressBarAcq.setValue(0)
        self.lineEditDelay = QLineEdit(self.frame)
        self.lineEditDelay.setObjectName(u"lineEditDelay")
        self.lineEditDelay.setGeometry(QRect(10, 50, 113, 20))
        self.labelDelay = QLabel(self.frame)
        self.labelDelay.setObjectName(u"labelDelay")
        self.labelDelay.setGeometry(QRect(10, 30, 91, 16))
        self.lineEditframeRate = QLineEdit(self.centralwidget)
        self.lineEditframeRate.setObjectName(u"lineEditframeRate")
        self.lineEditframeRate.setGeometry(QRect(610, 550, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(610, 530, 91, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(470, 530, 111, 41))
        self.labelLogoFlir = QLabel(self.centralwidget)
        self.labelLogoFlir.setObjectName(u"labelLogoFlir")
        self.labelLogoFlir.setGeometry(QRect(240, 0, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonStop.setText("")
        self.labelLogo.setText("")
        self.pushButtonInit.setText("")
        self.pushButtonCapture.setText("")
        self.pushButtonSave.setText("")
        self.lineEditNoImages.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButtonPlay.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"No. Images", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Acquisition", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Captured:", None))
        self.labelImagesCapt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditDelay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelDelay.setText(QCoreApplication.translate("MainWindow", u"Delay (s)", None))
        self.lineEditframeRate.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frame rate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"rgb image", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"gray image", None))

        self.labelLogoFlir.setText("")
    # retranslateUi

