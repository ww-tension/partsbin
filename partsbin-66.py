# === Stage 66: Add export of a short status dashboard ===
# Project: PartsBin
def print_status_dashboard(parts):
    total_items = len(parts)
    low_stock = [p for p in parts if p["quantity"] <= p["reorder_point"]]
    out_of_stock = [p for p in parts if p["quantity"] == 0]
    total_quantity = sum(p["quantity"] for p in parts)
    total_reorder = sum(p["reorder_point"] for p in parts if p["quantity"] <= p["reorder_point"])
    print("=" * 40)
    print("PARTS BIN STATUS DASHBOARD")
    print("=" * 40)
    print(f"Total part types : {total_items}")
    print(f"Total quantity   : {total_quantity}")
    print(f"Items low on stock: {len(low_stock)}")
    print(f"Items out of stock: {len(out_of_stock)}")
    print(f"Reorder needed   : {total_reorder} units")
    print("-" * 40)
    if out_of_stock:
        print("OUT OF STOCK:")
        for p in out_of_stock:
            print(f"  - {p['name']} (SKU: {p['sku']})")
    if low_stock and not out_of_stock:
        print("LOW STOCK:")
        for p in low_stock:
            print(f"  - {p['name']} (SKU: {p['sku']}) qty={p['quantity']}/{p['reorder_point']}")
    else:
        print("All parts are within stock levels.")
    print("=" * 40)
