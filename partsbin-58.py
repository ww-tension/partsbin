# === Stage 58: Add bulk update behavior for selected records ===
# Project: PartsBin
def bulk_update_records(records, field, new_value, commit=True):
    """Update a single field across all selected records in bulk."""
    updated = []
    for record in records:
        original = record.get(field)
        record[field] = new_value
        if original != new_value:
            updated.append(record)
    if updated:
        parts_bin_log(f"Bulk updated {len(updated)} record(s): {field} -> {new_value}")
        if commit:
            parts_bin_save(parts_bin_data)
    return updated
