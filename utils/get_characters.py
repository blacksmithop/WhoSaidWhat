import spacy
from pydantic import BaseModel
from typing import List
from utils.models import Speaker

nlp = spacy.load("en_core_web_sm")



class Identifier:
    all_speakers: List[Speaker] = []
    
    def get_speakers(self, text: str) -> List[Speaker]:
        doc = nlp(text)
        # for ent in doc.ents:
        #     print(ent, ent.label_)
        names = [
            ent.text for ent in doc.ents if ent.label_ in ("PERSON", "GPE")
        ]
        print("Names", names)
        unique_names = list(set(names))
        speakers = [
            Speaker(name=name) for name in unique_names
        ]
        self.update_speakers(speakers=speakers)
        return speakers
    
    def update_speakers(self, speakers):
        self.all_speakers.extend(speakers)


class Splitter:
    def get_sentences(self, text: str) -> List[str]:
        doc = nlp(text)
        sentences = [str(sent.text) for sent in doc.sents]
        return sentences