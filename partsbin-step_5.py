# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: PartsBin
def update_quantity(self, item_id, new_quantity):
    """Update the quantity of an item by ID."""
    if item_id not in self._items:
        raise KeyError(f"Item with id '{item_id}' not found.")
    self._items[item_id]["quantity"] = new_quantity
    return self._items[item_id]

def update_reorder_point(self, item_id, new_point):
    """Update the reorder point for an item by ID."""
    if item_id not in self._items:
        raise KeyError(f"Item with id '{item_id}' not found.")
    self._items[item_id]["reorder_point"] = new_point
    return self._items[item_id]

def update_supplier(self, item_id, supplier_name, supplier_contact):
    """Update the supplier information for an item by ID."""
    if item_id not in self._items:
        raise KeyError(f"Item with id '{item_id}' not found.")
    self._items[item_id]["supplier_name"] = supplier_name
    self._items[item_id]["supplier_contact"] = supplier_contact
    return self._items[item_id]
