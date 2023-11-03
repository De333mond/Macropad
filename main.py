import sys
from pprint import pprint

from PySide6.QtWidgets import QApplication, QMainWindow
from UI.main_ui import Ui_MainWindow
from ContextManager import ContextManager
from window_context import WindowContextManager, WindowInfo


class MacropadMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def print_window(manager: WindowContextManager):
    window.context_output.setText(str(manager.current_window))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacropadMainWindow()

    win_manager = WindowContextManager()

    win_manager.listeners.append(print_window)

    window.start_btn.clicked.connect(win_manager.start)
    window.stop_btn.clicked.connect(win_manager.stop)

    window.show()
    app.exec()
