# === Stage 14: Add file load support with fallback demo data ===
# Project: PartsBin
def load_data(filepath):
    """Load parts from a JSON file or return built-in demo data."""
    try:
        import json
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return [
            {"name": "Screws", "quantity": 150, "reorder_point": 50, "supplier": "FastFix Co."},
            {"name": "Bolts", "quantity": 200, "reorder_point": 75, "supplier": "FastFix Co."},
            {"name": "Washers", "quantity": 300, "reorder_point": 100, "supplier": "MetalWorks Ltd"},
            {"name": "Nuts", "quantity": 120, "reorder_point": 40, "supplier": "MetalWorks Ltd"},
            {"name": "Gaskets", "quantity": 60, "reorder_point": 20, "supplier": "SealTech Inc"},
            {"name": "Bearings", "quantity": 25, "reorder_point": 10, "supplier": "RollerParts Co"},
        ]
