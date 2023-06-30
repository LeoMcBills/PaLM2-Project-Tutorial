import streamlit as st
from streamlit_chat import message
import google.generativeai as palm

# add a title to the app
st.title("McBills")

'''
Initial message

Initialize message
'''
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "Say something to get started!"}]


# Create a form to send instructions to PaLM2 API
with st.form("chat_input", clear_on_submit=True):
    a , b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
        )

        b.form_submit_button("send", use_container_width=True)
