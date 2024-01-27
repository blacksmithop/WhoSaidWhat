import spacy
from pydantic import BaseModel
from typing import List


nlp = spacy.load("en_core_web_sm")

class Person(BaseModel):
    name: str


class Identifier:

    def get_speakers(self, text: str) -> List[Person]:
        doc = nlp(text)
        names = [
            ent.text for ent in doc.ents if ent.label_ == "PERSON"
        ]
        speakers = [
            Person(name=name) for name in names
        ]
        return speakers
    

class Splitter:
    def get_paragraphs(self, text: str) -> List[str]:
        parts = text.split("\n")
        return parts