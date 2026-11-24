# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: PartsBin
def reset_demo_data(db_path):
    if not db_path:
        return
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS parts")
    cur.execute("DROP TABLE IF EXISTS suppliers")
    cur.execute("DROP TABLE IF EXISTS bins")
    cur.execute("CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT, contact TEXT, email TEXT)")
    cur.execute("CREATE TABLE parts (part_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, reorder_point INTEGER, supplier_id INTEGER)")
    cur.execute("CREATE TABLE bins (bin_id INTEGER PRIMARY KEY, location TEXT, part_id INTEGER)")
    cur.execute("INSERT INTO suppliers VALUES (1, 'Fasteners Co', 'orders@fasteners.co', 'orders@fasteners.co')")
    cur.execute("INSERT INTO suppliers VALUES (2, 'Electro Supply', 'sales@electro.com', 'sales@electro.com')")
    cur.execute("INSERT INTO parts VALUES (1, 'M4 Bolt', 100, 20, 1)")
    cur.execute("INSERT INTO parts VALUES (2, '10mm Nut', 45, 15, 1)")
    cur.execute("INSERT INTO parts VALUES (3, 'LED 5mm Red', 8, 10, 2)")
    cur.execute("INSERT INTO parts VALUES (4, 'Resistor 1k', 250, 50, 2)")
    cur.execute("INSERT INTO bins VALUES (1, 'A1', 1)")
    cur.execute("INSERT INTO bins VALUES (2, 'A2', 2)")
    cur.execute("INSERT INTO bins VALUES (3, 'B1', 3)")
    cur.execute("INSERT INTO bins VALUES (4, 'B2', 4)")
    conn.commit()
    conn.close()
    print("Demo data reset complete.")
