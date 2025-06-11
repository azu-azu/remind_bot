from abc import ABC, abstractmethod

class BaseSource(ABC):
    """
    抽象基底クラス：Renが構造知識を取得するための統一インターフェース
    """

    @abstractmethod
    def get_citation(self) -> str:
        """
        出典情報を返す（📚セクション）
        """
        pass

    @abstractmethod
    def explain_mechanism(self, topic: str) -> str:
        """
        指定されたトピックに基づき、構造の説明をMarkdownで返す（🧱セクション）
        """
        pass

    @abstractmethod
    def get_examples(self, topic: str) -> list:
        """
        Real-World Examples（🔎）をリスト形式で返す
        """
        pass

    @abstractmethod
    def get_summary(self, topic: str) -> str:
        """
        構造認識と行動示唆の2点セット（🪨）を返す
        """
        pass

    @abstractmethod
    def get_quote(self) -> str:
        """
        Reference Quote（📘）を返す
        """
        pass
