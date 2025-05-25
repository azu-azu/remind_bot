def parse_tukkomi(content: str, max_count: int) -> list[str]:
    return [
        line.strip()[2:].strip()
        for line in content.strip().split("\n")
        if line.strip().startswith("- ")
    ][:max_count]
