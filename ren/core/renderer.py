# ren/core/renderer.py

class Renderer:
    def __init__(self, rules: dict):
        self.rules = rules
        self.section_order = rules.get("structure", {}).get("sections", [])

    def render(self, sections: dict) -> str:
        """
        sections: {
            'cited_source': ...,
            'mechanism': ...,
            ...
        }
        をMarkdown形式に変換して返す。
        """

        lines = []

        for section in self.section_order:
            content = sections.get(section)
            if not content:
                continue

            heading = self.get_heading(section)
            lines.append(heading)
            lines.append("")  # 1行空ける
            lines.append(content)
            lines.append("")  # セクションごとに空行

        return "\n".join(lines)

    def get_heading(self, section: str) -> str:
        """
        セクション名からMarkdown見出しを生成する（emoji + 見出しレベル）
        """
        emoji_map = {
            "cited_source": "📚",
            "mechanism": "🧱",
            "real_world_examples": "🔎",
            "summary": "🧩",
            "supplement": "💡",
            "closing": "🕊",
            "quote": "📘"
        }

        emoji = emoji_map.get(section, "##")
        heading_level = self.rules.get("markdown_rules", {}).get("heading_style", "##")
        return f"{heading_level} {emoji} {self.section_title(section)}"

    def section_title(self, section: str) -> str:
        """
        セクション名を見出し用のラベルに変換
        """
        title_map = {
            "cited_source": "Cited Source",
            "mechanism": "○○のしくみ",
            "real_world_examples": "Real-World Examples",
            "summary": "もう一度、まとめるよ",
            "supplement": "補足ポイント",
            "closing": "最後にひとこと",
            "quote": "Reference Quote"
        }
        return title_map.get(section, section)
