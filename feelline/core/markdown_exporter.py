from datetime import datetime

def export_markdown(log: dict) -> str:
    """
    Export the structured log as fujiko-style markdown text.
    """
    date_str = log.get("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    mind_en = log.get("whats_on_my_mind", {}).get("en", "")
    mind_ja = log.get("whats_on_my_mind", {}).get("ja", "")

    tags_en = log.get("tags", {}).get("en", [])
    tags_ja = log.get("tags", {}).get("ja", [])

    honest_voice = log.get("honest_voice", [])
    tukkomi = log.get("tukkomi", [])

    point_of_view = log.get("point_of_view", "")

    moon = log.get("moon", {})
    poetic_en = moon.get("poetic", {}).get("en", "")
    poetic_ja = moon.get("poetic", {}).get("ja", "")
    grounding = moon.get("grounding", [])
    reminder_en = moon.get("reminder", {}).get("en", "")
    reminder_ja = moon.get("reminder", {}).get("ja", "")

    turtle = log.get("turtle", {})
    laozi_quote = turtle.get("laozi_quote", "")
    murmur = turtle.get("murmur", [])
    murmur_1 = murmur[0] if len(murmur) > 0 else ""
    murmur_2 = murmur[1] if len(murmur) > 1 else ""

    quiet_cosmos = log.get("quiet_cosmos", {})
    cosmos_fact = quiet_cosmos.get("fact", "")
    cosmos_interpretation = quiet_cosmos.get("interpretation", "")

    lines = [
        f"## 📅 Date：{date_str}",
        "",
        "## 💭 What's on my mind",
        f"> {mind_en}",
        "",
        f"{mind_ja}",
        "",
        "## ❤️‍🔥 Honest Voice",
        f"- {honest_voice[0]}" if honest_voice else "- （なし）",
        "",
        "## 🏷 Tags",
        f"- {', '.join(tags_en) if tags_en else '（なし）'}",
        f"- {', '.join(tags_ja) if tags_ja else '（なし）'}",
        "",
        "## 🎯 Fujikoツッコミ",
        f"- {tukkomi[0]}" if tukkomi else "- （なし）",
        "",
        "## 🌕 Message from the Moon",
    ]

    if poetic_en or poetic_ja:
        lines.append(f"> {poetic_en}")
        lines.append(f"> {poetic_ja}")
        lines.append("")

    if grounding:
        for g in grounding:
            lines.append(f"- {g}")
        lines.append("")

    if reminder_en or reminder_ja:
        lines.append(f"> {reminder_en}")
        lines.append(f"> {reminder_ja}")
        lines.append("")

    lines += [
        "## 💎 Point of View",
        point_of_view or "（なし）",
        "",
        "## 🐢 亀のつぶやき",
        f"> {laozi_quote}",
        "",
        f"{murmur_1}",
        f"{murmur_2}",
        "",
        "## 🌌 Quiet Cosmos",
        f"> {cosmos_fact}" if cosmos_fact else "> （事実なし）",
        f"> {cosmos_interpretation}" if cosmos_interpretation else "> （解釈なし）"
    ]

    return "\n".join(lines)