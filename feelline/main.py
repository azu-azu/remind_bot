from core.log_store import load_logs
from summarizer.log_summarizer import summarize_logs
from core.markdown_exporter import export_markdown
from pathlib import Path
import sys

# 例）python session_summary_main.py logs/2025-05-18.json
# このコマンドを実行した場合のコマンドライン引数は...
# sys.argv[0] session_summary_main.py：自分自身（スクリプトファイル名）
# sys.argv[1] logs/2025-05-18.json：ユーザーが渡した「ログファイルのパス」

def main():
    # --- 1. ログファイルのパスを取得 ---
    if len(sys.argv) < 2:
        print("Usage: python session_summary_main.py <path_to_log_file>")
        sys.exit(1)

    log_path = sys.argv[1]

    if not Path(log_path).exists():
        print(f"Error: File not found: {log_path}")
        sys.exit(1)

    # --- 2. 複数ログ読み込み ---
    logs = load_logs(log_path)

    # --- 3. GPTで1件に要約 ---
    summary_log = summarize_logs(logs)

    # --- 4. Markdown形式に変換 ---
    markdown = export_markdown(summary_log)

    # --- 5. Markdown出力 ---
    print("\n\n===== FINAL SUMMARY (Markdown) =====\n")
    print(markdown)


if __name__ == "__main__":
    main()
