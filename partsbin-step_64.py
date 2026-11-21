# === Stage 64: Add validation for relationship references ===
# Project: PartsBin
def validate_part(part):
    if not isinstance(part, dict):
        raise ValueError("part must be a dict")
    name = part.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("part name must be a non-empty string")
    quantity = part.get("quantity")
    if quantity is not None and (not isinstance(quantity, (int, float)) or quantity < 0):
        raise ValueError("quantity must be a non-negative number")
    reorder_point = part.get("reorder_point")
    if reorder_point is not None and (not isinstance(reorder_point, (int, float)) or reorder_point < 0):
        raise ValueError("reorder_point must be a non-negative number")
    supplier_id = part.get("supplier_id")
    if supplier_id is not None and (not isinstance(supplier_id, (str, int)) or supplier_id == ""):
        raise ValueError("supplier_id must be a non-empty string or integer")
    return part
