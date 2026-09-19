# === Stage 27: Add monthly summary calculations ===
# Project: PartsBin
def calculate_monthly_summary(bin_data):
    """Calculate monthly summary statistics for PartsBin tracking."""
    monthly_stats = {}
    for bin_id, records in bin_data.items():
        monthly_stats[bin_id] = {}
        for rec in records:
            month = rec['date'][:7]  # YYYY-MM
            if month not in monthly_stats[bin_id]:
                monthly_stats[bin_id][month] = {
                    'total_received': 0,
                    'total_reorder': 0,
                    'unique_suppliers': set(),
                    'total_quantity': 0
                }
            stats = monthly_stats[bin_id][month]
            stats['total_received'] += rec['quantity_received']
            stats['total_reorder'] += rec['quantity_reorder']
            stats['total_quantity'] += rec['quantity']
            if rec.get('supplier'):
                stats['unique_suppliers'].add(rec['supplier'])
    return monthly_stats
