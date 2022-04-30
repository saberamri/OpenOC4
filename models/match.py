from pydantic import BaseModel, PositiveInt


class Match(BaseModel):
    """
    The Match() class inherits from the BaseModel() class:it contains the elements of Match

    Args:
        BaseModel (class): This class contains the attributes and methods of match
    """
    player1_id: PositiveInt
    player2_id: PositiveInt
    score_player1: float
