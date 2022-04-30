from datetime import datetime
from typing import List
from pydantic import BaseModel, PositiveInt, constr


class Tournament(BaseModel):
    """The Tournament() class inherits from the BaseModel() class
    This class contains the attributes and methods of the tournament user.

    Args:
        BaseModel (class): This class contains the attributes and methods of the tournament
    """
    id: PositiveInt
    name: constr(strict=True, min_length=2, max_length=25)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    place: constr(strict=True, min_length=2, max_length=10)
    number_of_rounds: PositiveInt = 4
    description: constr(strict=True, max_length=50) = ""
    players: List[PositiveInt]
    timeconrol: int
