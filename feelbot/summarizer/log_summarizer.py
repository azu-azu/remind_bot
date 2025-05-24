import json
from datetime import datetime
from config.config import SUMMARY_MODEL, SUMMARY_TEMPERATURE
from core.chat_runner import run_chat

SESSION_SUMMARY_PROMPT_TEMPLATE = """
You are a structural emotional summarizer.

Your task is to review the following emotional logs and generate ONE final emotional log entry.

Each field must be filled with only one entry and match this exact structure:

- whats_on_my_mind.en: One-sentence emotional truth in English
- whats_on_my_mind.ja: The same in Japanese
- tags.en / tags.ja: 2–3 keywords for each
- honest_voice: The most emotionally raw expression (1 only, Japanese)
- tukkomi: A single clever structural comment in soft Kansai-ben (Japanese)
- point_of_view: One reflective philosophical line (in English or Japanese)
- moon.poetic.en / ja: One-line poetic insight in EN and JA
- moon.grounding: Two lines in JA (心理学的には／別の観点)
- moon.reminder.en / ja: Final gentle reminder in EN and JA
- turtle.laozi_quote: 1 line Laozi quote in Japanese
- turtle.murmur: 2 lines of poetic murmur in Japanese (list of 2 lines)
- quiet_cosmos:
    - fact: A scientifically accurate fact in simple Japanese (1 line)
    - interpretation: A soft poetic explanation (2–3 gentle lines in Japanese)

Input emotional logs:

{logs_json}

Output the result strictly in JSON format.
Do not include explanations or formatting outside the JSON structure.
"""

def summarize_logs(logs: list[dict]) -> dict:
    """
    Summarize multiple emotional logs into one final condensed log using GPT.
    This represents the emotional conclusion of a session.
    """
    logs_json = json.dumps(logs, ensure_ascii=False, indent=2)
    prompt = SESSION_SUMMARY_PROMPT_TEMPLATE.format(logs_json=logs_json)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        content = run_chat(
            messages=[
                {
                    "role": "system",
                    "content": "You are a structural emotional summarizer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=SUMMARY_MODEL,
            temperature=SUMMARY_TEMPERATURE
        )

        result = json.loads(content)
        result["date"] = now
        return result

    except Exception as e:
        return {
            "whats_on_my_mind": {"en": "", "ja": ""},
            "tags": {"en": [], "ja": []},
            "honest_voice": [f"[summary error: {e}]"],
            "tukkomi": "[構造要約エラー]",
            "point_of_view": "[構造観点生成エラー]",
            "moon": {
                "poetic": {"en": "", "ja": ""},
                "grounding": [],
                "reminder": {"en": "", "ja": ""}
            },
            "turtle": {
                "laozi_quote": "[老子の引用エラー]",
                "murmur": ["[つぶやき1エラー]", "[つぶやき2エラー]"]
            },
            "quiet_cosmos": {
                "fact": "[観察事実エラー]",
                "interpretation": "[詩的解釈エラー]"
            },
            "date": now
        }