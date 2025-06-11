# Ren

## directory structure
```
remindly/
├── ren/
│   ├── main.py                        # CLI/スクリプトのエントリーポイント
│
│   ├── core/                          # 出力構造の核
│   │   ├── ren_core.py                # Renの中核ロジック
│   │   ├── prompt_guard.py            # 出力構造の検証クラス
│   │   └── renderer.py                # Markdown形式で整形出力
│
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── base_source.py            # 必要なら抽象クラス保持（GPTベース構成が中心なら、この .py 実装は削減 or 補助的位置）
│   │
│   │   ├── registry.py               # GPTに渡すときにsource一覧を構造化して提供
│   │
│   ├── sources/                      # 思想別の構造要約ファイル（← ここが新設）
│   │   ├── covey_7habits.md
│   │   ├── drucker_exec.md
│   │   ├── design_agile.md
│   │   ├── first_principles.md
│   │   └── radical_candor.md
│
│   ├── examples/
│   │   ├── elon_musk.txt
│   │   ├── amazon_example.md
│   │   └── templates/
│   │       └── output_template.md
│
│   ├── tests/
│   │   ├── test_ren_core.py
│   │   ├── test_prompt_guard.py
│   │   └── test_sources.py
│
│   ├── utils/
│   │   ├── logger.py
│   │   └── markdown_utils.py
│
│   ├── config/
│   │   ├── sources.yaml
│   │   ├── rules_loader.py
│   │   └── rules.yaml
│
│   └── README.md
```