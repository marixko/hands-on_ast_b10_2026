import json
from pathlib import Path

def load_config(config_path='config.json'):
    config_path = Path(config_path)
    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with config_path.open('r') as config_file:
        config = json.load(config_file)
    
    return config