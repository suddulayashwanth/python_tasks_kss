# ============================================================
# 🚀 FastAPI + Gemini API (With Try Except)
# ============================================================

# Install Required Packages:
# pip install fastapi uvicorn google-genai python-dotenv

import os
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

MODEL_NAME = "gemini-3-flash-preview"

# ============================================================
# Request Body Schema
# ============================================================

class QuestionRequest(BaseModel):
    question: str

# ============================================================
# API Endpoint
# ============================================================

@app.post("/ask")
def ask_question(data: QuestionRequest):

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=data.question,
        )

        return {
            "success": True,
            "question": data.question,
            "response": response.text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

# ============================================================
# Run Server
# ============================================================

# Command:
# uvicorn app:app --reload