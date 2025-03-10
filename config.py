from dotenv import load_dotenv
import os

load_dotenv()

def validate_config():
    if not os.getenv("DEEPSEEK_API_KEY"):
        raise ValueError("Missing DEEPSEEK_API_KEY in .env file")