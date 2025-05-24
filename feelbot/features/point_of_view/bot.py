from feelbot.config.config import POV_MODEL, POV_TEMPERATURE
from feelbot.core.chat_runner import run_chat
from .prompt import get_point_of_view_prompt

# --- GPTの出力を構造的に分解する関数 ---
def parse_point_of_view(text: str) -> dict:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    en = lines[0] if len(lines) >= 3 else ""
    ja = lines[1] if len(lines) >= 3 else ""
    source = lines[2] if len(lines) >= 3 else ""

    return {
        "en": en,
        "ja": ja,
        "source": source
    }

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