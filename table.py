from typing import Any, List
from view import View


class Table(View):
    """structure the data display data
    Args:
        View (class): parent class
    """
    def __init__(self, title: str, cols: List[str], items: List[Any]):
        content = self.gen_headers(cols) + self.gen_lines(items)
        super().__init__(title=title, content=content)
        self.cols = cols
        self.items = items

    def gen_headers(self, cols: List[str]):
        """generate headers
        Args:
            cols (List[str]): headers
        Returns:
            headers: columns name
        """
        pass

    def gen_lines(self, items: List[Any]):
        """generate lines
        Args:
            items (List[Any]): list of items
        Returns:
            lines: data lines
        """
        pass