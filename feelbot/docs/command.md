<!-- activate -->
source .venv/bin/activate

<!-- 実行 -->
python -m feelbot.main

<!-- 時間制限付きで実行（安全策） -->
gtimeout 30s python -m feelbot.main