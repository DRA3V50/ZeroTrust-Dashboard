import sqlite3
import pandas as pd

DB_PATH = "data/controls.db"
README_PATH = "README.md"

# Fetch data
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Create Markdown table
table_md = "| Control ID | Domain | Score (%) |\n"
table_md += "|-----------|--------|-----------|\n"
for _, r in df.iterrows():
    table_md += f"| {r.control_id} | {r.domain} | {r.score} |\n"

# Write to latest report
with open("reports/latest_report.md", "w") as f:
    f.write("# Zero Trust Dashboard Report\n\n")
    f.write(table_md)

# Optional: Update README dynamically
# Replace between markers <!-- START_METRICS --> ... <!-- END_METRICS -->
with open(README_PATH, "r") as f:
    readme = f.read()

start_marker = "<!-- START_METRICS -->"
end_marker = "<!-- END_METRICS -->"

if start_marker in readme and end_marker in readme:
    before = readme.split(start_marker)[0]
    after = readme.split(end_marker)[1]
    readme = before + start_marker + "\n" + table_md + "\n" + end_marker + after
    with open(README_PATH, "w") as f:
        f.write(readme)
