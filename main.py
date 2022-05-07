from main_menu import MainMenu
from player_form import PlayerForm
from player_menu import PlayerMenu
from tournament_menu import TournmanetMenu


def players():
    choice = PlayerMenu().show()
    match choice:
        case 1:
            add_players()
        case 5:
            main()


def add_players():
    form_data = PlayerForm().show()
    players()


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