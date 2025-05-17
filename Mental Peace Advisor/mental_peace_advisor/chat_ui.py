import streamlit as st
from formatting import format_bot_message_html

def display_conversation(conversation):
    """
    Yeh function conversation history ko screen par dikhata hai.
    User ke messages right side align hote hain,
    aur bot ke messages left side aligned hote hain styling ke sath.
    """
    for sender, msg in conversation:
        if sender == "user":
            # Agar sender user hai to message right align karke blue background mein dikhayen
            st.markdown(
                f'<p style="text-align:right; background:#d0e7ff; padding:8px 12px; '
                f'border-radius:10px; max-width:75%; margin-left:auto; font-weight:bold;">You: {msg}</p>',
                unsafe_allow_html=True
            )
        else:
            # Agar sender bot hai to message ko pehle format karen phir left align karke green background mein dikhayen
            formatted_msg = format_bot_message_html(msg)
            st.markdown(
                f'<div style="text-align:left; background:#d4edda; padding:8px 12px; '
                f'border-radius:10px; max-width:75%; margin-right:auto; font-weight:bold;">'
                f'<strong>Mental Peace BOT:</strong><br>{formatted_msg}</div>',
                unsafe_allow_html=True
            )
