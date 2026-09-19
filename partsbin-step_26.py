# === Stage 26: Add weekly summary calculations ===
# Project: PartsBin
def weekly_summary(bins):
    """Compute per-category weekly usage totals and flag low-stock alerts."""
    weekly = {}
    alerts = {}
    now = datetime.now()
    for cat, items in bins.items():
        weekly[cat] = 0
        alerts[cat] = 0
        for item in items:
            weekly[cat] += item['quantity']
            if item['quantity'] <= item['reorder'] * 0.5:
                alerts[cat] += 1
    return weekly, alerts
