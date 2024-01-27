import streamlit as st
from annotated_text import annotated_text, annotation
from typing import List


def get_annotated_speech(text: str, speakers: List[str], speech: str):

    speaker_hash = {}
    spk_no, speech_no = 0, 0

    speech_hash = {}
    fake_speech = f"SPEECH#{speech_no}"
    text = text.replace(speech, fake_speech)
    speech_hash[fake_speech] = speech
    
    for speaker in speakers:
        fake_speaker = f"SPEAKER#{spk_no}"
        spk_no += 1
        text = text.replace(speaker, fake_speaker)
        speaker_hash[fake_speaker] = speaker

    words = text.split()

    result = []
    for word in words:
        cleaned_word = word.strip(",.!#?\"")

        if cleaned_word in speech_hash:
            mapping = speech_hash[cleaned_word]
            entry = annotation(mapping, "Speech", font_family="Comic Sans MS", border="2px dashed red")
        elif cleaned_word in speaker_hash:
            mapping = speaker_hash[cleaned_word]
            entry = annotation(mapping, "Person", font_family="Comic Sans MS", border="2px dashed red")
        else:
            entry = f"{word} "

        result.append(entry)

    return annotated_text(*result)