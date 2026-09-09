# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: PartsBin
def format_parts_table(parts, columns=None):
    """Compact console table for PartsBin inventory.

    Args:
        parts: list of dicts with keys: id, name, qty, reorder_point, supplier.
        columns: optional list of column names to display.

    Returns:
        formatted string suitable for print().
    """
    if not parts:
        return "No parts in inventory."

    if columns is None:
        columns = ["id", "name", "qty", "reorder_point", "supplier"]

    header = " | ".join(columns)
    separator = "-" * (len(header)) + "|"
    lines = [header, separator]

    for p in parts:
        row = " | ".join(str(p.get(col, "N/A")) for col in columns)
        lines.append(row)

    return "\n".join(lines)


def format_part_detail(part):
    """Single-part detail block for console output.

    Args:
        part: dict with keys: id, name, qty, reorder_point, supplier, location.

    Returns:
        formatted string with label and value pairs.
    """
    detail_keys = ["id", "name", "qty", "reorder_point", "supplier", "location"]
    lines = []
    for key in detail_keys:
        value = part.get(key, "N/A")
        if key == "qty":
            status = "LOW" if int(value) <= int(part.get("reorder_point", 0)) else "OK"
            lines.append(f"{key.upper()}: {value} [{status}]")
        elif key == "reorder_point":
            lines.append(f"{key.upper()}: {value}")
        else:
            lines.append(f"{key.upper()}: {value}")
    return "\n".join(lines)
