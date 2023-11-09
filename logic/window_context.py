from threading import Thread
from time import sleep

import psutil
import win32gui
import win32process

from DataClasses import WindowInfo
from utils import Event


class WindowContextManager:
    def __init__(self):
        self.current_window: WindowInfo | None = None
        self.update_timeout = 0.1
        self.history_buffer = 10
        self.history: list[WindowInfo] = []
        self._is_running = False
        self.thread: Thread | None = None
        self.on_window_changed: Event = Event[WindowInfo]()

    @staticmethod
    def _capture() -> WindowInfo:
        active_window = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(active_window)[1]
        process = psutil.Process(pid)

        return WindowInfo(
            pid=pid,
            title=win32gui.GetWindowText(active_window),
            process=process.name(),
            path=process.exe()
        )

    def _capture_process(self):
        while self._is_running:
            sleep(self.update_timeout)
            window = self._capture()

            if self.current_window and self.current_window == window:
                continue
            else:
                self.current_window = window
                self._history_append(window)
                self.on_window_changed.invoke(window)

    def _history_append(self, window):
        self.history.insert(0, window)
        if len(self.history) > self.history_buffer:
            self.history.pop()

    def start(self):
        self._is_running = True
        self.thread: Thread = Thread(target=self._capture_process, name="Capture process")
        self.thread.start()

    def stop(self):
        if self.thread is not None:
            self._is_running = False
            self.thread = None
