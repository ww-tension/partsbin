# === Stage 72: Add Markdown report export ===
# Project: PartsBin
def export_report(parts, path="partsbin_report.txt"):
    lines = []
    lines.append("PartsBin Inventory Report")
    lines.append("=" * 40)
    lines.append(f"Total items: {len(parts)}")
    lines.append(f"Total quantity: {sum(p['quantity'] for p in parts)}")
    lines.append("")
    lines.append(f"{'Name':<25}{'Qty':>6}{'Reorder':>8}{'Supplier':<20}")
    lines.append("-" * 60)
    for p in sorted(parts, key=lambda x: x['quantity']):
        supplier = p.get('supplier', 'N/A')
        supplier = supplier[:19] if supplier else 'N/A'
        lines.append(f"{p['name']:<25}{p['quantity']:>6}{p.get('reorder_point', 0):>8}{supplier:<20}")
    lines.append("")
    low = [p for p in parts if p['quantity'] <= p.get('reorder_point', 0)]
    lines.append(f"Items at or below reorder point: {len(low)}")
    for p in low:
        lines.append(f"  - {p['name']} (qty: {p['quantity']})")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return path
