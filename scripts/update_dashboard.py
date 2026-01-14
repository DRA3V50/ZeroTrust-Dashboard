import sqlite3
import pandas as pd
import os
from datetime import datetime

from create_controls_db import db_path

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect(db_path)

# Read current controls
df = pd.read_sql("SELECT * FROM controls", conn)

# Update example: randomly adjust scores by +/- 5% for demo purposes
import random
df['score'] = df['score'].apply(lambda x: max(0, min(100, x + random.randint(-5, 5))))

# Save updated values back to DB
df.to_sql("controls", conn, if_exists="replace", index=False)

# Write Markdown report
report_file = os.path.join("reports", f"latest_report.md")
df.to_markdown(report_file, index=False)

print("Dashboard data updated successfully.")
