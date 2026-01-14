import sqlite3
import pandas as pd
import os
from datetime import datetime

# Paths
DB_PATH = "data/controls.db"
REPORT_PATH = "reports/latest_report.md"
README_PATH = "README.md"

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# Fetch data from database
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# --- Update latest_report.md ---
with open(REPORT_PATH, "w") as f:
    f.write("# Zero Trust Dashboard Report\n\n")
    f.write(f"_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n")
    f.write("| Control | Domain | Score (%) |\n")
    f.write("|--------|--------|-----------|\n")
    for _, r in df.iterrows():
        f.write(f"| {r.control_id} | {r.domain} | {r.score}% |\n")
print("[OK] Report updated")

# --- Update README.md metrics table dynamically ---
with open(README_PATH, "r") as f:
    readme_content = f.read()

# Build metrics table markdown
metrics_table_md = "\n| Control | Domain | Score (%) |\n|--------|--------|-----------|\n"
for _, r in df.iterrows():
    metrics_table_md += f"| {r.control_id} | {r.domain} | {r.score}% |\n"

# Replace table between markers
start_marker = "<!-- METRICS_TABLE_START -->"
end_marker = "<!-- METRICS_TABLE_END -->"

if start_marker in readme_content and end_marker in readme_content:
    pre = readme_content.split(start_marker)[0]
    post = readme_content.split(end_marker)[1]
    new_readme = f"{pre}{start_marker}\n{metrics_table_md}{end_marker}{post}"
else:
    # If markers not found, append at the end
    new_readme = f"{readme_content}\n{start_marker}\n{metrics_table_md}{end_marker}\n"

with open(README_PATH, "w") as f:
    f.write(new_readme)

print("[OK] README metrics table updated")
