# === Stage 28: Add overdue item detection based on due dates ===
# Project: PartsBin
def detect_overdue_items(items, today=None):
    """
    Identify items whose reorder date has passed but quantity is still insufficient.
    Returns a list of dicts with item name, current quantity, reorder quantity,
    and days overdue.
    """
    if today is None:
        today = datetime.date.today()
    overdue = []
    for item in items:
        if item['quantity'] < item['reorder_quantity']:
            reorder_date = item['reorder_date']
            if isinstance(reorder_date, str):
                reorder_date = datetime.date.fromisoformat(reorder_date)
            if reorder_date <= today:
                days_overdue = (today - reorder_date).days
                overdue.append({
                    'name': item['name'],
                    'quantity': item['quantity'],
                    'reorder_quantity': item['reorder_quantity'],
                    'days_overdue': days_overdue
                })
    return overdue
