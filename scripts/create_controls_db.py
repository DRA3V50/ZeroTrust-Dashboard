import sqlite3
from pathlib import Path

# Paths
data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)
db_path = data_dir / "controls.db"

# Connect to database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')

# Optional: populate with default controls if table is empty
default_controls = [
    ("A.5.1", "InfoSec Policies", 0),
    ("A.6.1", "Org InfoSec", 0),
    ("A.8.2", "Risk Management", 0),
    ("A.9.2", "Access Control", 0)
]

for control, domain, score in default_controls:
    c.execute('INSERT OR IGNORE INTO controls (control, domain, score) VALUES (?, ?, ?)',
              (control, domain, score))

conn.commit()
conn.close()
print("Database initialized successfully.")
