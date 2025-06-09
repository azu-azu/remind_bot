# ren/core/prompt_guard.py

class PromptGuard:
    def __init__(self, rules: dict):
        self.required_sections = set(
            rules.get("structure", {}).get("required_sections", [])
        )

    def validate(self, sections: dict):
        """
        出力構造（セクション辞書）がルールを満たしているかを検証。
        足りないものや空の要素があれば ValueError を投げる。
        """

        # 必須セクションの存在チェック
        missing = self.required_sections - set(sections.keys())
        if missing:
            raise ValueError(f"Missing required sections: {', '.join(missing)}")

        # 各セクションの内容が空でないかチェック
        empty = [key for key, val in sections.items() if not val or val.strip() == ""]
        if empty:
            raise ValueError(f"Empty content in sections: {', '.join(empty)}")

        # Markdown構文の静的構造チェック（将来拡張用）
        # 例: heading level, --- の挿入確認 など

        return True
