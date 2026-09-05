# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: PartsBin
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Supplier:
    name: str
    email: str
    phone: Optional[str] = None
    active: bool = True

@dataclass
class Part:
    name: str
    part_number: str
    description: str = ""
    unit: str = "pcs"

@dataclass
class Bin:
    name: str
    location: str
    capacity: int = 0
    active: bool = True

@dataclass
class InventoryItem:
    part: Part
    bin: Bin
    supplier: Supplier
    quantity: int = 0
    reorder_point: int = 0
    last_received: Optional[date] = None
    last_ordered: Optional[date] = None
