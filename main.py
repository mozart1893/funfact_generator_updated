# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import os
import random
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"
TOPICS = [
    "Artificial Intelligence",
    "Emerging Technology",
    "World Politics",
    "Sports",
    "Health and Wellness",
    "Entertainment"
]

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response schema
class FactResponse(BaseModel):
    facts: list[str]

@app.get("/", response_class=HTMLResponse)
def serve_homepage():
    return FileResponse("static/index.html")

@app.get("/generate", response_model=FactResponse)
def generate_facts():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    selected_topics = [random.choice(TOPICS) for _ in range(6)]

    prompt = f"""Generate 6 fun facts with these requirements:
    1. One fact per line
    2. Format: "Topic: Fact text"
    3. Topics in this order: {', '.join(selected_topics)}
    4. Make it short, surprising, and accurate
    """

    body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, json=body, headers=headers)
    response.raise_for_status()

    raw_text = response.json()["choices"][0]["message"]["content"]
    facts = [line.strip() for line in raw_text.split("\n") if line.strip()]

    return {"facts": facts}
