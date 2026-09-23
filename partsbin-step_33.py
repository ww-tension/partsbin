# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: PartsBin
# Part 33: Settings dictionary and update functions
SETTINGS = {
    "default_reorder_point": 10,
    "default_lead_time_days": 5,
    "currency_symbol": "$",
    "decimal_format": ".2f",
    "notification_email": None,
    "log_file": "partsbin.log",
    "data_file": "partsbin_data.json",
}

def set_setting(key, value):
    """Set a settings key to a new value."""
    SETTINGS[key] = value

def get_setting(key, default=None):
    """Get a settings key, returning default if missing."""
    return SETTINGS.get(key, default)

def update_settings_from_dict(new_dict):
    """Merge a dictionary into SETTINGS, overwriting existing keys."""
    for k, v in new_dict.items():
        SETTINGS[k] = v
