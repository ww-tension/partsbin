# === Stage 36: Add templates for quickly creating common records ===
# Project: PartsBin
def create_record(record_type, name, quantity=0, reorder_point=0, supplier=None, unit="piece"):
    if record_type not in ("part", "supply"):
        raise ValueError("record_type must be 'part' or 'supply'")
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    if reorder_point < 0:
        raise ValueError("reorder_point must be non-negative")
    if supplier is None:
        supplier = {"name": "Unknown", "contact": "", "email": ""}
    return {
        "id": next_record_id(),
        "type": record_type,
        "name": name,
        "quantity": quantity,
        "reorder_point": reorder_point,
        "supplier": supplier,
        "unit": unit,
        "created_at": datetime.now().isoformat(),
    }

def create_part(name, quantity=0, reorder_point=0, supplier=None, unit="piece"):
    return create_record("part", name, quantity, reorder_point, supplier, unit)

def create_supply(name, quantity=0, reorder_point=0, supplier=None, unit="box"):
    return create_record("supply", name, quantity, reorder_point, supplier, unit)

def create_supplier(name, contact="", email=""):
    return {"name": name, "contact": contact, "email": email}
