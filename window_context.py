from dataclasses import dataclass
from threading import Thread
from time import sleep
from typing import Callable

import win32gui
import win32process
import psutil


@dataclass
class WindowInfo:
    pid: int
    title: str
    process: str
    path: str

    def __str__(self):
        return self.process.split(".exe")[0].capitalize()

    def __repr__(self):
        return self.__str__()



class WindowContextManager:
    def __init__(self):
        self.current_window: WindowInfo | None = None
        self.update_timeout = 0.1
        self.history_buffer = 10
        self.history: list[WindowInfo] = []
        self._is_running = False
        self.listeners: list[Callable] = []
        self.thread: Thread | None = None

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
                self._on_current_change()

    def _history_append(self, window):
        self.history.insert(0, window)
        if len(self.history) > self.history_buffer:
            self.history.pop()

    def _on_current_change(self):
        for el in self.listeners:
            el(self)

    def start(self):
        self._is_running = True
        self.thread: Thread = Thread(target=self._capture_process, name="Capture process")
        self.thread.start()

    def stop(self):
        if self.thread is not None:
            self._is_running = False
            self.thread = None
