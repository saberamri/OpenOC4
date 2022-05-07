from views.menu import Menu


class TournmanetMenu(Menu):
    def __init__(self):
        super().__init__(title="Gérer les tournois",
                         options=["Créer un tournois",
                                  "Reprendre un tournois",
                                  "Afficher les rapports d'un tournois",
                                  "Retour"])