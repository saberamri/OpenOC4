from typing import List
from view import View


class Form(View):
    def __init__(self, title: str, fields: List[str]):
        super().__init__(title=title)
        self.fields = fields

    def show():
        super().show()