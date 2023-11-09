import json

from logic.Action import Action
from logic.DataClasses import ContextConfig, Button, Encoder, WindowInfo
from .utils import Event, EnhancedJSONEncoder


class ConfigController:
    config_path = 'D:\Git\Macropad\config.json'

    @property
    def default_config(self) -> ContextConfig:
        return ContextConfig(
            image='',
            title='Global',
            window=None,
            buttons=[
                Button(
                    label='Button1',
                    index=0,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button2',
                    index=1,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button3',
                    index=2,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button4',
                    index=3,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button5',
                    index=4,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button6',
                    index=5,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button7',
                    index=6,
                    action=Action().get_config(),
                ),
                Button(
                    label='Button8',
                    index=7,
                    action=Action().get_config(),
                ),

            ],
            current_encoder=0,
            encoders=[
                Encoder(
                    label='Encoder1',
                    actionPlus=Action().get_config(),
                    actionPush=Action().get_config(),
                    actionMinus=Action().get_config(),
                )
            ]
        )

    def __init__(self):
        self.config: list[ContextConfig] = []

    def load(self) -> None:
        try:
            self._load_config()
        except FileNotFoundError:
            self.save_app_context(self.default_config)

    def save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            json.dump(self.config, file, cls=EnhancedJSONEncoder)

    def save_app_context(self, config: ContextConfig) -> ContextConfig:
        i = 0
        title = str(config.title)
        while any([el.title == title + (f'_{i}' if i > 0 else '') for el in self.config]):
            i += 1

        config.title = title + (f'_{i}' if i > 0 else '')

        self.config.append(config)
        self.save_config()
        return config

    def _load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            data: list = json.load(file)
            for context in data:
                buttons = [Button(**el) for el in context["buttons"]]
                encoders = [Encoder(**el) for el in context['encoders']]
                window = None
                if context['window']:
                    window = WindowInfo(
                        pid=context['window']['pid'],
                        title=context['window']['title'],
                        process=context['window']['process'],
                        path=context['window']['path'],
                    )

                self.config.append(
                    ContextConfig(
                        image=context['image'],
                        title=context['title'],
                        window=window,
                        buttons=buttons,
                        current_encoder=0,
                        encoders=encoders
                    )
                )


if __name__ == "__main__":
    conf = ConfigController()
    conf.load()


