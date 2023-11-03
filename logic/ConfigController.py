import json

from utils import Event


class ConfigController:
    config_path = '../config.json'
    default_config = {
        'Global': {
            'buttons': [],
            'encoder': [],
        }
    }

    def __init__(self):
        self.config: dict | None = None
        self.on_context_changed: Event = Event[dict]()

        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.create_default()

    def create_default(self):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            json.dump(self.default_config, file, )
            self.config = self.default_config

    def save_config(self, ):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            json.dump(self.config, file)

    def add_app_context(self, context: dict):
        # TODO: Config validation or create dataclass for config
        self.config.update(context)
        self.save_config()
        self.on_context_changed.invoke(self.config)

    def __getitem__(self, item):
        return {**self.config[item]}


if __name__ == "__main__":
    conf = ConfigController()
    conf['Global']['buttons'] = {'aasdf': 'asdf'}
    conf.add_app_context({'Local': {}})
