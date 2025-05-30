# 📌 2025-05-25｜bot.pyとparser.pyの分離：責務再構成の記録

---

## 🧭 背景と課題

これまで `generate_xxx()` 関数内で行っていた処理は、次の3つが一体化していた：

1. promptの生成
2. GPTへの問い合わせ
3. 結果の整形・抽出

この構造には以下の問題があった：

- **責務の境界が曖昧**で、各層の役割が不明確になりがちだった
- 特定のロジック（例：JSON解析、行抽出など）を**再利用できなかった**
- ユニットテストが難しく、**構造のデバッグ・保守性が低下**していた

---

## 🧱 分離の目的と方針

### ✅ 結論

> `bot.py` は **GPTとの対話制御に集中**し、
> `parser.py` は **GPT出力の整形・抽出に専念する分離構造**に再設計した。

---

## 📐 新構造における責務定義

| ファイル       | 責務内容                           |
|----------------|------------------------------------|
| `bot.py`       | - promptを生成する（prompt.pyから）<br> - run_chatを実行する<br> - 結果をparserに渡す |
| `parser.py`    | - GPT出力の構造に基づき<br>　必要なフィールドを抽出・整形 |

---

## 🔍 構造設計としての意図

- **「整形」と「制御」を分離**することで、各関数が単純・明確になる
- parserは、**どこから呼ばれても同じように整形処理が行える**
- botは、「どう整えるか」には関与せず、**あくまで“中継と制御”に集中**

---

## 🔁 運用上のメリット

| 観点           | 効果 |
|----------------|------|
| テスト性       | parser単体でテスト可能（GPTレスポンスをモック可） |
| 再利用性       | parserを別の入力源にも流用可能 |
| 保守性         | botとparserの修正が分離され、影響範囲が狭まる |
| 説明責任の明確化 | GPTが期待構造を返す前提と、それを整形する側の責任を切り分けられる |

---

## 🛡️ 今後の指針

- **parserは“整形のみ”に徹し、構造制御（件数・型など）はbotが責任を持つ**
- parserが定数を読み込む構造は禁止し、**botから引数として渡す設計に統一**
- 機能追加時にも、「生成」と「整形」の分離を徹底し、再利用性と保守性を最優先に考えること

