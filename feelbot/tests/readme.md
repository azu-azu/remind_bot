# 🧪 Test Instructions
This directory contains manual and automated test scripts for validating output renderers.

## 📦 How to Run (from project root)

```bash
python3 feelbot/tests/test_cli_output_manual.py
```

### 📌 Purpose
This test verifies the behavior of flatten_result() and render_cli()
It uses a fixed dummy result structure to simulate structured emotional logs
No API calls are made — this is a local-only, zero-cost test

### 🛠️ Notes
Do not commit logs, only the test scripts
The CLI output is manually verified for structure, formatting, and content

### ✅ Future Plans
Add markdown and JSON renderer tests
Integrate pytest and snapshot testing

---

## Manual Unit Testing via Python REPL（REPLでの単体テスト）
* 「Pythonインタラクティブシェル（REPL）」

### 注意事項
* Python REPL で関数 or モジュールを変更したテストをするときは：
* 必ず importlib.reload() からやり直し
* from ... import ... 形式は避けて、モジュールごと import に統一
* reload後は明示的に cli_output.print_result(...) の形でテストさせる


### remindlyでpython起動
```
python3
```

### テストサンプル
```
from feelbot.format.cli_output import print_result
print_result({})
```

```
import importlib
import feelbot.format.cli_output as cli_output
importlib.reload(cli_output)
cli_output.print_result({})
```

---

[memo]

| 日本語     | 英語表現             | 説明                              |
| ------- | ---------------- | ------------------------------- |
| 単体テスト   | Unit Test        | 最小の関数やモジュール単位でのテスト。自動化可能なものが基本。 |
| 手動テスト   | Manual Test      | 自動じゃなく人間が手で確認するもの（REPLなど）       |
| 結合テスト   | Integration Test | 複数モジュールが連携して正しく動くかを確認するテスト      |
| システムテスト | System Test      | アプリ全体が要件どおりに動くかを確認するテスト         |
