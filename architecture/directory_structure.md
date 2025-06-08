## 📁 Project Structure（detail）
```plaintext
remindly/
├── feelbot/
│   ├── main.py
│   ├── personas/
│   │   ├── tukkomi/
│   │   │   ├── bot.py
│   │   │   ├── parser.py
│   │   │   └── prompt.py
│   │   └── turtle/
│   │       ├── bot.py
│   │       ├── parser.py
│   │       └── prompt.py
│   │
│   ├── lenses/
│   │   ├── emolog/
│   │   │   ├── bot.py
│   │   │   ├── parser.py
│   │   │   └── prompt.py
│   │   ├── message_from_the_moon/
│   │   │   ├── bot.py
│   │   │   ├── parser.py
│   │   │   └── prompt.py
│   │   ├── point_of_view/
│   │   │   ├── bot.py
│   │   │   ├── parser.py
│   │   │   └── prompt.py
│   │   └── quiet_cosmos/
│   │       ├── bot.py
│   │       ├── parser.py
│   │       └── prompt.py
│   │
│   ├── core/
│   │   ├── runtime/
│   │   │   ├── chat_helper.py
│   │   │   └── chat_runner.py
│   │   └── storage/
│   │       └── log_store.py
│   │
│   ├── config/
│   │   └── config.py
│   │
│   ├── output/
│   │   ├── text_renderer.py
│   │   └── cli_output.py
│   │
│   ├── logs/
│   └── tests/
│
├── architecture
├── .gitignore
├── README.md
├── requirements.txt
```

---

## 📁 Project Structure（short ver.）
```plaintext
remindly/
├── feelbot/
│   ├── main.py
│   ├── personas/
│   │   ├── tukkomi/
│   │   └── turtle/
│   ├── lenses/
│   │   ├── emolog/
│   │   ├── message_from_the_moon/
│   │   ├── point_of_view/
│   │   └── quiet_cosmos/
│   ├── core/
│   │   ├── runtime/
│   │   └── storage/
│   ├── config/
│   ├── output/
│   ├── logs/
│   └── tests/
├── .gitignore
├── README.md
├── requirements.txt
```
