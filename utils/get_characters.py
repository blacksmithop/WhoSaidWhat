import spacy
from pydantic import BaseModel
from typing import List
from utils.models import Speaker

nlp = spacy.load("en_core_web_sm")



class Identifier:

    def get_speakers(self, text: str) -> List[Speaker]:
        doc = nlp(text)
        # for ent in doc.ents:
        #     print(ent, ent.label_)
        names = [
            ent.text for ent in doc.ents if ent.label_ in ("PERSON", "GPE")
        ]
        unique_names = list(set(names))
        speakers = [
            Speaker(name=name) for name in unique_names
        ]
        return speakers
    

class Splitter:
    def get_paragraphs(self, text: str) -> List[str]:
        parts = text.split("\n\n")
        return parts