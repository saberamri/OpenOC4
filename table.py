from typing import Any
from view import View


class Table(View):
    """structure the data display data
    Args:
        View (class): parent class
    """
    def __init__(self, title: str, cols: str, items: Any):
        super().__init__(title)
        self.cols = cols
        self.items = items