from typing import Any, List
from view import View


class Table(View):
    """structure the data display data
    Args:
        View (class): parent class
    """
    def __init__(self, title: str, cols: List[str], items: List[Any]):
        super().__init__(title)
        self.cols = cols
        self.items = items