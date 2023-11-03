from DataClasses import WindowInfo, ContextConfig


class ContextManager:
    def __init__(self):
        self.current_context: ContextConfig

    def set_window(self, window: WindowInfo):
        self.current_window = window
