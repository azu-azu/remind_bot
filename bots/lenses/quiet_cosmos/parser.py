def parse_quiet_cosmos(response: str) -> dict:
    lines = [line.strip() for line in response.splitlines() if line.strip()]

    fact_line = ""
    explanation_lines = []

    fact_started = False
    for line in lines:
        if "Scientific Fact" in line or "Kid-Friendly Version" in line:
            continue
        if not fact_started:
            fact_line = line
            fact_started = True
        else:
            explanation_lines.append(line)

    return {
        "fact": fact_line,
        "interpretation": " ".join(explanation_lines[:3])
    }
