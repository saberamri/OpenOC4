from typing import List
from view import View


class Menu(View):
    """The Menu class contains two attrributes:
    - title
    - options
    and contain a show class method overloaded from the parent class view().

    Args:
        View (class): parent class
    """
    def __init__(self, title: str, options: List[str]):
        """constructor
        Args:
            title (str): title
            options (List[str]): options list
        """
        content = "\n".join([f"{i}.  {option}" for i, option in enumerate(options, start=1)])
        super().__init__(title=title, content=content)

    def show(self):
        super().show()
        while True:
            choice = input(":? ")
            try:
                return int(choice)
            except ValueError:
                print("entrer un choix numérique")
