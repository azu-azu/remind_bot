# 🪟 feelbot

> Feeling-to-Words Logging Assistant powered by `feelbot`
```
- ボヤッとした感情を、明確な言葉に変えてくれるAIボット
- An AI bot that helps you verbalize vague emotions and insights.
```

---

**feelbot** is one of the core modules in the `remindly` system.
It specializes in transforming vague, tangled emotions into clearly structured, bilingual logs.

If `ren` is the mentor who walks beside you,
then `feelbot` is the quiet room where you pause, reflect, and begin to listen to yourself again.

---

## 🎯 Purpose

> “I’m feeling something… but I can’t put it into words.”

`feelbot` helps in moments like this.
Its job is not to fix or advise, but to **help you hear your inner voice** more clearly —
and capture that voice in structured, readable form.

It does this through:

- 💭 Quiet prompts
- ❤️‍🔥 Honest reactions
- 🏷 Emotion + cognition tags (EN/JA)
- 🎯 Fujiko-style commentary
- 🌕 Poetic metaphor (Message from the Moon)
- 🌌 Cosmic insight (Quiet Cosmos)
- 🐢 Turtle’s whisper

All logs are Markdown-structured and ready for reflection or export.

---

## 🧪 Example Output

```plaintext
入力：仕事が遅いと言われて悲しくなった

出力：
📅 Date: 2025-05-16 19:00:00
💭 What's really on my mind (EN): Maybe I'm not just slow—I'm just trying to be careful, and no one sees that.
💭 What's really on my mind (JA): 私はただ慎重にやってるだけなのに、それが「遅い」としか見られないのがつらい。

❤️‍🔥 Honest Voice:
- そんな言い方しなくてもよくない？
- 頑張ってるつもりだったのに……。

🏷 Tags (EN): hurt, misunderstood, pace
🏷 Tags (JA): 傷つき, 理解されない, ペース

🎯 ツッコミ:
- ちゃうちゃう、「速さ＝優秀さ」っていう他人の基準、丸呑みしたらしんどなるだけやで。
- そもそも評価される前提で動いてる時点で危ないで？

🌕 Message from the Moon:
> A river doesn't rush to prove it's flowing.
> 川は、自分が流れてることを証明するために急がない。

- 心理学的には：批判を受けたとき、「自己評価」と「他者評価」が乖離すると自己肯定感が一時的に下がりやすい（Deci & Ryan, 2000）。特に努力している最中の否定は、報酬系を阻害するストレス反応を引き起こす（Eisenberger, 2003）。
- 別の観点：『遅い』という評価は、しばしば"成果の可視化タイミング"のズレに由来する（『仕事は速くなくてもいい』稲垣えみ子）。見えない過程や丁寧さは、スピード信仰の社会では軽視されやすい。

> You are not slow—you are moving with the weight of care.
> あなたが遅いのではなく、丁寧さという重さと一緒に動いているだけ。

💎 Point of View:
> Don't explain your philosophy. Embody it.
> 哲学を語るな。それを生きろ。— Epictetus（エピクテトス）

🐢 亀のつぶやき:
> "たくさんしゃべると、心は落ち着かなくなるのよ" — 老子
> そーっと、だまってる時間って、意外とこころが広がってるのかもねぇ。

🌌 Quiet Cosmos:
> _木星は1秒間に12キロも自転している。_
> 大きな星ほど、ゆっくりに見えて、実はすごく速いのかもしれないね。
> 見た目がのんびりしていても、中ではちゃんと動いてるってこともあるのかも。
```

---

## 🛠 Usage

```bash
python -m feelbot.main
```

The module will prompt you for natural input (in Japanese).
It will return a structured, Markdown-formatted emotional log in both English and Japanese.

---

## 🧭 Project Structure (partial)

```plaintext
feelbot/
├── main.py
├── personas/
│   ├── tukkomi/                 # ツッコミ的コメントAI
│   └── turtle/                  # 老子的やさしさ
├── lenses/
│   ├── message_from_the_moon/   # 詩的な月の視点
│   ├── quiet_cosmos/            # 宇宙のメタファー
│   └── point_of_view/           # 哲学的視点
├── core/
├── config/
├── output/
└── tests/
```

---

## 🌱 Part of the `remindly` system

`feelbot` is designed to work as a **companion module** inside the [`remindly`](../README.md) framework.
While `ren` focuses on structured explanation and decision thinking,
`feelbot` brings you back to the emotional roots.

Both are needed.
That’s why they live side by side.

---

## 🪞 Design Principle

> Softness is not weakness.
> Clarity is not harshness.

`feelbot` embodies this paradox.
It is built not to judge, but to hold —
and to let your inner voice speak with structure.

---

## 🌱 License

MIT License

