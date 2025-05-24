from feelbot.config.config import TURTLE_MODEL, TURTLE_TEMPERATURE
from feelbot.core.chat_runner import run_chat  # GPT通信共通関数
from .prompt import get_turtle_prompt

def generate_turtle(text: str) -> dict:
    prompt = get_turtle_prompt(text)

    try:
        content = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=TURTLE_MODEL,
            temperature=TURTLE_TEMPERATURE
        ).strip()

        lines = [line.strip() for line in content.splitlines() if line.strip()]

        return {
            "laozi_quote": lines[0] if len(lines) >= 1 else "",
            "murmur": lines[1:3] if len(lines) >= 3 else []
        }

    except Exception as e:
        return {
            "laozi_quote": f"[turtle error: {e}]",
            "murmur": ["[つぶやき生成エラー]"]
        }