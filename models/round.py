from datetime import datetime
from typing import List
from pydantic import BaseModel

from models.match import Match


class Round(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    matchs: List[Match]