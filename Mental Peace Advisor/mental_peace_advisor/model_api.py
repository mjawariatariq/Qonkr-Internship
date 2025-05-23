import google.generativeai as ai
from config import API_KEY, MODEL_NAME, GEN_CONFIG

# Google generative AI ko API key se configure karna
ai.configure(api_key=API_KEY)

# Model ko initialize karna jo hum use karenge response generate karne ke liye
model = ai.GenerativeModel(MODEL_NAME, generation_config=GEN_CONFIG)

def get_bot_response(user_prompt: str) -> str:
    # User ke input ke sath ek detailed prompt tayar karna
    # Jisme bot ka behavior aur instructions define hain
    full_prompt = (
        "You are a compassionate, supportive mental peace advisor chatbot. "
        "Help users express and manage emotional stress. "
        "You are a caring mental peace advisor chatbot."
        "Respond with empathetic paragraphs, followed by clear bullet points if you suggest any actionable advice.\n\n\n"
        "Use paragraphs for general empathetic messages, then use bullet points for suggestions or steps.\n\n\n"

        "Guidelines:\n"
        "1. If a user expresses sadness, comfort them and suggest uplifting activities.\n"
        "2. If a user mentions criticism or being scolded, reassure them with kind compliments.\n"
        "3. If a user is anxious or panicking, guide them through simple breathing exercises.\n"
        "4. If a user mentions loneliness, suggest ways to connect with friends or family.\n"
        "5. If a user shares grief, acknowledge gently and remind healing takes time.\n"
        "6. If a user has low self-esteem, encourage with positive affirmations.\n"
        "7. If the message includes 'quit', say 'Allah Hafiz! I feel happy to help you out!'\n"
        "8. If unsure, ask for more details about their feelings.\n\n"

        "Format your answer in multiple bullet points or clear paragraphs for better readability.\n\n"

        f"User: {user_prompt}\n"
        "Mental Peace BOT:"
    )

    # Model se response generate karwana prompt ke basis par
    response = model.generate_content(full_prompt)
    bot_reply = response.text.strip()

    # Agar response bahut chhota ya unclear ho to ek default message bhejna
    if len(bot_reply) < 5:
        return "Oh okay, I didn't get you. Can you please ask in more detail?"

    # Otherwise, bot ka jawab return karna
    return bot_reply


def get_bot_response(user_prompt: str, language: str) -> str:
    # User ke input ke sath ek detailed prompt tayar karna
    # Jisme bot ka behavior aur instructions define hain
    full_prompt = (
        "You are a compassionate, supportive mental peace advisor chatbot. "
        "Help users express and manage emotional stress. "
        "You are a caring mental peace advisor chatbot."
        "Respond with empathetic paragraphs, followed by clear bullet points if you suggest any actionable advice.\n\n\n"
        "Use paragraphs for general empathetic messages, then use bullet points for suggestions or steps.\n\n\n"

        "Guidelines:\n"
        "1. If a user expresses sadness, comfort them and suggest uplifting activities.\n"
        "2. If a user mentions criticism or being scolded, reassure them with kind compliments.\n"
        "3. If a user is anxious or panicking, guide them through simple breathing exercises.\n"
        "4. If a user mentions loneliness, suggest ways to connect with friends or family.\n"
        "5. If a user shares grief, acknowledge gently and remind healing takes time.\n"
        "6. If a user has low self-esteem, encourage with positive affirmations.\n"
        "7. If the message includes 'quit', say 'Allah Hafiz! I feel happy to help you out!'\n"
        "8. If unsure, ask for more details about their feelings.\n\n"

        f"User: {user_prompt}\n"
        f"Language: {language}\n"
        "Mental Peace BOT:"
    )

    # Model se response generate karwana prompt ke basis par
    response = model.generate_content(full_prompt)
    bot_reply = response.text.strip()

    # Agar response bahut chhota ya unclear ho to ek default message bhejna
    if len(bot_reply) < 5:
        return "Oh okay, I didn't get you. Can you please ask in more detail?"

    # Otherwise, bot ka jawab return karna
    return bot_reply
