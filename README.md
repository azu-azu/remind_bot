
# 🌙 remindly
> Feeling-to-Words Logging Assistant powered by `feelline`
- ボヤッとした感情を、明確な言葉に変えてくれるAIボット
- An AI bot that helps you verbalize vague emotions and insights.

**remindly** is an AI system designed to **record and manage structured emotional logs**,
generated through the expressive power of its core engine, `feelline`.

While `feelline` transforms vague or tangled emotions into clear and structured language,
**remindly** receives those outputs and organizes them into meaningful records—
for reflection, tracking, and emotional pattern analysis over time.

---

## 🐰 Use Cases

```
- 日々のボヤッとした気持ちを言語化して内省に使いたいとき
- 自己理解のログを溜めて、感情パターンを可視化したいとき
- チームメンバーとの1on1前に、自分の感情を整理したいとき
```

- When you want to clarify your vague emotions and store them for future reflection
- When you're looking to build a personal emotional log and observe recurring patterns
- When you want to ground yourself before a 1on1 or difficult conversation

---

## 🌠 Overview

The system generates structured, Markdown-based emotional logs from natural input.
Each log includes layered insights such as:

- 💭 What's really on my mind — The quiet, unspoken truth behind your words
- ❤️‍🔥 Honest Voice — Raw, unfiltered emotional reactions
- 🏷 Tags — Emotion and cognition labels in EN/JA
- 🎯 Fujiko-style Commentary — Soft, witty critique of your internal logic
- 🌕 Message from the Moon — Grounded psychological reflection with poetic framing
- 💎 Point of View — Quiet, perspective-shifting insight drawn from philosophy or timeless wisdom
- 🐢 Turtle's Whisper — Gentle Laozi-inspired murmurs
- 🌌 Quiet Cosmos — Cosmic-scale metaphors from real astrophysics

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
- A river doesn't rush to prove it's flowing.
- 川は、自分が流れてることを証明するために急がない。

- 心理学的には：批判を受けたとき、「自己評価」と「他者評価」が乖離すると自己肯定感が一時的に下がりやすい（Deci & Ryan, 2000）。特に努力している最中の否定は、報酬系を阻害するストレス反応を引き起こす（Eisenberger, 2003）。

- 別の観点：『遅い』という評価は、しばしば"成果の可視化タイミング"のズレに由来する（『仕事は速くなくてもいい』稲垣えみ子）。見えない過程や丁寧さは、スピード信仰の社会では軽視されやすい。

- You are not slow—you are moving with the weight of care.
- あなたが遅いのではなく、丁寧さという重さと一緒に動いているだけ。

💎 Point of View:
- Don't explain your philosophy. Embody it.
- 哲学を語るな。それを生きろ。— Epictetus（エピクテトス）

🐢 亀のつぶやき:
- "たくさんしゃべると、心は落ち着かなくなるのよ" — 老子
- そーっと、だまってる時間って、意外とこころが広がってるのかもねぇ。

🌌 Quiet Cosmos:
- _木星は1秒間に12キロも自転している。_
- 大きな星ほど、ゆっくりに見えて、実はすごく速いのかもしれないね。
- 見た目がのんびりしていても、中ではちゃんと動いてるってこともあるのかも。
```

---

## 🛠 Setup

```bash
git clone https://github.com/your-username/remindly.git
cd remindly
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

ルートに .env ファイルを作成し、以下のように設定：
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
> ※ .env は .gitignore に含めて公開しないこと


### How to Run
```bash
python feelline/main.py
```
> 感情ログを入力すると、英語と日本語で構造化された「気づきログ」が返ってきます。

---

## 📁 Project Structure
```plaintext
remindly/
├── feelline/ # Core emotional processing logic
│ ├── main.py
│ ├── features/ # Each feature module (emolog, moon, turtle, etc.)
│ ├── core/ # Orchestration, inference, API handling
│ ├── summarizer/ # Log aggregation and analysis
│ ├── templates/ # Markdown output formatting
│ └── config/ # Global settings and environment management
├── .gitignore
├── README.md
├── requirements.txt
```

---

📐 Philosophy of Design
Why we chose not to use LangChain

This project was built not just to process text,
but to explore and articulate the structure of human emotion.
At the core of the design lies the deep intention:

> 🫧 To express vague or tangled feelings in language—gently, precisely, structurally.

Therefore, the entire system was designed around these principles:
- Prompts must be poetic — not abstract, but emotionally resonant and grounded.
- Output must be explicit and structured — in Markdown or JSON, with no hidden processing.
- Interaction must feel like reading, not querying — the experience matters.

We consciously avoided LangChain because:
- Its abstractions (like OutputParser) interfere with the softness and subtlety of our expressions.
- Fine-grained prompt tuning becomes harder under the LangChain paradigm.
- The project is not about "tool chaining"—it's about sensing structure in human experience.

So from the beginning, we made a clear design decision:
This is not a LangChain problem.
This is a "build it line by line, with us" problem.

---

## 🌱 License
MIT License

---

