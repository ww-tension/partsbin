# === Stage 25: Add daily summary calculations ===
# Project: PartsBin
def daily_summary(parts_list):
    """Generate a daily summary report for the parts inventory."""
    summary = {
        "date": _get_today(),
        "total_parts": len(parts_list),
        "low_stock_parts": [p for p in parts_list if p.quantity <= p.reorder_point],
        "total_quantity": sum(p.quantity for p in parts_list),
    }
    return summary

def print_daily_summary(parts_list):
    """Print the daily summary report."""
    summary = daily_summary(parts_list)
    print(f"Daily Summary - {summary['date']}")
    print(f"Total Parts: {summary['total_parts']}")
    print(f"Total Quantity: {summary['total_quantity']}")
    if summary['low_stock_parts']:
        print(f"Low Stock Parts ({len(summary['low_stock_parts'])}):")
        for p in summary['low_stock_parts']:
            print(f"  - {p.name}: {p.quantity} remaining (reorder at {p.reorder_point})")
    else:
        print("All parts are in good stock!")

# Example usage
parts = [
    Part("Screws", 100, 50, "Supplier A"),
    Part("Nuts", 200, 100, "Supplier B"),
    Part("Washers", 50, 25, "Supplier A"),
]
print_daily_summary(parts)
