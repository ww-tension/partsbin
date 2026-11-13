# === Stage 46: Add a schema version field and migration helper ===
# Project: PartsBin
SCHEMA_VERSION = 1

MIGRATIONS = {
    1: "initial schema with id, name, quantity, reorder_point, supplier",
}


def apply_migrations(db_path, target_version=SCHEMA_VERSION):
    if not os.path.exists(db_path):
        with open(db_path, "w") as f:
            f.write("")
    with open(db_path) as f:
        current_version = int(f.read().strip() or "0")
    for version, description in sorted(MIGRATIONS.items()):
        if version > current_version:
            print(f"applying migration to version {version}: {description}")
            current_version = version
    with open(db_path, "w") as f:
        f.write(str(current_version))


def current_schema_version(db_path):
    if not os.path.exists(db_path):
        return 0
    with open(db_path) as f:
        return int(f.read().strip() or "0")
