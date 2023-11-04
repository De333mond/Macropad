import dataclasses
import json
from typing import Callable, Generic, TypeVar

from logic.Action import Action

T = TypeVar('T')


class Event(Generic[T]):
    def __init__(self):
        self._listeners = []

    def bind(self, func: Callable[[T], None]):
        self._listeners.append(func)

    def invoke(self, value: T):
        for listener in self._listeners:
            listener(value)

    def unbind(self, func: Callable[[T], None]):
        self._listeners = filter(lambda x: x != func, self._listeners)


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, Action):
            return o.get_config()
        return super().default(o)
