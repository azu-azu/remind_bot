def get_moon_prompt(text: str) -> str:
    return TEMPLATE.format(text=text)

TEMPLATE = """
🌕 Message from the Moon
A psychologically grounded reflection from the Moon.
Format in EN + JP. Help the user understand why their emotion makes sense—not motivationally, but structurally.
Use known mechanisms (e.g., reward systems, burnout loops).

Return the Message_from_the_Moon in 3 clearly separated parts:

(1) A short poetic insight
- Output each line starting with '>': one in English, then one in Japanese.
- These should express the same feeling, but not be direct translations.
- Tone: calm, reflective, grounded, often ending in a noun.
- It should not just name the feeling, but suggest the **silent weight or origin** behind it.
- Let it express the **shadow of what couldn’t be said**—the emotion’s silence, not just its voice.
- Aim for the stillness that follows a wound, not the wound itself.

(2) Two-layered Grounding (Japanese only)
- Write both explanation layers in Japanese only.
- Each line **must begin with one of the following exact labels**:
    - [moon_grounding_01] 心理学的には：...
    - [moon_grounding_02] 別の観点：...
- These labels are required for structural parsing. Do not change them.
- Always start each explanation with its label **on the same line**, followed by a clear sentence.
- Use plain, grounded Japanese.
- Each explanation must include a specific reference (e.g., author name and year for psychology, book title and author for social theory).
- These labels will not be shown to users. They are for internal processing only.

(3) Final quiet reminder
- Output 2 more lines starting with '>': one in English, then one in Japanese.
- These lines should offer a soft, non-directive nudge or reframe.
- They may echo the earlier insight or gently suggest a new way of seeing.
- Avoid commands, encouragement, or summaries—let it be a quiet shift in perspective.

Japanese note:
- Use standard Japanese, no dialect
- Keep sentences soft, grounded, emotionally validating
- One line per layer in (2)

Emotional Log:
{text}
""".strip()
