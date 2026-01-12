import sqlite3
import os

DB_PATH = "data/controls.db"
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS controls (
    control_id TEXT PRIMARY KEY,
    domain TEXT,
    score INTEGER
)
""")

# Populate sample data
controls = [
    ("A.5.1", "Application", 90),
    ("A.6.1", "Data", 80),
    ("A.7.2", "Identity", 70),
    ("A.9.2", "Network", 60)
]

c.executemany("INSERT OR REPLACE INTO controls VALUES (?, ?, ?)", controls)
conn.commit()
conn.close()

print(f"[DEBUG] Database created/populated at {DB_PATH}")
