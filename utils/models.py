from pydantic import BaseModel
from typing import List


class Speaker(BaseModel):
    name: str


class Dialogue(BaseModel):
    text: str
    speakers: List[Speaker]
    speech: str

