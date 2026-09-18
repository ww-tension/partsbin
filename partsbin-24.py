# === Stage 24: Add grouped summaries by category or status ===
# Project: PartsBin
def grouped_summary(parts_list, group_by='status'):
    """Return a compact grouped summary of parts by category or status."""
    groups = {}
    for p in parts_list:
        key = p.get(group_by, 'unknown')
        groups.setdefault(key, []).append(p)
    result = []
    for status, items in groups.items():
        total_qty = sum(item.get('quantity', 0) for item in items)
        low_items = [i for i in items if i.get('quantity', 0) <= i.get('reorder_point', 0)]
        result.append({
            'status': status,
            'count': len(items),
            'total_quantity': total_qty,
            'needs_reorder': len(low_items),
        })
    return result
