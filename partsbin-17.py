# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: PartsBin
def dry_run(self, action: str, parts: list) -> str:
    """Simulate a mutating command and return a dry-run summary."""
    affected = [p for p in parts if p["quantity"] != 0 or p["reorder_point"] != 0]
    if not affected:
        return "Dry run: no parts affected by this action."
    return f"Dry run: {action} would affect {len(affected)} of {len(parts)} parts."
