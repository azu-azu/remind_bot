from feelbot.config.config import MOON_MODEL, MOON_TEMPERATURE
from feelbot.core.chat_runner import run_chat
from .prompt import get_moon_prompt
from .parser import parse_moon


def generate_moon(text: str) -> dict:
    """
    Run the GPT model to generate a Moon message based on the given emotional log text.
    The output is parsed by `parse_moon()` to extract structured content.
    """
    prompt = get_moon_prompt(text)

    try:
        raw = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=MOON_MODEL,
            temperature=MOON_TEMPERATURE
        ).strip()

        return parse_moon(raw)

    except Exception as e:
        return {
            "poetic": {"en": f"[moon error: {e}]", "ja": "xxx"},
            "grounding": [
                "心理学的には：xxx",
                "別の観点：xxx"
            ],
            "reminder": {"en": "", "ja": ""}
        }
