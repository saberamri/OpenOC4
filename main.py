from main_menu import MainMenu
from player_menu import PlayerMenu
from tournament_menu import TournmanetMenu


def main():
    """principal controller
    """
    # Menu(title="Bienvenue sur chess Manager version 1.0",
    #      options=["Gérer les joueurs", "Gérer les tournois"]).show()
    choice = MainMenu().show()
    match choice:
        case 1:
            choice = PlayerMenu().show()
            match choice:
                case 5:
                    main()
        case 2:
            TournmanetMenu().show()

main()