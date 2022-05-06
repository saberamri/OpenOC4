from menu import Menu


def main():
    """principal controller
    """
    Menu(title="Bienvenue sur chess Manager version 1.0",
         options=["Gérer les joueurs", "Gérer les tournois"]).show()


main()