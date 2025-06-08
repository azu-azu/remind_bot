from bots.core.chat_helper import assemble_emotional_truth
from bots.core.log_store import save_log
from bots.format.cli_output import print_result
from datetime import datetime

if __name__ == "__main__":
    print("💬 入力してください（終了するには空のままEnter）")
    user_input = input(">>> ").strip()

    if user_input:
        # 感情構造ログを生成
        result = assemble_emotional_truth(user_input)

        # メタ情報付加
        result["timestamp"] = datetime.now().isoformat(timespec='seconds')
        result["source"] = "main.py"

        # 👉 出力責任はここに一任！
        print_result(result)

        # ログ保存
        save_log(result)
        print("✅ Saved!")
    else:
        print("👋 Exiting")
