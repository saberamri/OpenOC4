from typing import List
from view import View


class Menu(View):
    def __init__(self, title: str, options: List[str]):
        self.options = options
        content = "\n".join(options)
        super().__init__(title=title, content=content)