import json
from pydantic import BaseModel

from models.player import Player


class Manager:

    def __init__(self):
        pass

    def load_frm_jason(self, path: str):
        with open(path) as json_data:
            data_dict = json.load(json_data)
            ls = []
            for item_data in data_dict:
                item = Player(**item_data)
                ls.append(item)