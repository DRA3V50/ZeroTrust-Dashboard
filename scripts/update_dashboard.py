import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime
from scripts.create_controls_db import db_path

# Ensure database exists
if not db_path.exists():
    from scripts.create_controls_db import db_path  # triggers creation

conn = sqlite3.connect(db_path)

# Example: Populate database with dummy values (or pull from your real source)
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

# Read data into pandas for report
df = pd.read_sql("SELECT * FROM controls", conn)

# Generate Markdown report
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

report_file = reports_dir / "latest_report.md"
df.to_markdown(report_file, index=False)

print("Dashboard data updated successfully.")
conn.close()
