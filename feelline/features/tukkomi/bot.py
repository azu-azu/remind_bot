from feelline.config.config import TUKKOMI_MODEL, TUKKOMI_TEMPERATURE, MAX_TUKKOMI_COUNT
from feelline.core.chat_runner import run_chat  # GPT通信共通関数
from .prompt import get_tukkomi_prompt

def generate_tukkomi(text: str) -> list[str]:
    prompt = get_tukkomi_prompt(text, MAX_TUKKOMI_COUNT)

    try:
        content = run_chat(
            messages=[{"role": "user", "content": prompt}],
            model=TUKKOMI_MODEL,
            temperature=TUKKOMI_TEMPERATURE
        )

        # Markdownの "- " 区切りを抽出
        return [
            line.strip()[2:].strip()
            for line in content.strip().split("\n")
            if line.strip().startswith("- ")
        ][:MAX_TUKKOMI_COUNT]

    except Exception as e:
        return [f"ツッコミ生成エラー: {e}"]