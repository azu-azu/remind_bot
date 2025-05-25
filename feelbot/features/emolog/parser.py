from feelbot.config.config import MAX_HONEST_COUNT

def parse_emolog(data: dict) -> dict:
    """
    Extract structured emolog fields from GPT JSON response.
    """
    return {
        "whats_on_my_mind": {
            "en": data.get("whats_on_my_mind", {}).get("en", ""),
            "ja": data.get("whats_on_my_mind", {}).get("ja", "")
        },
        "honest_voice": data.get("honest_voice", [])[:MAX_HONEST_COUNT],
        "tags": {
            "en": data.get("tags", {}).get("en", []),
            "ja": data.get("tags", {}).get("ja", [])
        }
    }
