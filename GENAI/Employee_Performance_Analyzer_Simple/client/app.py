"""
Simple API client example.

Run the FastAPI server first:
    python sample_app.py

Then run this file in another terminal:
    python client/app.py
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/")

print("Status:", response.status_code)
print("Response:", response.json())
