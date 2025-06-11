from pathlib import Path

class SourceRegistry:
    """
    sources/ フォルダ内の .md 知識ファイルを管理・選定するクラス
    """

    def __init__(self, source_dir="sources"):
        self.source_dir = Path(source_dir)
        self.sources = self._load_sources()

    def _load_sources(self) -> dict:
        """
        .mdファイルを全件読み込んで辞書形式で返す
        キー: ファイル名（拡張子なし）
        値: 内容（str）
        """
        sources = {}
        for md_file in self.source_dir.glob("*.md"):
            key = md_file.stem
            with open(md_file, encoding="utf-8") as f:
                sources[key] = f.read()
        return sources

    def list_available_sources(self) -> list:
        """
        登録されているソース名一覧を返す
        """
        return list(self.sources.keys())

    def get_source_text(self, key: str) -> str:
        """
        指定したソースの内容を返す
        """
        return self.sources.get(key, "")

    def get_source_block(self) -> str:
        """
        GPTに渡す用の「出典要約ブロック」を自動生成
        各 .md の最初の2〜3行（タイトル・作者）をまとめて返す
        """
        blocks = []
        for key, text in self.sources.items():
            lines = text.strip().splitlines()
            title = lines[0].replace("# 📘 Title", "").strip() if lines else key
            author = next((l.replace("# ✍️ Author", "").strip() for l in lines if "# ✍️ Author" in l), "Unknown")
            blocks.append(f"- {key}: *{title}* by {author}")
        return "\n".join(blocks)
