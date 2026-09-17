# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: PartsBin
def add_tag(tag: str, parts: dict) -> None:
    """Assign a tag to every part whose name contains the tag string."""
    for key, part in parts.items():
        if part["name"].lower() not in tag.lower():
            continue
        if "tags" not in part:
            part["tags"] = []
        if tag not in part["tags"]:
            part["tags"].append(tag)

def remove_tag(tag: str, parts: dict) -> None:
    """Remove a tag from every part that currently has it."""
    for key, part in parts.items():
        if "tags" not in part:
            continue
        if tag in part["tags"]:
            part["tags"].remove(tag)

def tag_summary(parts: dict, tag: str) -> dict:
    """Return counts of parts by tag for inventory reporting."""
    summary = {}
    for key, part in parts.items():
        tags = part.get("tags", [])
        if tag in tags:
            summary.setdefault(tag, {"total": 0, "value": 0.0})
            summary[tag]["total"] += 1
            summary[tag]["value"] += float(part.get("price", 0))
    return summary
