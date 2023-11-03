from typing import Callable, Generic, TypeVar

T = TypeVar('T')


class Event(Generic[T]):
    def __init__(self):
        self.listeners = []

    def add_listener(self, func: Callable[[T], None]):
        self.listeners.append(func)

    def invoke(self, value: T):
        for listener in self.listeners:
            listener(value)
