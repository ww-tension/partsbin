# === Stage 44: Add backup creation for the data file ===
# Project: PartsBin
def create_backup(path, backup_dir="backups"):
    try:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"partsbin_{timestamp}.bak")
        shutil.copy2(path, backup_path)
        return backup_path
    except OSError as exc:
        print(f"Backup failed: {exc}")
        return None
