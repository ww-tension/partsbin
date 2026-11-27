# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: PartsBin
def snapshot_diff(before, after, fields=("id", "name", "quantity", "reorder_point", "supplier")):
    before = dict(before)
    after = dict(after)
    removed = sorted(k for k in before if k not in after)
    added = sorted(k for k in after if k not in before)
    changed = {}
    for key in before:
        if key in after and before[key] != after[key]:
            changed[key] = (before[key], after[key])
    return {"removed": removed, "added": added, "changed": changed}
