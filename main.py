import sys

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy, QWidget, QLabel, QVBoxLayout

from UI.Widgets import ChooseContextWidget
from UI.stylesheets.styles import central_widget_style

from UI.main_ui import Ui_MainWindow
from UI.Widgets import PadWidget


class BlockWidget(QWidget):
    clicked = Signal(str)
    def __init__(self, text, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel(text)
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(lambda: self.clicked.emit(text))
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class MacropadMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_widget = QWidget()
        main_widget.setStyleSheet(central_widget_style)
        main_layout = QVBoxLayout()


        self.choose_context_widget = ChooseContextWidget()
        main_layout.addWidget(self.choose_context_widget)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacropadMainWindow()
    window.show()
    app.exec()
