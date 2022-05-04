from form import Form
from manager import Manager
from menu import Menu
from models.player import Player
from table import Table

# view = View(title="title 1",
#             content= "content1")
# print(view.show())

# Menu(title="Bienvenue sur chess manager version 1.0",
#      options=["Gérer les joueurs", "Gérer les tournois"]).show()

# print(Form(title="Ajouter un joueur", fields=[("Nom", "Last_name", str),
#                                         ("prénom", "First_name", str),
#                                         ("année de naissance", "birth_date_year", int),
#                                         ("sexe", "gender", str),
#                                         ("classement", "rank", int)]).show())

player_manager = Manager(item_type=Player)
player_manager.load_from_jason("./Jason/players.json")

Table(title="liste des joueurs",
      cols=["id", "nom", "prénom", "classement"],
      items=player_manager.items)