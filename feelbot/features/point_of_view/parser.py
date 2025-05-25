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
