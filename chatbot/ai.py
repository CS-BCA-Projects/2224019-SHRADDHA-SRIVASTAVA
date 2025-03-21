import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
MODEL_NAME = "gemini-1.5-pro"

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
