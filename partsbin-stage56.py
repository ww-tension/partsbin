# === Stage 56: Add compact error classes for domain failures ===
# Project: PartsBin
class PartsBinError(Exception):
    """Base class for all PartsBin domain errors."""
    pass


class PartNotFoundError(PartsBinError):
    def __init__(self, part_id):
        self.part_id = part_id
        super().__init__(f"Part with id '{part_id}' not found.")


class SupplierNotFoundError(PartsBinError):
    def __init__(self, supplier_id):
        self.supplier_id = supplier_id
        super().__init__(f"Supplier with id '{supplier_id}' not found.")


class NegativeQuantityError(PartsBinError):
    def __init__(self, field):
        self.field = field
        super().__init__(f"Quantity for '{field}' cannot be negative.")


class ReorderPointError(PartsBinError):
    def __init__(self, field):
        self.field = field
        super().__init__(f"Reorder point for '{field}' must be non-negative.")
