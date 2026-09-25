import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Create a .env file and add your Gemini API key."
    )

client = genai.Client(api_key=api_key)
