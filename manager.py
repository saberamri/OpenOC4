import json
from typing import Any
from pydantic import BaseModel

from models.player import Player


class Manager:

    def __init__(self, item_type: Any):
        self.item_type = item_type
        self.items = {}
        self.load_from_jason()

    def load_from_jason(self, path: str):
        with open(path) as json_data:
            data_dict = json.load(json_data)
            for item_data in data_dict:
                item = Player(**item_data)
                item = self.items[item.id]