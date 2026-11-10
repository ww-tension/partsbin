# === Stage 42: Add CSV export without external dependencies ===
# Project: PartsBin
def export_to_csv(parts, filename="partsbin_export.csv"):
    if not parts:
        return
    fieldnames = ["id", "name", "category", "quantity", "reorder_point", "supplier", "unit", "location"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in parts:
            writer.writerow(p)
    return filename
