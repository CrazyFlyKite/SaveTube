import json
import logging
from pathlib import Path


class DataManager:
    def __init__(self, path: Path = Path('SaveTube/data.json')):
        self.__path = path

    def load_preferences(self) -> dict:
        try:
            with open(self.__path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
            logging.error(f'{self.__path} not found!')
        except json.JSONDecodeError:
            data = {}
            logging.error(f'Cannot decode from {self.__path}!')

        return data

    def write_preferences(self, key: str, value: str = '') -> None:
        data = self.load_preferences()

        data[key] = value

        with open(self.__path, 'w') as file:
            json.dump(data, file, indent=2)
