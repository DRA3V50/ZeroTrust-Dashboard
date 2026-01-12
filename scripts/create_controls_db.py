import sqlite3
import os
import random  # optional for random scores

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

# Sample data with random scores for dynamic updates
controls = [
    ("A.5.1", "Policy", random.randint(60, 100)),
    ("A.6.1", "Access Control", random.randint(60, 100)),
    ("A.8.2", "Assets", random.randint(60, 100)),
    ("A.9.2", "Monitoring", random.randint(60, 100))
]

c.executemany("INSERT OR REPLACE INTO controls VALUES (?, ?, ?)", controls)
conn.commit()
conn.close()
print("[DEBUG] Database created/populated at data/controls.db")
