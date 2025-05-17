import streamlit as st
from model_api import get_bot_response
from chat_ui import display_conversation

# App ka title set karna - screen par jo naam dikhayega wo yeh hoga
st.title("Mental Peace Advisor Bot")

# Session state mein 'conversation' naam ka list check karna agar maujood nahi to naya banayein
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Pehle se jo conversation chal rahi hai usko screen par dikhana
display_conversation(st.session_state.conversation)

# User input lene ke liye form create karna, form submit hone ke baad input clear ho jaye
with st.form("chat_form", clear_on_submit=True):
    # Text input field jahan user apna message type karega
    user_input = st.text_input("You:", key="chat_input", placeholder="Type your message here...")
    # Form submit karne ke liye button
    submitted = st.form_submit_button("Send")

# Agar user ne message bheja (submit kiya)
if submitted:
    # Check karna ke user ne kuch likha bhi hai ya sirf space hai
    if user_input.strip():
        # User ka message conversation list mein add karna
        st.session_state.conversation.append(("user", user_input.strip()))
        # Bot se reply lena jo model_api mein define hai
        reply = get_bot_response(user_input.strip())
        # Bot ka reply bhi conversation mein add karna
        st.session_state.conversation.append(("bot", reply))
    else:
        # Agar user ne kuch nahi likha to warning message dikhana
        st.warning("Please enter a message before submitting.")
