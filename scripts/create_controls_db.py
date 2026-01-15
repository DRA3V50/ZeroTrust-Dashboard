#!/usr/bin/env python3
import sqlite3
import os
from datetime import datetime
import random

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
    ("A.5.1", "InfoSec Policies"),
    ("A.6.1", "Org InfoSec"),
    ("A.8.2", "Risk Management"),
    ("A.9.2", "Access Control")
]

for control, domain in controls:
    # Generate random score 0-100
    score = random.randint(0, 100)
    c.execute('''
    INSERT OR REPLACE INTO controls (control, domain, score, last_updated)
    VALUES (?, ?, ?, ?)
    ''', (control, domain, score, datetime.utcnow().isoformat()))

conn.commit()
conn.close()
print(f"Database updated with random scores at {db_path}")
