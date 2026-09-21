# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: PartsBin
def upcoming_reorder(items, days_ahead=30):
    """Return items whose estimated reorder date is within `days_ahead` days."""
    today = datetime.date.today()
    upcoming = []
    for item in items:
        if item.reorder_date is None:
            continue
        delta = (item.reorder_date - today).days
        if 0 <= delta <= days_ahead:
            upcoming.append({
                'name': item.name,
                'qty': item.quantity,
                'reorder_date': item.reorder_date.isoformat(),
                'days_left': delta,
            })
    upcoming.sort(key=lambda x: x['days_left'])
    return upcoming
