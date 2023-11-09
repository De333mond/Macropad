from DataClasses import WindowInfo, ContextConfig
from logic.ConfigController import ConfigController
from logic.window_context import WindowContextManager
from logic.utils import Event


class ContextManager:
    def __init__(self):
        self.current_context_key: str = 'Global'
        self.context_config: ConfigController = ConfigController()
        self.window_manger: WindowContextManager = WindowContextManager()

        self.window_manger.on_window_changed.bind(self._on_window_changed)

        self.window_manger.start()

        self.on_context_changed: Event = Event[ContextConfig]()

        self.context_config.load()


    @property
    def current_context(self) -> ContextConfig:
        return self.context_config[self.current_context_key]

    @property
    def keys(self):
        return self.context_config.config.keys()

    def _on_window_changed(self, window: WindowInfo):
        for key, value in self.context_config.config.items():
            if value.window == window:
                self.current_context_key = key
                self.on_context_changed.invoke(self.current_context)
                return



if __name__ == "__main__":
    manager = ContextManager()
    manager.on_context_changed.bind(print)






