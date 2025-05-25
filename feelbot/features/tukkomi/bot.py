from feelbot.config.config import TUKKOMI_MODEL, TUKKOMI_TEMPERATURE, MAX_TUKKOMI_COUNT
from feelbot.core.chat_runner import run_chat
from .prompt import get_tukkomi_prompt
from .parser import parse_tukkomi

def generate_tukkomi(text: str) -> list[str]:
    prompt = get_tukkomi_prompt(text, MAX_TUKKOMI_COUNT)

    try:
        content = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=TUKKOMI_MODEL,
            temperature=TUKKOMI_TEMPERATURE
        )

        return parse_tukkomi(content)

    except Exception as e:
        return [f"ツッコミ生成エラー: {e}"]
