from PyQt5.QtWidgets import QPushButton

class PadButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PadButton")
        self.setMinimumSize(50, 50)
        self.setMaximumSize(50, 50)
        self.setStyleSheet(
            "QPushButton {\n"
            "background-color: #1b263b;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #415a77;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "background-color: #415a77;\n"
            "}"
        )
        self.setCheckable(True)
        self.setChecked(False)
        self.setFlat(False)
