# === Stage 18: Add an activity log with timestamps and action names ===
# Project: PartsBin
import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, item, user):
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'action': action,
            'item': item,
            'user': user,
        }
        self.entries.append(entry)
        print(f"[{entry['timestamp']}] {entry['action']}: {entry['item']} by {entry['user']}")
