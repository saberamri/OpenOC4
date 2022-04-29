from datetime import date, timedelta
from enum import Enum
from pydantic import BaseModel, PositiveInt, conint, constr


class Gender(Enum):
    """
    Gender is a class that inherits from the Enum class.
    Enum is a basic python module integrated into the language 
    it will enumerate the values of the gender variable.

    """
    Male = "H"
    Female = "F"


class Player(BaseModel):
    """
    The Player() class inherits from the BaseModel() class
    This class contains the attributes and methods of the player user.

    """
    id: PositiveInt
    rank: conint(strict=True, gt=0, le=3000)
    last_name: constr(strict=True, min_length=2, max_length=12)
    birth_date: date
    first_name: str
    gender: Gender


player1 = Player(id=42,
                 rank=30,
                 last_name="Joe",
                 birth_date="2020-04-23",
                 first_name="Amri",
                 gender="H")
print(player1)