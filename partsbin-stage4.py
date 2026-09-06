# === Stage 4: Implement create operations for the primary records ===
# Project: PartsBin
def create_part(part_id: int, name: str, quantity: int, reorder_point: int, supplier_id: int) -> dict:
    """Create a new Part record."""
    return {"id": part_id, "name": name, "quantity": quantity, "reorder_point": reorder_point, "supplier_id": supplier_id}

def create_supplier(supplier_id: int, name: str, email: str, phone: str) -> dict:
    """Create a new Supplier record."""
    return {"id": supplier_id, "name": name, "email": email, "phone": phone}

def create_bin_location(location_id: int, name: str, coordinates: tuple) -> dict:
    """Create a new BinLocation record."""
    return {"id": location_id, "name": name, "coordinates": coordinates}

def create_bin(bin_id: int, part_id: int, location_id: int, quantity: int) -> dict:
    """Create a new Bin record."""
    return {"id": bin_id, "part_id": part_id, "location_id": location_id, "quantity": quantity}
