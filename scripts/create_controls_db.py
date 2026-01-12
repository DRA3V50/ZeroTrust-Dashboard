import sqlite3

# Create SQLite DB
conn = sqlite3.connect("data/controls.db")
c = conn.cursor()

# Drop table if exists
c.execute("DROP TABLE IF EXISTS controls")

# Create controls table
c.execute("""
CREATE TABLE controls (
    control_id TEXT,
    domain TEXT,
    score INTEGER
)
""")

# Insert sample data
controls = [
    ("A.5.1", "Identity", 80),
    ("A.6.1", "Device", 70),
    ("A.8.2", "Network", 60),
    ("A.9.2", "Data", 90)
]
c.executemany("INSERT INTO controls VALUES (?, ?, ?)", controls)
conn.commit()
conn.close()
print("[DEBUG] Database created/populated at data/controls.db")
