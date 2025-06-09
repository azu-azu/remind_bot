# ren/core/ren_core.py

from ren.knowledge.drucker import DruckerSource  # 暫定：まずは1つだけ実装
from ren.core.prompt_guard import PromptGuard
from ren.core.renderer import Renderer
from ren.config.rules_loader import load_rules  # rules.yamlから読み込み
import datetime

class RenCore:
    def __init__(self):
        self.rules = load_rules()
        self.source = DruckerSource()  # 今はDruckerだけ、将来は選択可能に
        self.guard = PromptGuard(self.rules)
        self.renderer = Renderer(self.rules)

    def generate_output(self, topic: str) -> str:
        """
        指定されたトピックに基づき、構造化されたMarkdown出力を生成する。
        """

        # 1. Sourceから情報取得
        citation = self.source.get_citation(topic)
        mechanism = self.source.explain_mechanism(topic)

        # 2. 出力構造を組み立てる
        sections = {
            "cited_source": citation,
            "mechanism": mechanism,
            "real_world_examples": self.source.get_examples(topic),
            "summary": self.source.summarize(topic),
            "supplement": self.source.get_supplement_points(topic),
            "closing": self.source.get_closing_sentence(topic),
            "quote": self.source.get_reference_quote(topic)
        }

        # 3. PromptGuardで構造検証（failなら例外）
        self.guard.validate(sections)

        # 4. Markdown形式で整形して返す
        output = self.renderer.render(sections)

        return output

    def save_output(self, topic: str, output: str):
        """
        Markdownファイルとして保存。ファイル名は連番なし・日付入り。
        """
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{date_str}_{topic.replace(' ', '-')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
