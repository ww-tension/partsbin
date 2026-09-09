# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: PartsBin
def sort_parts(parts, key):
    """Sort parts by the given key: title, date, priority, or last_update."""
    key_map = {
        'title': lambda p: p['title'].lower(),
        'date': lambda p: p['date'],
        'priority': lambda p: p['priority'],
        'last_update': lambda p: p['last_update'],
    }
    if key not in key_map:
        return parts
    return sorted(parts, key=key_map[key])
