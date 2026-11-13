# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: PartsBin
def demo_scenario():
    parts = {
        "P001": {"name": "Screws", "qty": 50, "reorder": 20, "supplier": "HardwareCo"},
        "P002": {"name": "Washers", "qty": 5, "reorder": 10, "supplier": "FastenerPlus"},
        "P003": {"name": "Gloves", "qty": 100, "reorder": 30, "supplier": "SafetySupply"},
    }

    print("PartsBin Demo")
    print("=" * 30)

    for code, part in parts.items():
        status = "LOW STOCK" if part["qty"] <= part["reorder"] else "OK"
        print(f"{code} {part['name']}: {part['qty']} units (reorder at {part['reorder']}) - {status}")

    for code, part in parts.items():
        if part["qty"] <= part["reorder"]:
            print(f"Reorder {part['name']} from {part['supplier']}")

    parts["P004"] = {"name": "Adhesive", "qty": 12, "reorder": 8, "supplier": "ChemSupply"}
    print(f"Added {parts['P004']['name']}")
    for code, part in sorted(parts.items()):
        print(f"{code} {part['name']}: {part['qty']} units from {part['supplier']}")

    parts["P002"]["qty"] += 25
    print(f"Received 25 Washers, new total: {parts['P002']['qty']}")
    for code, part in parts.items():
        if part["qty"] <= part["reorder"]:
            print(f"Reorder {part['name']} from {part['supplier']}")

    parts["P002"]["qty"] -= 10
    print(f"Used 10 Washers, new total: {parts['P002']['qty']}")
    for code, part in parts.items():
        if part["qty"] <= part["reorder"]:
            print(f"Reorder {part['name']} from {part['supplier']}")

    print("Demo complete")
