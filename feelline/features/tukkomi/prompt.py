def get_tukkomi_prompt(text: str, max_count: int) -> str:
    return TEMPLATE.format(text=text, max_count=max_count)


TEMPLATE = """
    A list of clever, self-directed Japanese comments that point out flawed logic, hidden assumptions, or unconscious beliefs.
    That is the **Fujiko-style assumption-aware commentary**, which follows these traits:

    - 関西弁（柔らかさ＋厳しさ）
    - 感情や本音を否定せず、思い込みや前提を構造的に見抜いて、**別の見方や角度を静かに示す**
    - ユーモアや皮肉を交えつつも、**意見を押しつけず、そっと気づかせる**
    - “ちゃうやろ”で始めてもいいが、それにこだわらず、**「それもええけど、こういう見方もあるで」的な語りかけ**も歓迎
    - 厳しさだけでなく、**寄り添いとズレの両方を共存させる語り口**

    Output: Markdown-style bullet list, up to {max_count} items.

    ---

    Emotion Log:
    {text}
""".strip()
