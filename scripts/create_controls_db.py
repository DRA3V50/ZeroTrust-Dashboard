#!/usr/bin/env python3
import sqlite3
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)
db_path = "data/controls.db"

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT,
    score INTEGER,
    last_updated TEXT
)
''')

controls = [
    ("A.5.1", "InfoSec Policies", 87),
    ("A.6.1", "Org InfoSec", 92),
    ("A.8.2", "Risk Management", 79),
    ("A.9.2", "Access Control", 85)
]

for control, domain, score in controls:
    c.execute('''
    INSERT OR REPLACE INTO controls (control, domain, score, last_updated)
    VALUES (?, ?, ?, ?)
    ''', (control, domain, score, datetime.utcnow().isoformat()))

conn.commit()
conn.close()
print(f"Database initialized at {db_path}")
