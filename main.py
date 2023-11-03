import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from UI.main_ui import Ui_MainWindow


class MacropadMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacropadMainWindow()

    window.show()
    app.exec()
