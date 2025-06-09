# ren/config/rules_loader.py

import yaml
import os

def load_rules() -> dict:
    """
    rules.yaml を読み込んで辞書として返す。
    """
    config_path = os.path.join(os.path.dirname(__file__), 'rules.yaml')
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
