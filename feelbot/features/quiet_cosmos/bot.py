from feelbot.config.config import QUIET_COSMOS_MODEL, QUIET_COSMOS_TEMPERATURE
from feelbot.core.chat_runner import run_chat
from .prompt import get_quiet_cosmos_prompt
from .parser import parse_quiet_cosmos

def generate_quiet_cosmos(theme: str) -> dict:
    prompt = get_quiet_cosmos_prompt(theme)

    try:
        response = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=QUIET_COSMOS_MODEL,
            temperature=QUIET_COSMOS_TEMPERATURE
        ).strip()

        return parse_quiet_cosmos(response)

    except Exception as e:
        return {
            "fact": f"[quiet cosmos error: {e}]",
            "interpretation": "宇宙がちょっと迷子になったみたい。"
        }
