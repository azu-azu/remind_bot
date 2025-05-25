def parse_moon(text: str) -> dict:
    """
    Parse the raw string returned from the GPT Moon prompt into structured parts.

    Expected format:
    - Lines starting with '>': poetic + reminder (first 2 = poetic, last 2 = reminder)
    - Lines starting with [moon_grounding_01], [moon_grounding_02]: grounding entries

    Returns:
    - dict with keys: poetic, grounding, reminder
    """

    # 前処理：空行・空白を除去
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    # > 行の抽出（Poetic + Reminder）
    quoted_lines = [l for l in lines if l.startswith(">")]

    poetic_en = quoted_lines[0][1:].strip() if len(quoted_lines) >= 4 else ""
    poetic_ja = quoted_lines[1][1:].strip() if len(quoted_lines) >= 4 else ""
    reminder_en = quoted_lines[2][1:].strip() if len(quoted_lines) >= 4 else ""
    reminder_ja = quoted_lines[3][1:].strip() if len(quoted_lines) >= 4 else ""

    # grounding抽出（prefixのみ除去。見出しは付けない）
    grounding_raw = [
        l for l in lines
        if l.startswith("[moon_grounding_01]") or l.startswith("[moon_grounding_02]")
    ]

    grounding_formatted = []
    for line in grounding_raw:
        if line.startswith("[moon_grounding_01]"):
            content = line.removeprefix("[moon_grounding_01]").strip()
            grounding_formatted.append(content)
        elif line.startswith("[moon_grounding_02]"):
            content = line.removeprefix("[moon_grounding_02]").strip()
            grounding_formatted.append(content)
        else:
            grounding_formatted.append(line) # fallback（想定外ラベルはそのまま）

    return {
        "poetic": {"en": poetic_en, "ja": poetic_ja},
        "grounding": grounding_formatted,
        "reminder": {"en": reminder_en, "ja": reminder_ja}
    }
