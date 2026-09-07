# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: PartsBin
def delete_part(db_path, part_id, confirm=False):
    """Delete a part from the database with an optional confirmation flag."""
    if not confirm:
        print(f"Part with ID {part_id} not confirmed for deletion.")
        return False
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM parts WHERE id = ?", (part_id,))
        deleted = cursor.rowcount
        conn.commit()
        conn.close()
        if deleted > 0:
            print(f"Part with ID {part_id} deleted successfully.")
        else:
            print(f"No part found with ID {part_id}.")
        return deleted > 0
    except sqlite3.Error as e:
        print(f"Error deleting part: {e}")
        return False
