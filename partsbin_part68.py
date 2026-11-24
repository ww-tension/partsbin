# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: PartsBin
def changelog(entries, limit=10):
    """Build a compact changelog from the activity log."""
    if not entries:
        return "No activity recorded yet."
    lines = []
    for entry in entries[-limit:]:
        date = entry.get("date", "?")
        record = entry.get("record", entry)
        action = record.get("action", "updated")
        if action == "created":
            verb = "added"
        elif action == "deleted":
            verb = "removed"
        else:
            verb = "changed"
        lines.append(f"- {date}: {verb} {record.get('part', '?')}")
    return "\n".join(lines)
