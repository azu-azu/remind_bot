from config.config import MOON_MODEL, MOON_TEMPERATURE
from core.chat_runner import run_chat
from .prompt import get_moon_prompt

# --- GPTの応答を構造的に分解する関数 ---
def parse_moon_message(text: str) -> dict:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    # > がついた行だけを抽出
    quoted_lines = [l for l in lines if l.startswith(">")]

    # poetic insight（先頭2行）と final reminder（末尾2行）を分離
    poetic_en = quoted_lines[0][1:].strip() if len(quoted_lines) >= 4 else ""
    poetic_ja = quoted_lines[1][1:].strip() if len(quoted_lines) >= 4 else ""
    reminder_en = quoted_lines[2][1:].strip() if len(quoted_lines) >= 4 else ""
    reminder_ja = quoted_lines[3][1:].strip() if len(quoted_lines) >= 4 else ""

    # grounding：plain promptに従い、心理学的には／別の観点 のみ抽出
    grounding = [
        l for l in lines if (
            l.startswith("心理学的には：") or
            l.startswith("別の観点：")
        )
    ]

    return {
        "poetic": {"en": poetic_en, "ja": poetic_ja},
        "grounding": grounding,
        "reminder": {"en": reminder_en, "ja": reminder_ja}
    }

# --- Moonメッセージを生成するメイン関数 ---
def generate_moon(text: str) -> dict:
    prompt = get_moon_prompt(text)

    try:
        raw = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=MOON_MODEL,
            temperature=MOON_TEMPERATURE
        ).strip()

        return parse_moon_message(raw)

    except Exception as e:
        return {
            "poetic": {"en": f"[moon error: {e}]", "ja": ""},
            "grounding": [],
            "reminder": {"en": "", "ja": ""}
        }