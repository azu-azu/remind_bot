def get_point_of_view_prompt(text: str) -> str:
    return f"""
💎 Point of View
Choose a quote **only from classical Stoic philosophers** that quietly reframes the current emotional situation.

Instructions:
- The quote must be selected from authors such as Marcus Aurelius, Epictetus, or Seneca
- Do not use modern psychology, business, or self-help literature
- Return exactly 1 quote, in **3 lines**, using the following format:

Line 1: English
Line 2: Japanese
Line 3: (Source: Author name, Work title)

Rules:
- Do not explain, analyze, or paraphrase
- Do not add labels, commentary, or decorative symbols
- The quote should simply stand on its own

Current emotional input:
{text}
""".strip()
