from bots.config.config import TURTLE_MODEL, TURTLE_TEMPERATURE
from bots.core.chat_runner import run_chat
from .prompt import get_turtle_prompt
from .parser import parse_turtle

def generate_turtle(text: str) -> dict:
    prompt = get_turtle_prompt(text)

    try:
        content = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=TURTLE_MODEL,
            temperature=TURTLE_TEMPERATURE
        ).strip()

        return parse_turtle(content)

    except Exception as e:
        return {
            "laozi_quote": f"[turtle error: {e}]",
            "murmur": ["[つぶやき生成エラー]"]
        }
