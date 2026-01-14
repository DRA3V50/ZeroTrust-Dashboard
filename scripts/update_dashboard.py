import sqlite3
from datetime import datetime
import os
from create_controls_db import db_path

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls")
data = c.fetchall()
conn.close()

# Keep order fixed
order = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]
data_sorted = sorted(data, key=lambda x: order.index(x[0]))

# Save tab-separated metrics table for README
metrics_file = "reports/metrics_table.md"
with open(metrics_file, "w") as f:
    f.write("control\tdomain\tscore\n")
    for control, domain, score in data_sorted:
        f.write(f"{control}\t{domain}\t{score}\n")
print(f"Dashboard report updated: {metrics_file}")
