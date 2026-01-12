import sqlite3
import os

os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/controls.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS controls (
    control_id TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    score INTEGER NOT NULL
)
""")

# Sample data
controls = [
    ("A.5.1", "Policy", 80),
    ("A.6.1", "Organization", 70),
    ("A.7.2", "Training", 60),
    ("A.9.2", "Access Control", 90)
]

for control in controls:
    c.execute("""
    INSERT OR REPLACE INTO controls (control_id, domain, score) VALUES (?, ?, ?)
    """, control)

conn.commit()
conn.close()
print("[DEBUG] Database created/populated at data/controls.db")
