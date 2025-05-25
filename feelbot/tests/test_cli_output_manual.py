import sys
import os

# ✅ プロジェクトルートを import パスに追加（VSCode・CI・tests/直実行対応）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from feelbot.format.text_renderer import flatten_result, render_cli

# ✅ テスト用のダミーデータ
dummy_result = {
    "date": "2025-05-25 08:26:00",
    "whats_on_my_mind": {
        "en": "I feel like I'm floating in space.",
        "ja": "宇宙にただよってる気分やわ。"
    },
    "honest_voice": ["Take your time.", "Don't rush."],
    "tags": {
        "en": ["#calm", "#space"],
        "ja": ["#静けさ", "#宇宙"]
    },
    "tukkomi": ["どこ行くねん！", "ちゃんと地球に戻ってきなはれ〜"],
    "moon": {
        "poetic": {
            "en": "The moon does not judge.",
            "ja": "月は、何も裁かない。"
        },
        "grounding": ["心理学的には：距離を取ると安心が戻ることもあるんやで。"],
        "reminder": {
            "en": "You don't have to have it all figured out.",
            "ja": "全部わからなくても大丈夫や。"
        }
    },
    "point_of_view": {
        "en": "Perspective changes everything.",
        "ja": "視点が変われば、すべてが変わる。",
        "source": "Fujiko"
    },
    "turtle": {
        "laozi_quote": "上善は水の如し。",
        "murmur": ["ゆっくり、静かに、深く。", "焦らんと、流れにまかせてええんや。"]
    },
    "quiet_cosmos": {
        "fact": "宇宙では音は伝わらない。",
        "interpretation": "静けさこそが、宇宙の言葉。"
    }
}

# ✅ 実行部分
if __name__ == "__main__":
    flat = flatten_result(dummy_result)
    output = render_cli(flat)
    print(output)
