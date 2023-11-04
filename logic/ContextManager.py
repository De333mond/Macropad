from DataClasses import WindowInfo, ContextConfig
from logic.utils import Event


class ContextManager:
    def __init__(self):
        self.current_context: ContextConfig
        self.context_list: list[ContextConfig] = []
        self.on_context_changed: Event = Event[ContextConfig]()

