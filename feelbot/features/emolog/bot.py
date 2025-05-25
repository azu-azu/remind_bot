import json
from feelbot.config.config import EMOLOG_MODEL, EMOLOG_TEMPERATURE
from feelbot.core.chat_runner import run_chat
from .prompt import get_emolog_prompt
from .parser import parse_emolog  # ← ✅ 追加

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
                "content": get_emolog_prompt()
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
    return parse_emolog(data)  # ← ✅ 呼び出しだけに
