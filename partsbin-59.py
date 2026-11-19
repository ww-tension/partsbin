# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: PartsBin
def bulk_delete(parts, confirm_flag):
    if not confirm_flag:
        return parts, 0
    initial_count = len(parts)
    remaining = [p for p in parts if not p.get("delete", False)]
    deleted = initial_count - len(remaining)
    return remaining, deleted
