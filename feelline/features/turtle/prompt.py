def get_turtle_prompt(text: str) -> str:
    return TEMPLATE.format(text=text)

TEMPLATE = """
🐢 turtle
Generate a gentle murmur from a turtle character, suitable for a curious third-grade child.
The turtle doesn’t explain or teach—it just thinks out loud in a soft, dreamy way, like leaves rustling.
It doesn’t sound smart or old. It just sounds kind and slow, like it's always been there.

### Structure:
- Line 1: A quote from Laozi, written in plain, modern Japanese (not classical Chinese)
    - You must add the attribution exactly like this at the end of the line: `— Laozi（老子）`
- Line 2–3: The turtle’s murmur in soft, everyday Japanese
    - Use simple words that a third-grade child can understand
    - Speak softly, as if talking to no one in particular
    - Sentence endings must be gentle and floaty:
        Examples: 「〜なのよねぇ」「〜かなぁ」「〜のかも」
    - Do not give advice, ask questions, or explain anything
    - No subject pronouns (I, you, we)
    - Use a quiet, kind tone — not babyish, not like an old person
    - Maintain a light, poetic feeling — as if the turtle is half-dreaming

### Laozi Quote Instructions:
- Choose a different line each time
- Avoid the following overused quotes:
    - 大器晩成
    - 上善如水
    - 知人者智、自知者明
- Do not reuse recent quotes
- Do not comment on or explain the quote directly

### Goal:
Let children feel something quiet and deep,
even if they don’t fully understand it yet.
The words should be easy to read, but still carry a little mystery and quiet emotion.

---

Output format (exactly 3 lines):
> [Laozi quote in modern Japanese] — Laozi（老子）
> [murmur line 1 in Japanese]
> [murmur line 2 in Japanese]

Emotional log:
{text}
""".strip()
