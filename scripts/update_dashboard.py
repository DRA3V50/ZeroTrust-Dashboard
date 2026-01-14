import sqlite3
import pandas as pd
from datetime import datetime
import os

# Database path
db_path = "data/controls.db"

# Create data folder if missing
os.makedirs("data", exist_ok=True)

# Connect to DB
conn = sqlite3.connect(db_path)

# Make sure table exists
conn.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT,
    score INTEGER
)
''')

# Sample update logic (replace with real metrics)
controls_data = [
    ("A.5.1", "InfoSec Policies", 87),
    ("A.6.1", "Org InfoSec", 92),
    ("A.8.2", "Risk Management", 79),
    ("A.9.2", "Access Control", 85)
]

for control, domain, score in controls_data:
    conn.execute('''
    INSERT OR REPLACE INTO controls (control, domain, score)
    VALUES (?, ?, ?)
    ''', (control, domain, score))

conn.commit()

# Save latest report
os.makedirs("reports", exist_ok=True)
report_file = f"reports/latest_report.md"
df = pd.read_sql("SELECT * FROM controls", conn)
df.to_markdown(report_file, index=False)
conn.close()

# Generate metrics table for README
metrics_md_path = "reports/metrics_table.md"
with open(metrics_md_path, "w") as f:
    f.write("| Control | Domain | Score (%) |\n")
    f.write("|---------|--------|-----------|\n")
    for _, row in df.iterrows():
        f.write(f"| {row['control']} | {row['domain']} | {row['score']} |\n")

print("Dashboard data updated successfully.")
