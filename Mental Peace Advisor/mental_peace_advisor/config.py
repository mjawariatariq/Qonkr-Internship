# API key jo Google generative AI ko access karne ke liye chahiye
API_KEY = "AIzaSyCeGE1aiFRCbZjui8R8hcGijSShU5ajT3I"

# Model ka naam jo hum use kar rahe hain response generate karne ke liye
MODEL_NAME = 'gemini-2.5-flash-preview-04-17'

# Generation configuration jo model ko batata hai ke response kaisa hona chahiye
GEN_CONFIG = {
    "temperature": 0.5,             # Response mein creativity ka level (0.5 moderate hai)
    "response_mime_type": "text/plain"  # Response ka format plain text hona chahiye
}
