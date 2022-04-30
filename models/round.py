from datetime import datetime
from typing import List
from pydantic import BaseModel

from models.match import Match


class Round(BaseModel):
    """
    The Round() class inherits from the BaseModel() class:it contains the elements of Round

    Args:
        BaseModel (class): This class contains the attributes and methods of round
    """
    name: str
    start_date: datetime
    end_date: datetime
    matchs: List[Match]