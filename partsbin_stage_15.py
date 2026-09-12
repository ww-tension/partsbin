# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: PartsBin
def dispatch_command(raw: str):
    """Parse a single line of user input and return a dict with action and args."""
    line = raw.strip()
    if not line:
        return {"action": "noop", "args": {}}
    parts = line.split(None, 1)
    cmd = parts[0].lower()
    rest = parts[1] if len(parts) > 1 else ""
    if cmd == "quit":
        return {"action": "quit", "args": {}}
    if cmd in ("status", "list"):
        return {"action": cmd, "args": {}}
    if cmd == "add":
        return {"action": "add", "args": {"item": rest}}
    if cmd == "remove":
        return {"action": "remove", "args": {"item": rest}}
    if cmd == "search":
        return {"action": "search", "args": {"query": rest}}
    if cmd == "history":
        return {"action": "history", "args": {}}
    if cmd == "help":
        return {"action": "help", "args": {}}
    if cmd == "stats":
        return {"action": "stats", "args": {}}
    if cmd == "import_csv":
        return {"action": "import_csv", "args": {"file": rest}}
    if cmd == "export_csv":
        return {"action": "export_csv", "args": {}}
    if cmd == "clear":
        return {"action": "clear", "args": {}}
    if cmd == "config":
        return {"action": "config", "args": {}}
    return {"action": "unknown", "args": {"raw": cmd}}
