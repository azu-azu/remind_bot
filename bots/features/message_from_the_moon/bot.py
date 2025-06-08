from bots.config.config import MOON_MODEL, MOON_TEMPERATURE
from bots.core.chat_runner import run_chat
from .prompt import get_moon_prompt
from .parser import parse_moon


def generate_moon(text: str) -> dict:
    """
    Run the GPT model to generate a Moon message based on the given emotional log text.
    The output is parsed by `parse_moon()` to extract structured content.
    """
    prompt = get_moon_prompt(text)

    try:
        raw = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=MOON_MODEL,
            temperature=MOON_TEMPERATURE
        ).strip()

        return parse_moon(raw)

    except Exception as e:
        return {
            "poetic": {"en": "Silence is safer than speech. — Epictetus", "ja": "沈黙は、心地いい🌙"},
            "grounding": [
                "🌘心理学的には：2分間の静寂がストレスホルモンを低下させ、集中力を高めることが研究で示されています（2006年, NIH他）",
                "🌒さらに、3日間の継続的な沈黙が海馬に新たなニューロンを生む可能性があるという報告もあります（最近の神経可塑性研究）"
            ],
            "reminder": {"en": "Silence is the sleep that nourishes wisdom. — Francis Bacon", "ja": "沈黙は、知恵を育てる"}
        }
