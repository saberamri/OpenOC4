from datetime import date, timedelta
from enum import Enum
from pydantic import BaseModel, PositiveInt, conint, constr, validator


class Gender(Enum):
    """
    Gender is a class that inherits from the Enum class.
    Enum is a basic python module integrated into the language 
    it will enumerate the values of the gender variable.

    """
    Male = "H"
    Female = "F"

    def __str__(self):
        """display the values or names of the categories of the Gender() class
        Returns:
            names or values of the Gender catégories
        """
        # return self.value
        return self.name


class Player(BaseModel):
    """
    The Player() class inherits from the BaseModel() class
    This class contains the attributes and methods of the player user.

    """
    id: PositiveInt
    rank: conint(strict=True, gt=0, le=3000)
    last_name: constr(strict=True, min_length=2, max_length=20)
    birth_date: date
    first_name: constr(strict=True, min_length=2, max_length=20)
    gender: Gender

    @validator("birth_date")
    def check_age(cls, v):
        """verify that participants are at least 18 years old.
            Args:
                v (date): date of birth of participants.
            Raises:
                ValueError: the age of the participants is under 18.
            Returns:
                v: birth date of participant.
        """
        age = (date.today() - v) // timedelta(days=365.2425)
        if age < 18:
            raise ValueError('age must be > 18')
        return v

    def __str__(self):
        """
        present just name and first name of the players
        -It is useful when we are going to select the 
         players for a tournament.
        """
        return f"{self.last_name.upper()}, {self.first_name.capitalize()}"

