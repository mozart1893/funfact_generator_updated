import os
import random
import requests
from dotenv import load_dotenv

# Load configuration
load_dotenv()
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

def generate_facts():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Create topic selection with possible repeats
    selected_topics = [random.choice(TOPICS) for _ in range(6)]

    prompt = f"""Generate 6 fun facts with these requirements:
    1. One fact per line
    2. Format: "Topic: Fact text"
    3. Topics in this order: {', '.join(selected_topics)}
    4. Make facts surprising but accurate
    5. Include emojis where appropriate
    6. Max 20 words per fact"""

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful facts assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        facts = response.json()["choices"][0]["message"]["content"].split("\n")
        return [fact.strip() for fact in facts if fact.strip()]
    
    except Exception as e:
        print(f"Error fetching facts: {str(e)}")
        return None

def display_facts(facts):
    print("\n📚 Today's 6 Random Fun Facts:\n")
    for i, fact in enumerate(facts[:6], 1):
        print(f"{i}. {fact}")
    print("\n🌟 Learn something new every day!")

if __name__ == "__main__":
    print("🔍 Fetching fun facts...")
    facts = generate_facts()
    
    if facts:
        display_facts(facts)
    else:
        print("Failed to retrieve facts. Please try again later.")