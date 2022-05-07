from views.menu import Menu


class MainMenu(Menu):
    def __init__(self):
        super().__init__(title="Bienvenue sur chess Manager version 1.0",
                     options=["Gérer les joueurs", "Gérer les tournois", "Quitter"])