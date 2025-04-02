
# Fun Fact Generator

A simple Python web app that generates fun facts using DeepSeek API and displays them on a web page.

## Features

- Random fun facts across 6 different topics
- Responsive UI using TailwindCSS
- Built with FastAPI

## Setup

### 1. Clone the repo and navigate into the folder

```bash
cd funfact_generator
```

### 2. Create a `.env` file

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 3. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

Then visit [http://localhost:8000](http://localhost:8000)

## Project Structure

```
.
├── config.py             # Loads and validates .env variables
├── fact_generator.py     # Core logic to interact with DeepSeek API
├── main.py               # FastAPI app with endpoints
├── requirements.txt      # Python dependencies
└── static/
    └── index.html        # Frontend UI
```
