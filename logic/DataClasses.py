from dataclasses import dataclass

from logic.Action import Action


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
    actionPlus: Action
    actionPlus: Action


@dataclass
class ContextConfig:
    title: str
    image: str
    window: WindowInfo
    buttons: list[Button]
    current_encoder: int
    encoders: list[Encoder]


