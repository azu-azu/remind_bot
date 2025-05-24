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
- Each item must be on a new line and begin with:
    - 心理学的には：clearly cite the psychological or neuroscientific research source (e.g., author name and year) that supports the explanation.
    - 別の観点：an explanation grounded in insights from social theory or business literature. Be sure to include a clear reference (e.g., book name and author) to support the claim.

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
