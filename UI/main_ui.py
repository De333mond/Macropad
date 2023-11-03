# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 645)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(54)
        sizePolicy.setVerticalStretch(54)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 1181, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1179, 99))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 99))
        self.ctxBtnGlobal = QPushButton(self.scrollAreaWidgetContents)
        self.ctxBtnGlobal.setObjectName(u"ctxBtnGlobal")
        self.ctxBtnGlobal.setGeometry(QRect(50, 40, 75, 24))
        self.ctxBtnChrome = QPushButton(self.scrollAreaWidgetContents)
        self.ctxBtnChrome.setObjectName(u"ctxBtnChrome")
        self.ctxBtnChrome.setGeometry(QRect(140, 40, 75, 24))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(290, 150, 113, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 130, 49, 16))
        self.macropad_layout = QWidget(self.centralwidget)
        self.macropad_layout.setObjectName(u"macropad_layout")
        self.macropad_layout.setGeometry(QRect(40, 140, 181, 391))
        self.btn4 = QPushButton(self.macropad_layout)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setGeometry(QRect(20, 200, 51, 51))
        self.btn5 = QPushButton(self.macropad_layout)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setGeometry(QRect(110, 20, 51, 51))
        self.btn8 = QPushButton(self.macropad_layout)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setGeometry(QRect(110, 200, 51, 51))
        self.btn7 = QPushButton(self.macropad_layout)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setGeometry(QRect(110, 140, 51, 51))
        self.btn6 = QPushButton(self.macropad_layout)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setGeometry(QRect(110, 80, 51, 51))
        self.btn3 = QPushButton(self.macropad_layout)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(20, 140, 51, 51))
        self.btn0 = QPushButton(self.macropad_layout)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setGeometry(QRect(20, 20, 51, 51))
        self.btn2 = QPushButton(self.macropad_layout)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(20, 80, 51, 51))
        self.encodedMinusBtn = QPushButton(self.macropad_layout)
        self.encodedMinusBtn.setObjectName(u"encodedMinusBtn")
        self.encodedMinusBtn.setGeometry(QRect(20, 310, 31, 31))
        self.encoderPushBtn = QPushButton(self.macropad_layout)
        self.encoderPushBtn.setObjectName(u"encoderPushBtn")
        self.encoderPushBtn.setGeometry(QRect(70, 290, 31, 31))
        self.encoderPlusBtn = QPushButton(self.macropad_layout)
        self.encoderPlusBtn.setObjectName(u"encoderPlusBtn")
        self.encoderPlusBtn.setGeometry(QRect(120, 310, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ctxBtnGlobal.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.ctxBtnChrome.setText(QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Header", None))
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn8.setText("")
        self.btn7.setText("")
        self.btn6.setText("")
        self.btn3.setText("")
        self.btn0.setText("")
        self.btn2.setText("")
        self.encodedMinusBtn.setText("")
        self.encoderPushBtn.setText("")
        self.encoderPlusBtn.setText("")
    # retranslateUi

