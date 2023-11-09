from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton,
                               QHBoxLayout, QSplitter, QLabel, QMessageBox, QFileDialog, QLineEdit,
                               QRadioButton, QGroupBox, QCheckBox, QFrame, QListWidget, QListWidgetItem)

from UI.Widgets.components import PadButton
class PadWidget(QFrame):
    # self.button_clicked.emit(3)
    button_clicked = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._button_list: list[PadButton] = []

        self.pad_buttons_frame = QFrame(parent)
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

        self.pad_btn_1 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_1)

        self.pad_btn_2 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_2)

        self.pad_btn_3 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_3)

        self.pad_btn_4 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_4)

        self.pad_layout.addLayout(self.pad_layout_left)

        self.pad_layout_right = QVBoxLayout()
        self.pad_layout_right.setSpacing(10)
        self.pad_layout_right.setObjectName(u"pad_layout_right")

        self.pad_btn_5 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_5)

        self.pad_btn_6 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_6)

        self.pad_btn_7 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_7)

        self.pad_btn_8 = PadButton(self.Macropad_layout)
        self.pad_layout_left.addWidget(self.pad_btn_8)

        self.pad_layout.addLayout(self.pad_layout_right)

        self.verticalLayout_3.addLayout(self.pad_layout)

        self.encoder_layout = QHBoxLayout()
        self.encoder_layout.setSpacing(10)
        self.encoder_layout.setObjectName(u"encoder_layout")

        self.encoder_btn_down = PadButton(self.Macropad_layout)
        self.encoder_layout.addWidget(self.encoder_btn_down)

        self.encoder_btn_push = PadButton(self.Macropad_layout)
        self.encoder_layout.addWidget(self.encoder_btn_down)

        self.encoder_btn_up = PadButton(self.Macropad_layout)
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

        parent.layout().addWidget(self.pad_buttons_frame)

        self._button_list.append(self.pad_btn_1)
        self._button_list.append(self.pad_btn_2)
        self._button_list.append(self.pad_btn_3)
        self._button_list.append(self.pad_btn_4)
        self._button_list.append(self.pad_btn_5)
        self._button_list.append(self.pad_btn_6)
        self._button_list.append(self.pad_btn_7)
        self._button_list.append(self.pad_btn_8)
        self._button_list.append(self.encoder_btn_down)
        self._button_list.append(self.encoder_btn_push)
        self._button_list.append(self.encoder_btn_up)

        for i in range(len(self._button_list)):
            self._button_list[i].clicked.connect(lambda: self._handle_btn_click(i))

    def _handle_btn_click(self, btn_num):
        for i in range(len(self._button_list)):
            self._button_list[i].setChecked(False)

        self.button_clicked.emit(btn_num)
