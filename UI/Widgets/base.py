from PySide6.QtWidgets import QWidget

from UI.stylesheets.styles import base_widget_style


class BWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(base_widget_style)
