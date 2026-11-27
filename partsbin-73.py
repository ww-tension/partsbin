# === Stage 73: Add a lightweight HTML report export ===
# Project: PartsBin
def export_report(parts, filename="partsbin_report.txt"):
    with open(filename, "w") as f:
        f.write("PartsBin Inventory Report\n")
        f.write("=" * 30 + "\n\n")
        for p in parts:
            f.write(f"{p['name']} | Qty: {p['quantity']} | Reorder: {p['reorder_point']} | Supplier: {p['supplier']}\n")
