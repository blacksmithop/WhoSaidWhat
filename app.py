import streamlit as st
import random
import time
from utils.stream_messages import stream_chat
from utils.models import Dialogue
from utils.handler import get_speech_data
from utils.get_annotated_text import get_annotated_speech
from typing import List

st.title("Identify Speakers from text")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Give me a conversation"):
    # Add user message to chat history
    # Display user message in chat message container
    with st.chat_message("user"):
        user_message = st.empty()
        # st.markdown(prompt)
        for i in stream_chat(text=prompt, obj_ref=user_message):
            pass
        user_message.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response: List[Dialogue] = get_speech_data(text=prompt)
        for item in response:

            st.markdown("#### Text")
            assistant_message_text = st.empty()
            assistant_response = item.text
            # Simulate stream of response with milliseconds delay
            for i in stream_chat(text=assistant_response, obj_ref=assistant_message_text):
                pass
            assistant_message_text.markdown(assistant_response)

            speakers = item.speakers
            if speakers:
                speakers = [i.name for i in speakers]
            st.markdown(f"> Speakers: \n{', '.join(speakers)}")
            st.divider()

            st.markdown("#### Dialogue")
            assistant_response = item.speech

            assistant_dialogue_speech = st.empty()
            # Simulate stream of response with milliseconds delay
            for i in stream_chat(text=assistant_response, obj_ref=assistant_dialogue_speech):
                pass
            assistant_dialogue_speech.markdown(assistant_response)
            st.divider()

            st.markdown("#### Annotation")
            get_annotated_speech(text=prompt, speakers=speakers, speech=assistant_response)
            st.divider()

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

