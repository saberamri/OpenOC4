from views.menu import Menu


class PlayerMenu(Menu):
    def __init__(self):
        super().__init__(title="Gérer les joueurs",
                         options=["Créer un joueur",
                                  "Editer le classement d'un joueur",
                                  "Afficher les joueurs par Nom",
                                  "Afficher les joueurs par classement",
                                  "Retour"])