import json

from logic.Action import Action
from logic.DataClasses import ContextConfig, Button, Encoder, WindowInfo
from utils import Event, EnhancedJSONEncoder


class ConfigController:
    config_path = '../config.json'
    default_config: ContextConfig = ContextConfig(
            image='',
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
        self.config: dict[str, ContextConfig] = {}
        self.on_config_changed: Event = Event[dict]()

    def init(self):
        try:
            self._load_config()
        except FileNotFoundError:
            self.save_app_context('Global', self.default_config)

    def create_default(self):
        title = "untitled"
        index = 0
        while ((title + str(index)) if index > 0 else title) in self.config.keys():
            index += 1

        return ((title + str(index)) if index > 0 else title), self.default_config

    def save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            json.dump(self.config, file, cls=EnhancedJSONEncoder)

    def save_app_context(self, context: str, config: ContextConfig):
        self.config.update({context: config})
        self.save_config()
        self.on_config_changed.invoke(self.config)

    def __getitem__(self, item):
        return {**self.config[item]}

    def _load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            data: dict = json.load(file)
            for key, value in data.items():
                buttons = [Button(**el) for el in value["buttons"]]
                encoders = [Encoder(**el) for el in value['encoders']]
                window = None
                if value['window']:
                    window = WindowInfo(
                        pid=value['window']['pid'],
                        title=value['window']['title'],
                        process=value['window']['process'],
                        path=value['window']['path'],
                    )

                self.config.update({
                    key: ContextConfig(
                        image=value['image'],
                        window=window,
                        buttons=buttons,
                        current_encoder=0,
                        encoders=encoders
                    )}
                )
        self.on_config_changed.invoke(self.config)


if __name__ == "__main__":
    conf = ConfigController()
    conf.init()


