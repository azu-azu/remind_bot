<!-- activate -->
source .venv/bin/activate

<!-- 実行 -->
python -m feelline.main

<!-- 時間制限付きで実行（安全策） -->
gtimeout 30s python -m feelline.main