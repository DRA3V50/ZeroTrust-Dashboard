import sqlite3

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
controls_data = [
    ("A.5.1", "Identity", 85),
    ("A.6.1", "Device", 90),
    ("A.8.2", "Network", 75),
    ("A.9.2", "Data", 80)
]

c.executemany("""
INSERT OR REPLACE INTO controls (control_id, domain, score) VALUES (?, ?, ?)
""", controls_data)

conn.commit()
conn.close()
print("[DEBUG] Database created/populated at data/controls.db")
