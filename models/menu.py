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
        content = "\n".join(options)
        super().__init__(title=title, content=content)
