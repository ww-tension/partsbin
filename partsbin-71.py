# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: PartsBin
import random

def seed_demo_data(parts, suppliers, seed=20240719):
    """Populate parts, suppliers, and quantities with deterministic demo data.

    Each call with the same seed yields identical data. Reorder points are
    derived from average quantities so the demo looks realistic.
    """
    random.seed(seed)
    demo_suppliers = ["Acme Parts Co.", "Global Supply", "QuickFix Industrial"]
    demo_names = [
        "M4x8 Hex Bolt", "1/4 in Brass Tube", "LED 5050 Strip",
        "Nitrile Gloves", "USB-C Cable", "9V Alkaline Battery",
        "M3 Nut", "Silicone Heat Shrink", "Solder Wire", "Phillips Screwdriver",
    ]
    for i, name in enumerate(demo_names):
        if name not in parts:
            parts[name] = {"reorder_point": 10, "supplier": None}
        if parts[name]["supplier"] is None:
            parts[name]["supplier"] = demo_suppliers[i % len(demo_suppliers)]
        if "quantity" not in parts[name]:
            parts[name]["quantity"] = random.randint(5, 40)
    if not suppliers:
        suppliers.update({s: 0 for s in demo_suppliers})
    return parts, suppliers
