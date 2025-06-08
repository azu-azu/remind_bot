# gptを使うときはここを呼び出す
import os
from dotenv import load_dotenv
from openai import OpenAI
from bots.config.config import DEFAULT_MODEL, DEFAULT_TEMPERATURE

load_dotenv(dotenv_path="bots/config/.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_chat(messages, model=DEFAULT_MODEL, temperature=DEFAULT_TEMPERATURE) -> str:
    """
    Call OpenAI Chat API and return the plain message content.
    - model and temperature can be overridden by caller
    - defaults are defined in config.py
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print("🛑 GPT API Error:", e)
        return ""