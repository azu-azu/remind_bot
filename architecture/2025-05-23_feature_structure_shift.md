# 📌 2025-05-23｜構造転換ログ：技術軸から“意味軸”へ（features/run_chat）

---

## 🧭 背景と違和感

これまでの構成は、`prompt/`, `bots/`, `parsers/` のように
**“役割や技術的機能ごと”にディレクトリを分けていた**。

また、各 bot（emolog, tukkomi, turtle など）では、**それぞれが独自に `OpenAI()` を呼び出す構造**になっており、
**依存が分散し、GPT呼び出しの抽象レイヤーが存在していなかった**。

---

## 💡 発想

> - 「promptやbotで分けるんじゃなく、**“emolog”という単位で全部まとめたい**」
> - 「GPT呼び出しも、**技術詳細を意識せず使えるように抽象化したい**」

---

## 🛠 実行された構造改革

### ✅ 1. `features/` への移行（意味軸構成）

- `features/emolog/` に `bot.py`, `prompt.py`, `parser.py` を統合
- その他の機能（turtle, moon など）もすべて `features/` 配下に再配置
- import 文をすべて `features.xxx.bot` に統一
- 冗長なファイル名（例：`moon_prompt.py`）を廃止し、機能単位に簡素化

### ✅ 2. GPT呼び出し責任の分離（コア抽象化）

- **初期の問題**：各 bot が `from openai import OpenAI` を直に呼んでいた
- **構造判断**：
    - GPT呼び出しはコア層に集約すべき
    - `core/openai_client.py` を作成し、`call_openai()` を定義
- ✅ 全プロジェクト中で `from openai import OpenAI` が1箇所だけになり、**依存の制御が明確に**

---

## 📌 構造判断としての決断

> **構造は“意味”でまとめ、技術的詳細は“抽象”で包むべきである**

---

## 📚 設計思想における根拠

### 1. **ドメイン駆動設計（DDD）**

> 「設計はドメインの言語で整理されるべきであり、技術スタックによって形を決めてはならない」
> — *Eric Evans, DDD (2003)*

- `features/` のように、**意味でコードをグルーピングすること**はDDDにおけるbounded context設計に対応

### 2. **Clean Architecture（Robert C. Martin）**

> 「フレームワークや外部依存に設計を汚染されるな。依存は外に向かって一方向にすべきだ」
> — *Clean Architecture, 2017*

- GPTライブラリ（OpenAI）は外部依存であり、**bot側に直に持たせるのはアンチパターン**
- 依存方向は**内側（core層）に集約**し、**bot側は抽象的インターフェースとして使う**のが正解

### 3. **依存性逆転の原則（DIP）**

> 「高水準モジュールは、低水準モジュールに依存すべきではない。両者は抽象に依存すべきである」
> — *SOLID原則*

- `run_chat()` や `call_openai()` を通じて、**OpenAIという技術詳細が1箇所に閉じ込められた**構造は、DIPを実現している

---

## 🌙 設計感覚

> **「見失わない構造」＝意味と物理が一致し、依存と抽象が明確に分離されていること**

---

## 🔁 今後の運用方針

- **すべてのGPT呼び出しは `core/openai_client.py` 経由で行う**
- 技術的な詳細（モデル、API名、通信処理など）は**botから見えない構造に隔離**
- 新機能追加時は `features/` 内に意味でグルーピングし、同一機能内で完結するよう整理すること

