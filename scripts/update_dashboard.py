import sqlite3
import pandas as pd
import os
from datetime import datetime

# Ensure directories exist
os.makedirs("reports", exist_ok=True)

DB_PATH = "data/controls.db"
REPORT_MD = "reports/latest_report.md"
README_PATH = "README.md"

# Fetch controls from SQLite database
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Update latest_report.md
with open(REPORT_MD, "w") as f:
    f.write("# Zero Trust Dashboard Report\n\n")
    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("## Zero Trust & ISO 27001 Metrics\n\n")
    for _, r in df.iterrows():
        f.write(f"- **{r.control_id}** ({r.domain}): {r.score}%\n")

print("[OK] latest_report.md updated")

# Generate Markdown table for README
table_lines = [
    "| Control ID | Domain | Score (%) |",
    "|-----------|--------|-----------|"
]

for _, r in df.iterrows():
    table_lines.append(f"| {r.control_id} | {r.domain} | {r.score} |")

table_md = "\n".join(table_lines)

# Read current README
with open(README_PATH, "r") as f:
    readme = f.read()

# Insert or replace table under "Key Metrics" section
import re
pattern = r"(## 🔑 Key Metrics\n\n)(.*?)(\n---)"
new_readme = re.sub(pattern, r"\1" + table_md + r"\3", readme, flags=re.DOTALL)

# Save updated README
with open(README_PATH, "w") as f:
    f.write(new_readme)

print("[OK] README.md metrics table updated")
