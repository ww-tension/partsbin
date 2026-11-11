# === Stage 45: Add restore from backup with validation ===
# Project: PartsBin
def restore_from_backup(path, validate=True):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Backup file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    parts = {}
    for ln in lines:
        if not ln.startswith("#"):
            cols = ln.split("|")
            if len(cols) < 4:
                raise ValueError(f"Malformed backup line: {ln!r}")
            parts[cols[0]] = {
                "name": cols[1],
                "quantity": int(cols[2]),
                "reorder": int(cols[3]),
                "supplier": cols[4] if len(cols) > 4 else "",
            }
    if validate and parts:
        for code, item in parts.items():
            if item["quantity"] < 0:
                raise ValueError(f"Negative quantity for part {code}")
            if item["reorder"] < 0:
                raise ValueError(f"Negative reorder point for part {code}")
    return parts
