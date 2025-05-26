import re

def parse_moon(text: str) -> dict:
    """
    Parse the raw 6-line response from the 'Message from the Moon' v2 prompt into structured components.

    Expected format:
    1. > poetic insight in English
    2. > poetic insight in Japanese
    3. [moon_grounding_01] 心理学的には：...
    4. [moon_grounding_02] 別の観点：...
    5. > quiet reminder in English
    6. > quiet reminder in Japanese

    Returns:
    - dict with keys: poetic, grounding, reminder
    """

    # 空行除去
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    # poetic（末尾の句読点や余韻を残すため、lstripのみに）
    poetic_en = lines[0][1:] if len(lines) >= 1 and lines[0].startswith(">") else ""
    poetic_en = poetic_en.lstrip()

    poetic_ja = lines[1][1:] if len(lines) >= 2 and lines[1].startswith(">") else ""
    poetic_ja = poetic_ja.lstrip()

    # grounding（ラベル1回だけ許可）
    grounding_dict = {}
    for line in lines:
        match = re.match(r"\[moon_grounding_0([12])\]\s*(.+)", line)
        if match:
            label_num = match.group(1)
            content = match.group(2).strip()
            if label_num not in grounding_dict:
                grounding_dict[label_num] = content

    grounding_raw = [
        grounding_dict.get("1", "心理学的には：xxx"),
        grounding_dict.get("2", "別の観点：xxx")
    ]

    # reminder（末尾2行の `>` から抽出）
    quoted_lines = [line for line in lines if line.startswith(">")]
    reminder_en = quoted_lines[-2][1:] if len(quoted_lines) >= 4 else ""
    reminder_en = reminder_en.lstrip()

    reminder_ja = quoted_lines[-1][1:] if len(quoted_lines) >= 4 else ""
    reminder_ja = reminder_ja.lstrip()

    return {
        "poetic": {"en": poetic_en, "ja": poetic_ja},
        "grounding": grounding_raw,
        "reminder": {"en": reminder_en, "ja": reminder_ja}
    }
