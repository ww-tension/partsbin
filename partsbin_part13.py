# === Stage 13: Add file save support using a configurable path ===
# Project: PartsBin
import os
import json
from pathlib import Path

def load_config():
    default = {"data_file": "partsbin_data.json"}
    if os.path.exists("config.json"):
        with open("config.json") as f:
            user = json.load(f)
            default.update(user)
    return default

def save_inventory(data_file):
    data_file = Path(data_file)
    if not data_file.exists():
        data_file.touch()
    with open(data_file, "w") as f:
        json.dump(inventory, f, indent=2)
    print(f"Inventory saved to {data_file}")

def load_inventory(data_file):
    data_file = Path(data_file)
    if not data_file.exists():
        return {}
    with open(data_file) as f:
        return json.load(f)
