from typing import  List
from view import View


class Form(View):
    def __init__(self, title: str, fields: List[str]):
        super().__init__(title=title)
        self.fields = fields

    def show(self):
        """
        - show title and not the content
        - ask for fields to fill in
        """
        super().show()
        for field in self.fields:
            input(field + "? ")