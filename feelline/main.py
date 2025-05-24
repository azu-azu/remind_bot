from feelline.core.chat_helper import assemble_emotional_truth
from feelline.core.log_store import save_log
from datetime import datetime

if __name__ == "__main__":
    print("💬 入力してください（終了するには空のままEnter）")

    # ユーザーからの入力を受け取る/strip() で「先頭・末尾の無意味な空白」を取る
    user_input = input(">>> ").strip()

    # 入力が空でなければ、処理を開始
    if user_input:
        # GPTに入力文を送り、要約・タグ・リマインド判定を含む辞書型の構造データが返ってくる
        result = assemble_emotional_truth(user_input)

        # ログの記録日時（ISO形式で秒まで）
        result["timestamp"] = datetime.now().isoformat(timespec='seconds')

        # このログが main.py から来たことを示す
        result["source"] = "main.py"

        # CLI上に出力
        print("\n📅 Date:", result["date"])

        # 感情の真実（whats_on_my_mind）
        print("💭 What's really on my mind:")
        print("EN:", result["whats_on_my_mind"]["en"])
        print("JA:", result["whats_on_my_mind"]["ja"])

        # Honest Voice
        print("\n❤️‍🔥 Honest Voice:")
        for line in result.get("honest_voice", []):
            print("-", line)

        # タグ
        print("\n🏷 Tags:")
        print("EN:", ", ".join(result["tags"]["en"]))
        print("JA:", ", ".join(result["tags"]["ja"]))

        # ツッコミ
        print("\n🎯 Fujikoツッコミ:")
        for line in result.get("tukkomi", []):
            print("-", line)

        # Message from the Moon
        if "moon" in result:
            moon = result["moon"]
            print("\n🌕 Message from the Moon:")

            # poetic
            poetic_en = moon["poetic"].get("en", "")
            poetic_ja = moon["poetic"].get("ja", "")
            if poetic_en or poetic_ja:
                print("> " + poetic_en)
                print("> " + poetic_ja)
                print()

            # grounding
            if moon["grounding"]:
                for grounding in moon["grounding"]:
                    print("-", grounding)
                print()

            # reminder
            reminder_en = moon["reminder"].get("en", "")
            reminder_ja = moon["reminder"].get("ja", "")
            if reminder_en or reminder_ja:
                print("> " + reminder_en)
                print("> " + reminder_ja)

        # Point of View
        if "point_of_view" in result:
            pov = result["point_of_view"]
            print("\n💎 Point of View:")
            print(f"> {pov['en']}")
            print(f"> {pov['ja']}")
            print(f"{pov['source']}")

        # turtle
        if "turtle" in result:
            print("\n🐢 亀のつぶやき:")
            print(result["turtle"]["laozi_quote"])  # 老子の引用（1行）
            print()  # 空行で余白

            for line in result["turtle"].get("murmur", []):  # murmurはリスト形式
                print(line)

        # Quiet Cosmos
        if "quiet_cosmos" in result:
            print("\n🌌 Quiet Cosmos:")
            cosmos = result["quiet_cosmos"]
            print(f"> {cosmos['fact']}")
            print(f"> {cosmos['interpretation']}")

        # ログの保存
        save_log(result)
        print("✅ Saved!")
    else:
        print("👋 Exiting")
