# temperature
# 0.3: 安定性重視｜講師タイプ（感情分析の正確性）｜出力のブレを抑えて安定した返答を目指す
# 0.4: やや低め｜哲学的視点、ユーモアと洞察
# 0.5: バランス重視｜詩的表現と根拠、要約の柔軟性
# 0.6: やや高め｜科学的事実と詩的解釈のバランス
# 0.8: 創造性重視｜自由な発想

DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.3

# 💭 emolog_generator.py
EMOLOG_MODEL = DEFAULT_MODEL
EMOLOG_TEMPERATURE = 0.3
MAX_HONEST_COUNT = 2  # Honest Voice の最大数

# 🌕 message_from_the_moon_generator.py
MOON_MODEL = DEFAULT_MODEL
MOON_TEMPERATURE = 0.6

# 💎 point_of_view_generator.py
POV_MODEL = DEFAULT_MODEL
POV_TEMPERATURE = 0.5

# 🎯 tukkomi_bot.py
TUKKOMI_MODEL = DEFAULT_MODEL
TUKKOMI_TEMPERATURE = 0.6
MAX_TUKKOMI_COUNT = 2  # ツッコミの最大数

# 🐢 turtle_bot.py
TURTLE_MODEL = DEFAULT_MODEL
TURTLE_TEMPERATURE = 0.8

# 🌌 quiet_cosmos_bot.py
QUIET_COSMOS_MODEL = DEFAULT_MODEL
QUIET_COSMOS_TEMPERATURE = 0.6

# 💬 log_summarizer.py
SUMMARY_MODEL = DEFAULT_MODEL
SUMMARY_TEMPERATURE = 0.4