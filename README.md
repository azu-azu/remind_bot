# remind_bot 🐇
> Feeling-to-Words Assistant
- ボヤッとした感情を、明確な言葉に変えてくれるAIボット
- An AI bot that helps you verbalize vague emotions and insights.

---

## 🐰 Use Cases
- 日々のボヤッとした気持ちを言語化して内省に使いたいとき
- 自己理解のログを溜めて、感情パターンを可視化したいとき
- チームメンバーとの1on1前に、自分の感情を整理したいとき

---

## 🌠 Overview

**remind_bot** は、感情ログを入力すると、GPTがその構造・原因・内面パターンを分析し、次のような情報を出力します：

- 💭 What's really on my mind｜本当に言いたいこと
- ❤️‍🔥 Honest Voice｜心の底の本音
- 🏷 Tags｜感情・認知・内面カテゴリの英日対応
- 🎯 ツッコミ｜構造へのツッコミ
- 🌕 Message from the Moon｜根拠をもとにした検証
- 💎 Point of View｜哲学的な見方
- 🐢 亀のつぶやき｜空気を読まない亀のひとこと
- 🌌 Quiet Cosmos｜宇宙物理から見る側面

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

### 1. Clone the repository

```bash
git clone https://github.com/your-username/remind_bot.git
cd remind_bot
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ".env file"
ルートに .env ファイルを作成し、以下のように設定：

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
> ※ .env は .gitignore に含めて公開しないこと


### 5. How to Run
```bash
python main.py
```
> 感情ログを入力すると、英語と日本語で構造化された「気づきログ」が返ってきます。

---

## 📁 Project Structure
```plaintext
remind_bot/
├── main.py                            # Entry point for CLI-based emotion logging
├── session_summary_main.py            # Optional entry point for session summaries

├── core/                              # Core orchestration logic
│   ├── chat_helper.py                 # Assembles and coordinates component outputs
│   ├── chat_runner.py                 # Handles OpenAI API communication
│   └── log_store.py                   # Manages timestamped log storage

├── features/                          # Feature-based modular organization
│   ├── 💭emolog/
│   │   ├── bot.py                     # Core logic for emotional truth generation
│   │   ├── prompt.py                  # System prompts for emolog behavior
│   │   └── __init__.py
│
│   ├── 🎯tukkomi/
│   │   ├── bot.py                     # Fujiko-style commentary logic
│   │   ├── prompt.py                  # Prompting structure for critical voice
│   │   └── __init__.py
│
│   ├── 🌕message_from_the_moon/
│   │   ├── bot.py                     # Generates poetic and grounded moon messages
│   │   ├── prompt.py                  # Prompts for moon-inspired output
│   │   └── __init__.py
│
│   ├── 💎point_of_view/
│   │   ├── bot.py                     # Generates perspective-shifting insights
│   │   ├── prompt.py                  # Prompts for philosophical viewpoints
│   │   └── __init__.py
│
│   ├── 🐢turtle/
│   │   ├── bot.py                     # Quiet turtle-style reflections
│   │   ├── prompt.py                  # Prompts for turtle responses (optional)
│   │   └── __init__.py
│
│   ├── 🌌quiet_cosmos/
│   │   ├── bot.py                     # Provides cosmic-scale perspectives
│   │   ├── prompt.py                  # Astronomical facts and gentle metaphors
│   │   └── __init__.py

├── summarizer/                        # Log summarization engine
│   └── log_summarizer.py              # Aggregates and analyzes recent logs

├── config/                            # Global configuration (model, temperature, limits)
│   └── config.py

├── templates/                         # Output formatting templates (e.g. Markdown)
├── logs/                              # Auto-saved emotional log history
├── docs/                              # Documentation and usage guides
├── setup/                             # Setup and utility scripts

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

