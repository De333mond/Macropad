# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QListWidget, QListWidgetItem,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 622)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(54)
        sizePolicy.setVerticalStretch(54)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: #ffffff;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"background-color: #0d1b2a;\n"
                                         "")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.choose_context_frame = QFrame(self.centralwidget)
        self.choose_context_frame.setObjectName(u"choose_context_frame")
        self.choose_context_frame.setFrameShape(QFrame.StyledPanel)
        self.choose_context_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.choose_context_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.context_scroll_area = QScrollArea(self.choose_context_frame)
        self.context_scroll_area.setObjectName(u"context_scroll_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.context_scroll_area.sizePolicy().hasHeightForWidth())
        self.context_scroll_area.setSizePolicy(sizePolicy1)
        self.context_scroll_area.setMinimumSize(QSize(0, 88))
        self.context_scroll_area.setStyleSheet(u"QScrollBar:horizontal {\n"
                                               "height: 6px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:horizontal {\n"
                                               "background-color: rgba(0,0,0, 0.25);\n"
                                               "\n"
                                               "border-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "QScrollBar:handle:horizontal:pressed {\n"
                                               "background-color: rgba(0,0,0, 0.35);\n"
                                               "\n"
                                               "border-radius: 3px;\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "")
        self.context_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.context_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.context_scroll_area.setWidgetResizable(True)
        self.context_scroll_content = QWidget()
        self.context_scroll_content.setObjectName(u"context_scroll_content")
        self.context_scroll_content.setGeometry(QRect(0, 0, 1134, 86))
        self.horizontalLayout_2 = QHBoxLayout(self.context_scroll_content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.context_list_frame = QFrame(self.context_scroll_content)
        self.context_list_frame.setObjectName(u"context_list_frame")
        self.context_list_frame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.context_list_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.context_element_btn = QPushButton(self.context_list_frame)
        self.context_element_btn.setObjectName(u"context_element_btn")
        self.context_element_btn.setMinimumSize(QSize(50, 50))
        self.context_element_btn.setMaximumSize(QSize(50, 50))
        self.context_element_btn.setStyleSheet(u"QPushButton {\n"
                                               "color: #e0e1dd;\n"
                                               "background-color: #1b263b;\n"
                                               "border-radius: 10px;\n"
                                               "border: 2px solid #778da9;\n"
                                               "}\n"
                                               "\n"
                                               ":pressed {\n"
                                               "background-color: #415a77;\n"
                                               "}\n"
                                               "\n"
                                               ":checked {\n"
                                               "background-color: #415a77;\n"
                                               "}")
        self.context_element_btn.setCheckable(True)
        self.context_element_btn.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.context_element_btn)

        self.horizontalLayout_2.addWidget(self.context_list_frame, 0, Qt.AlignLeft)

        self.context_scroll_area.setWidget(self.context_scroll_content)

        self.verticalLayout.addWidget(self.context_scroll_area)

        self.AddContextBtn = QPushButton(self.choose_context_frame)
        self.AddContextBtn.setObjectName(u"AddContextBtn")
        self.AddContextBtn.setMinimumSize(QSize(25, 25))
        self.AddContextBtn.setMaximumSize(QSize(25, 25))
        self.AddContextBtn.setStyleSheet(u"background-color: #778da9;\n"
                                         "")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_sq.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AddContextBtn.setIcon(icon)

        self.verticalLayout.addWidget(self.AddContextBtn)

        self.verticalLayout_2.addWidget(self.choose_context_frame)

        self.pad_settings_frame = QFrame(self.centralwidget)
        self.pad_settings_frame.setObjectName(u"pad_settings_frame")
        self.pad_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.pad_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.pad_settings_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pad_buttons_frame = QFrame(self.pad_settings_frame)
        self.pad_buttons_frame.setObjectName(u"pad_buttons_frame")
        self.pad_buttons_frame.setStyleSheet(u"background-color: #1b263b;")
        self.pad_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.pad_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pad_buttons_frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Macropad_layout = QFrame(self.pad_buttons_frame)
        self.Macropad_layout.setObjectName(u"Macropad_layout")
        self.Macropad_layout.setMinimumSize(QSize(196, 336))
        self.Macropad_layout.setMaximumSize(QSize(196, 336))
        self.Macropad_layout.setStyleSheet(u"border-radius: 15px;\n"
                                           "background-color: #0d1b2a;\n"
                                           "\n"
                                           "")
        self.verticalLayout_3 = QVBoxLayout(self.Macropad_layout)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.pad_layout = QHBoxLayout()
        self.pad_layout.setSpacing(70)
        self.pad_layout.setObjectName(u"pad_layout")
        self.pad_layout_left = QVBoxLayout()
        self.pad_layout_left.setSpacing(10)
        self.pad_layout_left.setObjectName(u"pad_layout_left")
        self.pad_btn_1 = QPushButton(self.Macropad_layout)
        self.pad_btn_1.setObjectName(u"pad_btn_1")
        self.pad_btn_1.setMinimumSize(QSize(50, 50))
        self.pad_btn_1.setMaximumSize(QSize(50, 50))
        self.pad_btn_1.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_1.setCheckable(True)
        self.pad_btn_1.setChecked(False)
        self.pad_btn_1.setFlat(False)

        self.pad_layout_left.addWidget(self.pad_btn_1)

        self.pad_btn_2 = QPushButton(self.Macropad_layout)
        self.pad_btn_2.setObjectName(u"pad_btn_2")
        self.pad_btn_2.setMinimumSize(QSize(50, 50))
        self.pad_btn_2.setMaximumSize(QSize(50, 50))
        self.pad_btn_2.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_2.setCheckable(True)
        self.pad_btn_2.setChecked(False)
        self.pad_btn_2.setFlat(False)

        self.pad_layout_left.addWidget(self.pad_btn_2)

        self.pad_btn_3 = QPushButton(self.Macropad_layout)
        self.pad_btn_3.setObjectName(u"pad_btn_3")
        self.pad_btn_3.setMinimumSize(QSize(50, 50))
        self.pad_btn_3.setMaximumSize(QSize(50, 50))
        self.pad_btn_3.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_3.setCheckable(True)
        self.pad_btn_3.setChecked(False)
        self.pad_btn_3.setFlat(False)

        self.pad_layout_left.addWidget(self.pad_btn_3)

        self.pad_btn_4 = QPushButton(self.Macropad_layout)
        self.pad_btn_4.setObjectName(u"pad_btn_4")
        self.pad_btn_4.setMinimumSize(QSize(50, 50))
        self.pad_btn_4.setMaximumSize(QSize(50, 50))
        self.pad_btn_4.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_4.setCheckable(True)
        self.pad_btn_4.setChecked(False)
        self.pad_btn_4.setFlat(False)

        self.pad_layout_left.addWidget(self.pad_btn_4)

        self.pad_layout.addLayout(self.pad_layout_left)

        self.pad_layout_right = QVBoxLayout()
        self.pad_layout_right.setSpacing(10)
        self.pad_layout_right.setObjectName(u"pad_layout_right")
        self.pad_btn_5 = QPushButton(self.Macropad_layout)
        self.pad_btn_5.setObjectName(u"pad_btn_5")
        self.pad_btn_5.setMinimumSize(QSize(50, 50))
        self.pad_btn_5.setMaximumSize(QSize(50, 50))
        self.pad_btn_5.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_5.setCheckable(True)
        self.pad_btn_5.setChecked(False)
        self.pad_btn_5.setFlat(False)

        self.pad_layout_right.addWidget(self.pad_btn_5)

        self.pad_btn_6 = QPushButton(self.Macropad_layout)
        self.pad_btn_6.setObjectName(u"pad_btn_6")
        self.pad_btn_6.setMinimumSize(QSize(50, 50))
        self.pad_btn_6.setMaximumSize(QSize(50, 50))
        self.pad_btn_6.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_6.setCheckable(True)
        self.pad_btn_6.setChecked(False)
        self.pad_btn_6.setFlat(False)

        self.pad_layout_right.addWidget(self.pad_btn_6)

        self.pad_btn_7 = QPushButton(self.Macropad_layout)
        self.pad_btn_7.setObjectName(u"pad_btn_7")
        self.pad_btn_7.setMinimumSize(QSize(50, 50))
        self.pad_btn_7.setMaximumSize(QSize(50, 50))
        self.pad_btn_7.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_7.setCheckable(True)
        self.pad_btn_7.setChecked(False)
        self.pad_btn_7.setFlat(False)

        self.pad_layout_right.addWidget(self.pad_btn_7)

        self.pad_btn_8 = QPushButton(self.Macropad_layout)
        self.pad_btn_8.setObjectName(u"pad_btn_8")
        self.pad_btn_8.setMinimumSize(QSize(50, 50))
        self.pad_btn_8.setMaximumSize(QSize(50, 50))
        self.pad_btn_8.setStyleSheet(u"QPushButton {\n"
                                     "background-color: #1b263b;\n"
                                     "}\n"
                                     "\n"
                                     ":pressed {\n"
                                     "background-color: #415a77;\n"
                                     "}\n"
                                     "\n"
                                     ":checked {\n"
                                     "background-color: #415a77;\n"
                                     "}")
        self.pad_btn_8.setCheckable(True)
        self.pad_btn_8.setChecked(False)
        self.pad_btn_8.setFlat(False)

        self.pad_layout_right.addWidget(self.pad_btn_8)

        self.pad_layout.addLayout(self.pad_layout_right)

        self.verticalLayout_3.addLayout(self.pad_layout)

        self.encoder_layout = QHBoxLayout()
        self.encoder_layout.setSpacing(10)
        self.encoder_layout.setObjectName(u"encoder_layout")
        self.encoder_btn_down = QPushButton(self.Macropad_layout)
        self.encoder_btn_down.setObjectName(u"encoder_btn_down")
        self.encoder_btn_down.setMinimumSize(QSize(50, 50))
        self.encoder_btn_down.setMaximumSize(QSize(50, 50))
        self.encoder_btn_down.setStyleSheet(u"QPushButton {\n"
                                            "background-color: #1b263b;\n"
                                            "}\n"
                                            "\n"
                                            ":pressed {\n"
                                            "background-color: #415a77;\n"
                                            "}\n"
                                            "\n"
                                            ":checked {\n"
                                            "background-color: #415a77;\n"
                                            "}")
        self.encoder_btn_down.setCheckable(True)
        self.encoder_btn_down.setChecked(False)
        self.encoder_btn_down.setFlat(False)

        self.encoder_layout.addWidget(self.encoder_btn_down)

        self.encoder_btn_push = QPushButton(self.Macropad_layout)
        self.encoder_btn_push.setObjectName(u"encoder_btn_push")
        self.encoder_btn_push.setMinimumSize(QSize(50, 50))
        self.encoder_btn_push.setMaximumSize(QSize(50, 50))
        self.encoder_btn_push.setStyleSheet(u"QPushButton {\n"
                                            "background-color: #1b263b;\n"
                                            "}\n"
                                            "\n"
                                            ":pressed {\n"
                                            "background-color: #415a77;\n"
                                            "}\n"
                                            "\n"
                                            ":checked {\n"
                                            "background-color: #415a77;\n"
                                            "}")
        self.encoder_btn_push.setCheckable(True)
        self.encoder_btn_push.setChecked(False)
        self.encoder_btn_push.setFlat(False)

        self.encoder_layout.addWidget(self.encoder_btn_push)

        self.encoder_btn_up = QPushButton(self.Macropad_layout)
        self.encoder_btn_up.setObjectName(u"encoder_btn_up")
        self.encoder_btn_up.setMinimumSize(QSize(50, 50))
        self.encoder_btn_up.setMaximumSize(QSize(50, 50))
        self.encoder_btn_up.setStyleSheet(u"QPushButton {\n"
                                          "background-color: #1b263b;\n"
                                          "}\n"
                                          "\n"
                                          ":pressed {\n"
                                          "background-color: #415a77;\n"
                                          "}\n"
                                          "\n"
                                          ":checked {\n"
                                          "background-color: #415a77;\n"
                                          "}")
        self.encoder_btn_up.setCheckable(True)
        self.encoder_btn_up.setChecked(False)
        self.encoder_btn_up.setFlat(False)

        self.encoder_layout.addWidget(self.encoder_btn_up)

        self.verticalLayout_3.addLayout(self.encoder_layout)

        self.verticalLayout_4.addWidget(self.Macropad_layout)

        self.encoder_context_list = QListWidget(self.pad_buttons_frame)
        QListWidgetItem(self.encoder_context_list)
        self.encoder_context_list.setObjectName(u"encoder_context_list")
        self.encoder_context_list.setMaximumSize(QSize(196, 16000000))
        self.encoder_context_list.setStyleSheet(u"background-color: #0d1b2a;\n"
                                                "color: #e0e1dd;")
        self.encoder_context_list.setSpacing(0)

        self.verticalLayout_4.addWidget(self.encoder_context_list)

        self.horizontalLayout_3.addWidget(self.pad_buttons_frame)

        self.settings_frame = QFrame(self.pad_settings_frame)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setStyleSheet(u"background-color: #0d1b2a;")
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.default_settings_frame = QFrame(self.settings_frame)
        self.default_settings_frame.setObjectName(u"default_settings_frame")
        self.default_settings_frame.setStyleSheet(u"background-color: #1b263b;")
        self.horizontalLayout_16 = QHBoxLayout(self.default_settings_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(6, 6, 6, 6)
        self.macro_label_frame = QFrame(self.default_settings_frame)
        self.macro_label_frame.setObjectName(u"macro_label_frame")
        self.verticalLayout_9 = QVBoxLayout(self.macro_label_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.macro_label_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #e0e1dd;")

        self.verticalLayout_9.addWidget(self.label, 0, Qt.AlignTop)

        self.lineEdit = QLineEdit(self.macro_label_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(110, 0))
        self.lineEdit.setStyleSheet(u"border: 2px solid #0d1b2a;\n"
                                    "border-radius: 5%;")

        self.verticalLayout_9.addWidget(self.lineEdit, 0, Qt.AlignTop)

        self.horizontalLayout_16.addWidget(self.macro_label_frame, 0, Qt.AlignLeft | Qt.AlignTop)

        self.choose_image_frame = QFrame(self.default_settings_frame)
        self.choose_image_frame.setObjectName(u"choose_image_frame")
        self.choose_image_frame.setMaximumSize(QSize(178, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.choose_image_frame)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(6, 6, 6, 6)
        self.image_prewiew_label = QLabel(self.choose_image_frame)
        self.image_prewiew_label.setObjectName(u"image_prewiew_label")
        self.image_prewiew_label.setMinimumSize(QSize(64, 64))
        self.image_prewiew_label.setMaximumSize(QSize(64, 64))
        self.image_prewiew_label.setStyleSheet(u"border: 1px solid #0d1b2a;\n"
                                               "")
        self.image_prewiew_label.setPixmap(QPixmap(u":/icons/icons/no_2.svg"))
        self.image_prewiew_label.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.image_prewiew_label)

        self.image_btns_layout = QVBoxLayout()
        self.image_btns_layout.setObjectName(u"image_btns_layout")
        self.image_btns_layout.setContentsMargins(5, 5, 5, 5)
        self.open_image_btn = QPushButton(self.choose_image_frame)
        self.open_image_btn.setObjectName(u"open_image_btn")
        self.open_image_btn.setStyleSheet(u"QPushButton {\n"
                                          "	color: #e0e1dd;\n"
                                          "	background-color: #415a77;\n"
                                          "}")

        self.image_btns_layout.addWidget(self.open_image_btn)

        self.draw_image_btn = QPushButton(self.choose_image_frame)
        self.draw_image_btn.setObjectName(u"draw_image_btn")
        self.draw_image_btn.setStyleSheet(u"QPushButton {\n"
                                          "	color: #e0e1dd;\n"
                                          "	background-color: #415a77;\n"
                                          "}")

        self.image_btns_layout.addWidget(self.draw_image_btn)

        self.horizontalLayout_15.addLayout(self.image_btns_layout)

        self.horizontalLayout_16.addWidget(self.choose_image_frame)

        self.verticalLayout_11.addWidget(self.default_settings_frame)

        self.action_settings_frame = QFrame(self.settings_frame)
        self.action_settings_frame.setObjectName(u"action_settings_frame")
        self.action_settings_frame.setStyleSheet(u"background-color: #1b263b;")
        self.action_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.action_settings_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.action_settings_frame)

        self.verticalLayout_11.setStretch(1, 1)

        self.horizontalLayout_3.addWidget(self.settings_frame)

        self.actions_frame = QFrame(self.pad_settings_frame)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setStyleSheet(u"background-color: #1b263b;")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.actionss_list = QListWidget(self.actions_frame)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        QListWidgetItem(self.actionss_list)
        self.actionss_list.setObjectName(u"actionss_list")
        self.actionss_list.setStyleSheet(u"background-color: #0d1b2a;\n"
                                         "color: #e0e1dd;")

        self.horizontalLayout_7.addWidget(self.actionss_list)

        self.horizontalLayout_3.addWidget(self.actions_frame)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.pad_settings_frame)

        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pad_btn_1.setDefault(False)
        self.pad_btn_2.setDefault(False)
        self.pad_btn_3.setDefault(False)
        self.pad_btn_4.setDefault(False)
        self.pad_btn_5.setDefault(False)
        self.pad_btn_6.setDefault(False)
        self.pad_btn_7.setDefault(False)
        self.pad_btn_8.setDefault(False)
        self.encoder_btn_down.setDefault(False)
        self.encoder_btn_push.setDefault(False)
        self.encoder_btn_up.setDefault(False)
        self.encoder_context_list.setCurrentRow(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.context_element_btn.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.AddContextBtn.setText("")
        self.pad_btn_1.setText("")
        self.pad_btn_2.setText("")
        self.pad_btn_3.setText("")
        self.pad_btn_4.setText("")
        self.pad_btn_5.setText("")
        self.pad_btn_6.setText("")
        self.pad_btn_7.setText("")
        self.pad_btn_8.setText("")
        self.encoder_btn_down.setText("")
        self.encoder_btn_push.setText("")
        self.encoder_btn_up.setText("")

        __sortingEnabled = self.encoder_context_list.isSortingEnabled()
        self.encoder_context_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.encoder_context_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Default", None));
        self.encoder_context_list.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"label", None))
        self.image_prewiew_label.setText("")
        self.open_image_btn.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.draw_image_btn.setText(QCoreApplication.translate("MainWindow", u"Draw Image", None))

        __sortingEnabled1 = self.actionss_list.isSortingEnabled()
        self.actionss_list.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.actionss_list.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0430\u0439\u0442",
                                                               None));
        ___qlistwidgetitem2 = self.actionss_list.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u041c\u0443\u043b\u044c\u0442\u0438\u043c\u0435\u0434\u0438\u044f",
                                                               None));
        ___qlistwidgetitem3 = self.actionss_list.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443",
                                                               None));
        ___qlistwidgetitem4 = self.actionss_list.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448",
                                                               None));
        ___qlistwidgetitem5 = self.actionss_list.item(4)
        ___qlistwidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0440\u043e\u0441", None));
        ___qlistwidgetitem6 = self.actionss_list.item(5)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442",
                                                               None));
        ___qlistwidgetitem7 = self.actionss_list.item(6)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0435\u0441\u0442 \u044d\u043d\u043a\u043e\u0434\u0435\u0440\u0430",
                                                               None));
        self.actionss_list.setSortingEnabled(__sortingEnabled1)

    # retranslateUi
