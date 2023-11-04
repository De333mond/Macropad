import json
from dataclasses import dataclass

from logic.Action import Action
from logic.utils import EnhancedJSONEncoder


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


@dataclass
class Button:
    label: str
    index: int
    action: Action


@dataclass
class Encoder:
    label: str
    actionMinus: Action
    actionPush: Action
    actionPlus: Action


@dataclass
class ContextConfig:
    image: str
    window: WindowInfo | None
    buttons: list[Button]
    current_encoder: int
    encoders: list[Encoder]


if __name__ == "__main__":
    pass
