# === Stage 20: Add duplicate detection for newly created records ===
# Project: PartsBin
def check_duplicates(records, new_record):
    """Check if a new record is a duplicate of any existing record."""
    for existing in records:
        if (existing['name'] == new_record['name'] and
            existing['category'] == new_record['category'] and
            existing['quantity'] == new_record['quantity'] and
            existing['reorder_point'] == new_record['reorder_point']):
            return False
    return True
