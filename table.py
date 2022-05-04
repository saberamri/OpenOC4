from typing import Any, List
from view import View


class Table(View):
    """structure the data display data
    Args:
        View (class): parent class
    """
    def __init__(self, title: str, cols: List[str], items: List[Any]):
        """
        constructor: calls the parent constructor to display title and content
        define content as generation in headers and cols.
        Args:
            title (str): table title
            cols (List[str]):list of table columns
            items (List[Any]): list of items of type Any
        """
        content = self.gen_headers(cols) + self.gen_lines(cols, items)
        super().__init__(title=title, content=content)
        self.cols = cols
        self.items = items

    def gen_headers(self, cols: List[str]):
        """generate uppercase and centered headers
        Args:
            cols (List[str]): headers
        Returns:
            headers: columns name
        """
        col_width = 18
        headers = ""
        for desc, _ in cols:
            headers += desc.upper().center(col_width)
        return headers + "\n"

    def gen_lines(self, cols: List[str], items: List[Any]):
        """generate row data with line break on each new row
        Args:
            items (List[Any]): list of items
        Returns:
            lines: data lines
        """
        col_width = 18
        lines = ""
        for item in items:
            for _, name in cols:
                lines += str(getattr(item, name)).center(col_width)
            lines += "\n"
        return lines