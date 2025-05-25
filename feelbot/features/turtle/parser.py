def parse_turtle(content: str) -> dict:
    lines = [line.strip() for line in content.splitlines() if line.strip()]

    return {
        "laozi_quote": lines[0] if len(lines) >= 1 else "",
        "murmur": lines[1:3] if len(lines) >= 3 else []
    }
