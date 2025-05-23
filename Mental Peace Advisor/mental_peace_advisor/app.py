# import streamlit as st
# from model_api import get_bot_response
# from chat_ui import display_conversation
# import speech_recognition as sr

# st.title("Mental Peace Advisor Bot")

# lang = st.radio("Select Language / زبان منتخب کریں:", ("English", "اردو"))
# st.session_state.lang = 'en' if lang == "English" else 'ur'

# if "conversation" not in st.session_state:
#     st.session_state.conversation = []

# # Show conversation
# display_conversation(st.session_state.conversation)

# # Text input form
# with st.form("chat_form", clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Type your message here...")
#     submitted = st.form_submit_button("Send")

# if submitted:
#     if user_input.strip():
#         st.session_state.conversation.append(("user", user_input.strip()))
#         reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
#         st.session_state.conversation.append(("bot", reply))
#         display_conversation(st.session_state.conversation)
#     else:
#         st.warning("Please enter a message before submitting.")

# st.subheader("Or speak to the bot:")

# if st.button("Start Speaking"):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             user_input = recognizer.recognize_google(audio, language="ur-PK" if st.session_state.lang == 'ur' else "en-US")
#             st.success("Audio recognized successfully!")
#             st.write(f"You said: {user_input}")

#             st.session_state.conversation.append(("user", user_input.strip()))
#             reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
#             st.session_state.conversation.append(("bot", reply))

#             display_conversation(st.session_state.conversation)

#         except sr.UnknownValueError:
#             st.error("Sorry, I could not understand the audio.")
#         except sr.RequestError as e:
#             st.error(f"Could not request results; {e}")
#         except Exception as e:
#             st.error(f"Error: {e}")


import streamlit as st
from model_api import get_bot_response
from chat_ui import display_conversation
import speech_recognition as sr

st.title("Mental Peace Advisor Bot")

# Language display to code mapping
lang_map = {
    "English": "en",
    "اردو": "ur",
    "سندھی (Sindhi)": "sd",
    "پنجابی (Punjabi)": "pa",
    "中文 (Chinese)": "zh",
    "العربية (Arabic)": "ar",
    "Français (French)": "fr",
    "Español (Spanish)": "es",
    "Deutsch (German)": "de",
    "فارسی (Persian)": "fa",
    "Türkçe (Turkish)": "tr"
}

# Speech recognition language codes
LANGUAGE_CODES = {
    "en": "en-US",
    "ur": "ur-PK",
    "sd": "sd",       
    "pa": "pa-IN",    
    "zh": "zh-CN",    
    "ar": "ar-SA",    
    "fr": "fr-FR",
    "es": "es-ES",
    "de": "de-DE",
    "fa": "fa-IR",
    "tr": "tr-TR"
}

# Language selector
lang_display = st.radio("Select Language / زبان منتخب کریں:", list(lang_map.keys()))
selected_lang = lang_map[lang_display]
st.session_state.lang = selected_lang

if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Show conversation
display_conversation(st.session_state.conversation)

# Text input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted:
    if user_input.strip():
        st.session_state.conversation.append(("user", user_input.strip()))
        reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
        st.session_state.conversation.append(("bot", reply))
        display_conversation(st.session_state.conversation)
    else:
        st.warning("Please enter a message before submitting.")

st.subheader("Or speak to the bot:")

if st.button("Start Speaking"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            # Get correct language code
            lang_code = LANGUAGE_CODES.get(st.session_state.lang, "en-US")
            user_input = recognizer.recognize_google(audio, language=lang_code)
            st.success("Audio recognized successfully!")
            st.write(f"You said: {user_input}")

            st.session_state.conversation.append(("user", user_input.strip()))
            reply = get_bot_response(user_input.strip(), language=st.session_state.lang)
            st.session_state.conversation.append(("bot", reply))

            display_conversation(st.session_state.conversation)

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except Exception as e:
            st.error(f"Error: {e}")
