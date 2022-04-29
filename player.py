from datetime import date
from enum import Enum
from pydantic import BaseModel


class Gender(Enum):
    Mail = "H"
    Female = "F"


class Player(BaseModel):
    rank: int
    last_name: str
    birth_date: date
    first_name: str
    gender: Gender


player1 = Player(rank=12,
                 last_name="Joe",
                 birth_date="1979-04-23",
                 first_name="Amri",
                 gender="H")
print(player1)