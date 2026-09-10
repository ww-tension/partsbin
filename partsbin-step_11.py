# === Stage 11: Add JSON export for the current application state ===
# Project: PartsBin
def export_state_json():
    state = {
        "parts": [],
        "suppliers": [],
        "transactions": [],
        "metadata": {
            "version": 3,
            "exported_at": _now_iso()
        }
    }
    for part in parts:
        state["parts"].append({
            "id": part["id"],
            "name": part["name"],
            "quantity": part["quantity"],
            "reorder_point": part["reorder_point"],
            "supplier_id": part["supplier_id"]
        })
    for supplier in suppliers:
        state["suppliers"].append({
            "id": supplier["id"],
            "name": supplier["name"],
            "email": supplier["email"]
        })
    for tx in transactions:
        state["transactions"].append({
            "id": tx["id"],
            "type": tx["type"],
            "part_id": tx["part_id"],
            "quantity": tx["quantity"],
            "timestamp": tx["timestamp"]
        })
    return state
