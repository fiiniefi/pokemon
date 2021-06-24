from typing import List

from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: str
    moves: List[str]
