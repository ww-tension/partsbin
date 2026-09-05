# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: PartsBin
import dataclasses
from typing import List

@dataclasses.dataclass
class Supplier:
    name: str
    contact: str

@dataclasses.dataclass
class Part:
    name: str
    sku: str
    quantity: int
    reorder_point: int
    unit_price: float
    supplier: Supplier

parts: List[Part] = [
    Part("Screw M4x20", "M4-20", 500, 100, 0.05, Supplier("FastenerCo", "info@fastenerco.com")),
    Part("LED 5mm Red", "LED-RED-5", 30, 10, 0.25, Supplier("OptoSupply", "sales@optosupply.com")),
    Part("Resistor 1kΩ", "RES-1K", 200, 50, 0.01, Supplier("ElecParts", "orders@elecparts.com")),
    Part("Bolt M6x50", "M6-50", 100, 20, 0.10, Supplier("FastenerCo", "info@fastenerco.com")),
]
