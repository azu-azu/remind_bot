from feelline.config.config import QUIET_COSMOS_MODEL, QUIET_COSMOS_TEMPERATURE
from feelline.core.chat_runner import run_chat
from .prompt import get_quiet_cosmos_prompt


def generate_quiet_cosmos(theme: str) -> dict:
    """
    Generate Quiet Cosmos output as a dictionary with fact and interpretation.
    """
    prompt = get_quiet_cosmos_prompt(theme)

    try:
        response = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=QUIET_COSMOS_MODEL,
            temperature=QUIET_COSMOS_TEMPERATURE
        ).strip()

        lines = [line.strip() for line in response.splitlines() if line.strip()]

        # Remove section headers and blank lines
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

    except Exception as e:
        return {
            "fact": f"[quiet cosmos error: {e}]",
            "interpretation": "宇宙がちょっと迷子になったみたい。"
        }