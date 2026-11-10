# === Stage 41: Add plain text import for a simple line-based format ===
# Project: PartsBin
def load_lines(path):
    parts = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split(",")
            if len(fields) < 5:
                continue
            parts.append({
                "name": fields[0].strip(),
                "qty": int(fields[1].strip()),
                "reorder": int(fields[2].strip()),
                "supplier": fields[3].strip(),
                "price": float(fields[4].strip()) if fields[4].strip() else 0.0,
            })
    return parts


def save_lines(path, parts):
    with open(path, "w") as f:
        for p in parts:
            f.write(f"{p['name']},{p['qty']},{p['reorder']},{p['supplier']},{p['price']}\n")


def load_lines_csv(path):
    parts = []
    with open(path, "r") as f:
        header = f.readline().strip().lower().split(",")
        idx = {name: i for i, name in enumerate(header)}
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split(",")
            try:
                parts.append({
                    "name": fields[idx["name"]].strip(),
                    "qty": int(fields[idx["qty"]].strip()),
                    "reorder": int(fields[idx["reorder"]].strip()),
                    "supplier": fields[idx["supplier"]].strip(),
                    "price": float(fields[idx["price"]].strip()) if fields[idx["price"]].strip() else 0.0,
                })
            except (ValueError, IndexError):
                continue
    return parts
