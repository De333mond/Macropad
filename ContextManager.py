import threading
from UI.main_ui import Ui_MainWindow
import pygetwindow
import time
import psutil
import win32gui


class ContextManager:
    def __init__(self, window: Ui_MainWindow):
        self.current_context = None
        self.listeners = []
        self._is_running = False
        self.window = window
        self.bind_actions()
        self.delay = 0.1

    def bind_actions(self):
        self.window.start_btn.clicked.connect(self.scan)
        self.window.stop_btn.clicked.connect(self.stop)


    def add_listener(self, func):
        self.listeners.append(func)

    def _invoke(self, value):
        for func in self.listeners:
            time.sleep(self.delay)
            func(value)

    def get_context(self):
        while self._is_running:
            pid = win32gui.GetForegroundWindow()
            res = win32gui.GetWindowText(pid)
            print(res)


    def scan(self):

        scan_thread = threading.Thread(target=self.get_context,)
        self._is_running = True
        scan_thread.start()

    def stop(self):

        self._is_running = False



