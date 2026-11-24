# === Stage 67: Add a function that returns key project metrics ===
# Project: PartsBin
def project_metrics(parts):
    total_parts = len(parts)
    total_quantity = sum(p['quantity'] for p in parts)
    below_reorder = [p for p in parts if p['quantity'] <= p['reorder_point']]
    out_of_stock = [p for p in parts if p['quantity'] == 0]
    total_suppliers = len(set(p['supplier'] for p in parts))
    return {
        'total_parts': total_parts,
        'total_quantity': total_quantity,
        'below_reorder': len(below_reorder),
        'out_of_stock': len(out_of_stock),
        'unique_suppliers': total_suppliers,
    }
