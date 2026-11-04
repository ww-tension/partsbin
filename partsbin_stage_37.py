# === Stage 37: Add recommendations for the next useful action ===
# Project: PartsBin
def suggest_next_action(parts):
    actions = []
    for part in parts:
        if part["quantity"] <= part["reorder_point"]:
            actions.append(("reorder", part["name"]))
        elif part["supplier"] is None:
            actions.append(("add_supplier", part["name"]))
        elif part["quantity"] == 0:
            actions.append(("purchase", part["name"]))
    if not actions:
        low = sorted(
            [(p["name"], p["quantity"], p["reorder_point"]) for p in parts],
            key=lambda x: x[2] - x[1],
        )
        if low:
            actions.append(("review", low[0][0]))
    return actions
