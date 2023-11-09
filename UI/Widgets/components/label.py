from PySide6.QtWidgets import QLabel
from UI.stylesheets.styles import label_widget_style

class Label(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(label_widget_style)

