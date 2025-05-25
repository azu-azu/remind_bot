# feelbot/format/text_renderer.py

def flatten_result(result: dict) -> dict:
    """
    生のresult(dict)を、出力に使いやすいフラット構造に整形する
    """
    return {
        "date": result.get("date", ""),
        "mind_en": result.get("whats_on_my_mind", {}).get("en", ""),
        "mind_ja": result.get("whats_on_my_mind", {}).get("ja", ""),
        "honest_voice": result.get("honest_voice", []),
        "tags_en": ", ".join(result.get("tags", {}).get("en", [])),
        "tags_ja": ", ".join(result.get("tags", {}).get("ja", [])),
        "tukkomi": result.get("tukkomi", []),
        "moon_poetic_en": result.get("moon", {}).get("poetic", {}).get("en", ""),
        "moon_poetic_ja": result.get("moon", {}).get("poetic", {}).get("ja", ""),
        "moon_grounding": result.get("moon", {}).get("grounding", []),
        "moon_reminder_en": result.get("moon", {}).get("reminder", {}).get("en", ""),
        "moon_reminder_ja": result.get("moon", {}).get("reminder", {}).get("ja", ""),
        "pov_en": result.get("point_of_view", {}).get("en", ""),
        "pov_ja": result.get("point_of_view", {}).get("ja", ""),
        "pov_source": result.get("point_of_view", {}).get("source", ""),
        "laozi": result.get("turtle", {}).get("laozi_quote", ""),
        "turtle_murmur": result.get("turtle", {}).get("murmur", []),
        "cosmos_fact": result.get("quiet_cosmos", {}).get("fact", ""),
        "cosmos_interpretation": result.get("quiet_cosmos", {}).get("interpretation", "")
    }

def render_cli(flat: dict) -> str:
    """
    フラット化された辞書を使って、CLI用の整形文字列を返す
    """
    lines = []
    lines.append(f"\n📅 Date: {flat['date']}")
    lines.append("💭 What's really on my mind:")
    lines.append(f"EN: {flat['mind_en']}")
    lines.append(f"JA: {flat['mind_ja']}\n")

    if flat["honest_voice"]:
        lines.append("❤️‍🔥 Honest Voice:")
        lines.extend([f"- {line}" for line in flat["honest_voice"]])
        lines.append("")

    lines.append("🏷 Tags:")
    lines.append(f"EN: {flat['tags_en']}")
    lines.append(f"JA: {flat['tags_ja']}\n")

    if flat["tukkomi"]:
        lines.append("🎯 Fujikoツッコミ:")
        lines.extend([f"- {line}" for line in flat["tukkomi"]])
        lines.append("")

    if flat["moon_poetic_en"] or flat["moon_poetic_ja"]:
        lines.append("🌕 Message from the Moon:")
        lines.append(f"> {flat['moon_poetic_en']}")
        lines.append(f"> {flat['moon_poetic_ja']}")
        lines.append("") # ここで空行を追加（grounding前）
        lines.extend([f"- {line}" for line in flat["moon_grounding"]])
        lines.append("") # ここで空行を追加（grounding後）
        lines.append(f"> {flat['moon_reminder_en']}")
        lines.append(f"> {flat['moon_reminder_ja']}\n")

    if flat["pov_en"] or flat["pov_ja"]:
        lines.append("💎 Point of View:")
        lines.append(f"> {flat['pov_en']}")
        lines.append(f"> {flat['pov_ja']}")
        lines.append(flat["pov_source"])

    if flat["laozi"]:
        lines.append("\n🐢 亀のつぶやき:")
        lines.append(flat["laozi"])
        lines.extend(flat["turtle_murmur"])

    if flat["cosmos_fact"] or flat["cosmos_interpretation"]:
        lines.append("\n🌌 Quiet Cosmos:")
        lines.append(f"> {flat['cosmos_fact']}")
        lines.append(f"> {flat['cosmos_interpretation']}")

    return "\n".join(lines)
