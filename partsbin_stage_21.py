# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: PartsBin
class Archive:
    def __init__(self, bin_db):
        self.bin_db = bin_db

    def archive(self, record_id):
        """Move a record to an archived state."""
        record = self.bin_db.get_record(record_id)
        if not record:
            return
        record["status"] = "archived"
        record["archived_at"] = datetime.now().isoformat()

    def restore(self, record_id):
        """Restore an archived record to active status."""
        record = self.bin_db.get_record(record_id)
        if not record:
            return
        if record["status"] != "archived":
            return
        record["status"] = "active"
        record["archived_at"] = None
