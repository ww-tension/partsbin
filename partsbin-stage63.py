# === Stage 63: Add relationships between records where useful ===
# Project: PartsBin
class Bin:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def __repr__(self):
        return f"<Bin {self.name}: {len(self.parts)} parts>"


class Part:
    def __init__(self, name, quantity, reorder_point, supplier):
        self.name = name
        self.quantity = quantity
        self.reorder_point = reorder_point
        self.supplier = supplier

    def __repr__(self):
        return f"<Part {self.name} x{self.quantity} (reorder {self.reorder_point})>"


class Supplier:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"<Supplier {self.name}>"
