from manager import Manager
from models.player import Player


player_manager = Manager(item_type=Player)
player_manager.load_from_jason("./Jason/players.json")
print(player_manager.items)