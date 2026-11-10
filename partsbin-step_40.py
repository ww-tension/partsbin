# === Stage 40: Add plain text report export ===
# Project: PartsBin
def export_report(parts, path):
    with open(path, "w") as f:
        f.write("PARTSBIN INVENTORY REPORT\n")
        f.write("=========================\n\n")
        f.write("Part Name        Qty    Reorder    Supplier\n")
        f.write("---------------  -----  ---------  --------------\n")
        for p in parts:
            name = p["name"][:16].ljust(16)
            qty = str(p["quantity"]).ljust(6)
            reorder = str(p["reorder_point"]).ljust(9)
            supplier = p["supplier"][:14].ljust(14)
            f.write(f"{name}{qty}{reorder}{supplier}\n")
        low = [p for p in parts if p["quantity"] <= p["reorder_point"]]
        f.write(f"\n{len(low)} part(s) at or below reorder point.\n")
