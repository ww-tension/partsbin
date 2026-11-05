# === Stage 38: Add data integrity checks for broken references ===
# Project: PartsBin
def check_integrity(data):
    parts = data.get("parts", [])
    suppliers = data.get("suppliers", [])
    supplier_ids = {s["id"] for s in suppliers}
    errors = []
    for i, part in enumerate(parts):
        if "id" not in part:
            errors.append(f"part[{i}] missing id")
        if "name" not in part:
            errors.append(f"part[{i}] missing name")
        if "quantity" not in part:
            errors.append(f"part[{i}] missing quantity")
        if "reorder_point" not in part:
            errors.append(f"part[{i}] missing reorder_point")
        if "supplier_id" in part and part["supplier_id"] not in supplier_ids:
            errors.append(f"part[{i}] references unknown supplier_id {part['supplier_id']}")
    return errors
