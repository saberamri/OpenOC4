from main_menu import MainMenu
from player_menu import PlayerMenu
from views.menu import Menu


def main():
    """principal controller
    """
    # Menu(title="Bienvenue sur chess Manager version 1.0",
    #      options=["Gérer les joueurs", "Gérer les tournois"]).show()
    choice = MainMenu().show()
    match choice:
        case 1:
            PlayerMenu().show()
        case 2:
            TournamentMenu().show()

main()