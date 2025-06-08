# Log storage and retrieval (json or sqlite)
# ログ設計における「記憶の中枢モジュール」

import json
import os
from datetime import datetime

def save_log(entry: dict):
    # ログファイル名用の日付文字列を生成
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_dir = "bots/logs"

    # logsフォルダがなければ自動で作る：存在しててもエラーにしない
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{date_str}.json")

    # すでに当日のログファイルがあれば、中身を読み出して追記用に保持
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = json.load(f)

    # 今回のログ（entry）をリストに追加
    logs.append(entry)

    # 整形済JSON形式で保存（日本語も壊れないよう ensure_ascii=False）
    # 'w' は 「書き込みモード（write）」
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

# 指定された日付のログファイル（例：2025-05-16.json）を読み込んでリストとして返す
def load_logs(date: str) -> list:
    # 日付をもとにファイルパスを生成
    log_file = os.path.join("logs", f"{date}.json")

    # ファイルがなければ空リストで返す（存在確認による安全性確保）
    if not os.path.exists(log_file):
        return []

    # 'r' は 読み込み専用モード（既存ファイルが必要）
    with open(log_file, 'r') as f:
        # JSONファイルを辞書リスト形式で返す
        return json.load(f)