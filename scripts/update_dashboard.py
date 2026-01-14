import sqlite3
import os
import pandas as pd

from create_controls_db import db_path  # Correct import

# Connect to the database
conn = sqlite3.connect(db_path)

# Sample update logic (replace with real data retrieval)
controls_data = [
    ("A.5.1", "InfoSec Policies", 87),
    ("A.6.1", "Org InfoSec", 92),
    ("A.8.2", "Risk Management", 79),
    ("A.9.2", "Access Control", 85),
]

# Insert or replace data
for control, domain, score in controls_data:
    conn.execute('''
        INSERT OR REPLACE INTO controls (control, domain, score)
        VALUES (?, ?, ?)
    ''', (control, domain, score))

conn.commit()

# Generate latest report
os.makedirs("reports", exist_ok=True)
df = pd.read_sql("SELECT * FROM controls", conn)
report_file = os.path.join("reports", "latest_report.md")
df.to_markdown(report_file, index=False)
conn.close()

print("Dashboard data updated successfully.")
