import streamlit as st
from streamlit_chat import message
import google.generativeai as palm

# add a title to the app
st.title("Doreen Alchemist")

'''
She knows math and can answer pretty well on all kinds of questions ranging from the most complex Biological concepts to explaining the theory of quantuum super-positioning to a 5-year old. Please enjoy a conversation with her.
Meanwhile, she knows python :)
'''
if "message" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What question do you have for me to answer?"}]


# Create a form to send instructions to PaLM2 API
with st.form("chat_input", clear_on_submit=True):
    a , b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
        )

    b.form_submit_button("send", use_container_width=True)

# Make user input at the left side of the screen, so it looks like a chat app
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user") # display message on the screen

# configure Google's PALM API with your API Key and response from the API
if user_prompt and palm_api_key:
    palm.configure(api_key=palm_api_key)

    st.session_state.messages.append({"role": "user", "content": user_prompt})

    message(user_prompt, is_user=True)

    response = palm.chat(messages=[user_prompt]) # get response from Google's PaLM API

    msg = {"role": "assistant", "content": response.last}

    st.session_state.messages.append(msg) # add message to the chat history

    message(msg["content"]) # display message on the screen

# Optionally, implement function to clear the chat history:
def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]
    if len(st.session_state.messages) > 1:
        st.button('Clear Chat', on_click=clear_chat)
