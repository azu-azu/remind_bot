import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from bots.lenses.emolog.parser import parse_emolog
from bots.lenses.message_from_the_moon.parser import parse_moon
from bots.lenses.point_of_view.parser import parse_point_of_view
from bots.lenses.quiet_cosmos.parser import parse_quiet_cosmos
from bots.personas.tukkomi.parser import parse_tukkomi
from bots.personas.turtle.parser import parse_turtle
from bots.output.text_renderer import flatten_result, render_cli


if __name__ == "__main__":
    print("▶️ TEST START — all feature parsers\n")

    # --- emolog ---
    parsed_emolog = parse_emolog({
        "whats_on_my_mind": {"en": "I'm tired", "ja": "疲れた"},
        "honest_voice": ["もっと早く進めたい", "でも動けない"],
        "tags": {"en": ["balance"], "ja": ["バランス"]},
    }, 2)

    # --- moon ---
    moon_text = """> 静けさは力になる。
    > Silence becomes strength.
    > あなたの存在は充分です。
    > Your presence is enough.

    [moon_grounding_01] 心理学的には：静けさは回復の源になります。
    [moon_grounding_02] 別の観点：立ち止まることで道が見えることもあります。
    """

    parsed_moon = parse_moon(moon_text)

    # --- point_of_view ---
    parsed_pov = parse_point_of_view("""Stay grounded.
地に足をつけて。
— Laozi""")

    # --- tukkomi ---
    parsed_tukkomi = parse_tukkomi("""- もっと落ち着けや
- はよやらんかい""",2)

    # --- turtle ---
    parsed_turtle = parse_turtle("""知者不言、言者不知。
本当に知ってる人は、静かに見ている。
その静けさが、世界を変えるかもしれない。""")

    # --- quiet_cosmos ---
    quiet_cosmos_text = """Scientific Fact:
    The moon has no atmosphere.

    Kid-Friendly Version:
    So you can't hear anything there. It's always quiet."""

    parsed_cosmos = parse_quiet_cosmos(quiet_cosmos_text)

    # --- 統合構造（flatten準拠） ---
    combined = {
        "date": "",
        "whats_on_my_mind": parsed_emolog["whats_on_my_mind"],
        "honest_voice": parsed_emolog["honest_voice"],
        "tags": parsed_emolog["tags"],
        "tukkomi": parsed_tukkomi,
        "moon": parsed_moon,
        "point_of_view": parsed_pov,
        "turtle": parsed_turtle,
        "quiet_cosmos": parsed_cosmos
    }

    flat = flatten_result(combined)
    print("🟨 flattened result:", flat)

    output = render_cli(flat)
    print("\n🖨️ rendered output:\n")
    print(output)
