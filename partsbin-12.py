# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: PartsBin
def import_inventory(filepath):
    """Load inventory from a JSON file with forgiving error handling."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in '{filepath}': {e}")
        return {}
    except PermissionError:
        print(f"No permission to read '{filepath}'.")
        return {}
    except Exception as e:
        print(f"Unexpected error reading '{filepath}': {e}")
        return {}

    if not isinstance(data, dict):
        print("Expected a JSON object at the top level.")
        return {}
    return data
