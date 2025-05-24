import json
from config.config import EMOLOG_MODEL, EMOLOG_TEMPERATURE, MAX_HONEST_COUNT
from .prompt import get_emolog_prompt
from core.chat_runner import run_chat

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
                "content": get_emolog_prompt(max_honest=MAX_HONEST_COUNT)
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

    return {
        "whats_on_my_mind": {
            "en": data.get("whats_on_my_mind", {}).get("en", ""),
            "ja": data.get("whats_on_my_mind", {}).get("ja", "")
        },
        "honest_voice": data.get("honest_voice", [])[:MAX_HONEST_COUNT],
        "tags": {
            "en": data.get("tags", {}).get("en", []),
            "ja": data.get("tags", {}).get("ja", [])
        }
    }