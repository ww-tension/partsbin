# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: PartsBin
def format_inventory_line(part):
    """Return a single readable line describing a part and its stock status."""
    if part.quantity <= part.reorder_point:
        status = "LOW"
    elif part.quantity == 0:
        status = "OUT"
    else:
        status = "OK"
    return f"{part.name} (SKU {part.sku}): {part.quantity} in stock | reorder at {part.reorder_point} | {status} | supplier: {part.supplier}"


def find_low_stock_parts(parts, threshold=None):
    """Return the subset of parts that need attention based on stock or reorder rules.

    A part is returned if its quantity is zero, below its reorder point, or
    below an optional numeric threshold when provided.
    """
    if threshold is None:
        return [p for p in parts if p.quantity <= p.reorder_point]
    return [p for p in parts if p.quantity <= threshold]


def total_quantity(parts):
    """Return the combined stock quantity across all provided parts."""
    return sum(part.quantity for part in parts)


def average_reorder_point(parts):
    """Return the mean reorder point across all provided parts, or zero if empty."""
    if not parts:
        return 0
    return sum(part.reorder_point for part in parts) / len(parts)


def group_parts_by_supplier(parts):
    """Return a dictionary mapping each supplier name to its list of parts."""
    grouped = {}
    for part in parts:
        grouped.setdefault(part.supplier, []).append(part)
    return grouped


def sort_parts_by_name(parts):
    """Return a new list of parts sorted alphabetically by name."""
    return sorted(parts, key=lambda part: part.name)


def sort_parts_by_quantity(parts):
    """Return a new list of parts sorted by quantity in descending order."""
    return sorted(parts, key=lambda part: part.quantity, reverse=True)


def find_part_by_sku(parts, sku):
    """Return the first part whose SKU matches the given value, or None if not found."""
    for part in parts:
        if part.sku == sku:
            return part
    return None


def find_part_by_name(parts, name):
    """Return the first part whose name matches the given value, or None if not found."""
    for part in parts:
        if part.name == name:
            return part
    return None


def count_low_stock_parts(parts):
    """Return the number of parts currently at or below their reorder point."""
    return sum(1 for part in parts if part.quantity <= part.reorder_point)


def parts_needing_order(parts):
    """Return the names of all parts that are out of stock or below their reorder point."""
    return [part.name for part in parts if part.quantity <= part.reorder_point]


def format_summary_report(parts):
    """Return a multi-line human-readable summary of the whole inventory."""
    lines = [
        f"Total parts: {len(parts)}",
        f"Total quantity: {total_quantity(parts)}",
        f"Average reorder point: {average_reorder_point(parts):.2f}",
        f"Low stock parts: {count_low_stock_parts(parts)}",
        f"Out of stock: {sum(1 for part in parts if part.quantity == 0)}",
        "",
        "Parts by supplier:",
    ]
    for supplier, group in sorted(group_parts_by_supplier(parts).items()):
        lines.append(f"  {supplier}: {len(group)} part(s)")
    return "\n".join(lines)
