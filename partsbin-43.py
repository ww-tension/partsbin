# === Stage 43: Add CSV import for the primary record type ===
# Project: PartsBin
def import_csv(path):
    import csv
    imported = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                imported.append({
                    "name": row["name"],
                    "quantity": int(row["quantity"]),
                    "reorder_point": int(row["reorder_point"]),
                    "supplier": row["supplier"],
                })
            except (KeyError, ValueError):
                continue
    return imported
