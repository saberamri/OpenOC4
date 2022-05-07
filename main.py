from main_menu import MainMenu
from player_menu import PlayerMenu
from tournament_menu import TournmanetMenu


def players():
    choice = PlayerMenu().show()
    match choice:
        case 5:
            main()


def tournaments():
    choice = TournmanetMenu().show()
    match choice:
        case 4:
            main()


def main():
    """principal controller
    """
    choice = MainMenu().show()
    match choice:
        case 1:
            players()
        case 2:
            tournaments()


main()