from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QScrollArea, QPushButton, QWidget, QHBoxLayout, QSizePolicy

from UI.Widgets.components import Label, ContextConfigButton
from .base import BWidget
from logic.DataClasses import ContextConfig
from logic.ConfigController import ConfigController


class ChooseContextWidget(BWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config_controller = ConfigController()
        self.config_controller.load()

        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        layout.align = Qt.AlignLeft

        self.scroll_area = QScrollArea()
        self.scroll_content_widget = QWidget()
        self.scroll_content_layout = QHBoxLayout()
        self.load_config(self.config_controller.config)
        self.scroll_content_widget.setLayout(self.scroll_content_layout)

        self.scroll_content_layout.setAlignment(Qt.AlignLeft)
        
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content_widget)
        layout.addWidget(self.scroll_area)

        self.add_context_button = QPushButton('Add Context')
        self.add_context_button.clicked.connect(self.handle_add_context_btn)
        layout.addWidget(self.add_context_button)
        self.add_context_button.setMaximumWidth(100)
        self.setLayout(layout)

    def handle_add_context_btn(self):
        config = self.config_controller.save_app_context(self.config_controller.default_config)
        button = ContextConfigButton(config)
        button.context_clicked.connect(self.handle_context_btn_click)
        self.scroll_content_layout.addWidget(button, 0)


    def handle_context_btn_click(self, config: ContextConfig):
        print(config)

    def load_config(self, config: list[ContextConfig]):
        for context in config:
            button = ContextConfigButton(context)
            button.context_clicked.connect(self.handle_context_btn_click)
            self.scroll_content_layout.addWidget(button)

