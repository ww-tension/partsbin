# === Stage 22: Add favorite records and quick favorite listing ===
# Project: PartsBin
def add_favorite(record):
    """Mark a record as a favorite by copying it with a favorite flag."""
    return dict(record, is_favorite=True)

def list_favorites(warehouse):
    """Return all records in the warehouse that are marked as favorites."""
    return [rec for rec in warehouse if rec.get("is_favorite")]
