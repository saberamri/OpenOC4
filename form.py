from typing import  List
from view import View


class Form(View):
    """constructor
        Args:
        - title (str): form title
        - fields: list of fields to  fill
    """
    def __init__(self, title: str, fields: List[str]):
        super().__init__(title=title)
        self.fields = fields

    def show(self):
        """
        - show title and not the content
        - ask for fields to fill in
        Returns:
            data(dict): data dictionary filled with their real fields
        """
        data = {}
        super().show()
        for field in self.fields:
            data[field] = input(field + "? ")
        return data