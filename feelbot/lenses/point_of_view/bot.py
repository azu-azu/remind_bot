from feelbot.config.config import POV_MODEL, POV_TEMPERATURE
from feelbot.core.runtime.chat_runner import run_chat
from .prompt import get_point_of_view_prompt
from .parser import parse_point_of_view

# --- Point of View を生成するメイン関数 ---
def generate_point_of_view(text: str) -> dict:
    prompt = get_point_of_view_prompt(text)

    try:
        raw = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=POV_MODEL,
            temperature=POV_TEMPERATURE
        ).strip()

        return parse_point_of_view(raw)

    except Exception as e:
        return {
            "en": "",
            "ja": "",
            "source": f"[point_of_view error: {e}]"
        }
