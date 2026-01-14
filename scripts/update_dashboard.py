import sqlite3
import pandas as pd
from pathlib import Path

# Database path
db_path = Path("data/controls.db")

# Create the data directory if it doesn't exist
db_path.parent.mkdir(parents=True, exist_ok=True)

# Connect to SQLite DB (creates if missing)
conn = sqlite3.connect(db_path)

# Initialize controls table if not exists
conn.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT,
    score INTEGER
)
''')

# Sample data (can be replaced with real metrics)
controls_data = [
    ("A.5.1", "InfoSec Policies", 87),
    ("A.6.1", "Org InfoSec", 92),
    ("A.8.2", "Risk Management", 79),
    ("A.9.2", "Access Control", 85)
]

# Upsert controls
for control, domain, score in controls_data:
    conn.execute('''
    INSERT INTO controls (control, domain, score)
    VALUES (?, ?, ?)
    ON CONFLICT(control) DO UPDATE SET score=excluded.score
    ''', (control, domain, score))

conn.commit()
conn.close()
print("Dashboard data updated successfully.")
