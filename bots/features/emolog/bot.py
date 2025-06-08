import json
from bots.config.config import EMOLOG_MODEL, EMOLOG_TEMPERATURE, MAX_HONEST_COUNT
from bots.core.runtime.chat_runner import run_chat
from .prompt import get_emolog_prompt
from .parser import parse_emolog

def call_openai_json(messages, model, temperature):
    try:
        raw = run_chat(messages, model=model, temperature=temperature)
        return json.loads(raw)
    except json.JSONDecodeError:
        print("🛑 GPT JSON decode error")
        return {}

def generate_emolog(text: str) -> dict:
    def create_prompt():
        return [
            {
                "role": "system",
                "content": get_emolog_prompt(MAX_HONEST_COUNT)
            },
            {
                "role": "user",
                "content": f"""
                    Please analyze the following emotional log and return a JSON response:

                    Text:
                    {text}
                """
            }
        ]

    data = call_openai_json(create_prompt(), EMOLOG_MODEL, EMOLOG_TEMPERATURE)
    return parse_emolog(data, max_honest=MAX_HONEST_COUNT)
