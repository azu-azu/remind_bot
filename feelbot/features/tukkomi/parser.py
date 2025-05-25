from feelbot.config.config import MAX_TUKKOMI_COUNT

def parse_tukkomi(content: str) -> list[str]:
    return [
        line.strip()[2:].strip()
        for line in content.strip().split("\n")
        if line.strip().startswith("- ")
    ][:MAX_TUKKOMI_COUNT]
