from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton
from logic.DataClasses import ContextConfig
from UI.stylesheets.styles import context_config_btn


class ContextConfigButton(QPushButton):
    context_clicked = Signal(ContextConfig)

    def __init__(self, context_config: ContextConfig):
        super().__init__()
        self.context_config = context_config
        self.setText(self.context_config.title)
        self.setMinimumSize(50, 50)
        self.setMaximumSize(150, 50)
        self.setStyleSheet(context_config_btn)

        self.setCheckable(True)
        self.setChecked(False)

        self.clicked.connect(lambda: self.context_clicked.emit(self.context_config))


