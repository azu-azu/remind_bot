from datetime import datetime

from bots.features.emolog.bot import generate_emolog  # 💭
from bots.features.message_from_the_moon.bot import generate_moon  # 🌕
from bots.features.point_of_view.bot import generate_point_of_view  # 💎
from bots.features.tukkomi.bot import generate_tukkomi  # 🎯
from bots.features.turtle.bot import generate_turtle  # 🐢
from bots.features.quiet_cosmos.bot import generate_quiet_cosmos  # 🌌

# 感情を抽出するメイン関数
def assemble_emotional_truth(text: str) -> dict:
    truth = generate_emolog(text)

    return {
        "whats_on_my_mind": truth["whats_on_my_mind"],
        "tags": truth["tags"],
        "honest_voice": truth["honest_voice"],
        "tukkomi": generate_tukkomi(text),
        "moon": generate_moon(text),
        "turtle": generate_turtle(text),
        "point_of_view": generate_point_of_view(text),
        "quiet_cosmos": generate_quiet_cosmos(text),  # 🌌 宇宙からの静かな観察

        # GPTのdateは使わず、常にローカル日時を使用：GPTのdateは不正確のため
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }