# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: PartsBin
def priority_recommendations(parts):
    """Return parts sorted by urgency, then by stock level."""
    def score(part):
        if part.get("quantity", 0) <= part.get("reorder_point", 0):
            return 100
        shortage = part.get("reorder_point", 0) - part.get("quantity", 0)
        return max(0, 100 - shortage)

    return sorted(parts, key=score, reverse=True)


def urgent_parts(parts, threshold=1):
    """Return parts at or below their reorder point."""
    return [p for p in parts if p.get("quantity", 0) <= p.get("reorder_point", 0)]
