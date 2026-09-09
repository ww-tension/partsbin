# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: PartsBin
def filter_items(items, **kwargs):
    """Filter parts by status, category, owner, or tag.
    
    Args:
        items: list of dict with keys 'status', 'category', 'owner', 'tags'.
        **kwargs: keyword filters. Each value is accepted if it matches exactly
                 or is a list/tuple of allowed values.
    
    Returns:
        A new list containing only items that satisfy all provided filters.
    """
    if not items:
        return []
    
    filtered = items
    
    for key, allowed in kwargs.items():
        if key not in ("status", "category", "owner", "tags"):
            raise ValueError(f"Unknown filter key: {key}")
        
        if allowed is None:
            continue
        
        if isinstance(allowed, (list, tuple)):
            allowed_set = set(allowed)
        else:
            allowed_set = {allowed}
        
        filtered = [
            item for item in filtered
            if item.get(key, "") in allowed_set
        ]
    
    return filtered
