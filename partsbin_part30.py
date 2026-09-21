# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: PartsBin
def parse_date(date_str):
    """Parse a date string into a datetime.date object.
    
    Supports formats: YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY.
    Raises ValueError with a clear message if parsing fails.
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError(f"Invalid date string: {date_str!r}")

    date_str = date_str.strip()

    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(
        f"Date '{date_str}' does not match any supported format. "
        "Expected YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY."
    )
