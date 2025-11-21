import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

def ask_groq(question):
    if not GROQ_API_KEY:
        return "Error: API key not set."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print("DEBUG: Raw API response:", data)  # <-- Add this to see what API returns

        # Adjusted for Groq API response
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return "No response from Groq API."
    except Exception as e:
        return f"Error: {e}"
