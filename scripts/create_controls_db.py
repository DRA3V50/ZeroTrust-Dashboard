import sqlite3, os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/controls.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS controls (
    control_id TEXT PRIMARY KEY,
    domain TEXT,
    score INTEGER
)
""")

# sample data
controls = [
    ("A.5.1", "Policy", 85),
    ("A.6.1", "Access Control", 75),
    ("A.8.2", "Assets", 90),
    ("A.9.2", "Monitoring", 60)
]

c.executemany("INSERT OR REPLACE INTO controls VALUES (?, ?, ?)", controls)
conn.commit()
conn.close()

print("[DEBUG] Database created/populated at data/controls.db")
