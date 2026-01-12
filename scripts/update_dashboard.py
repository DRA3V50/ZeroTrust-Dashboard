import sqlite3
import pandas as pd
import os

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect("data/controls.db")
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

with open("reports/latest_report.md", "w") as f:
    f.write("# Zero Trust Dashboard\n\n")
    for _, r in df.iterrows():
        f.write(f"- **{r.control_id}** ({r.domain}): {r.score}%\n")

print("[OK] Report updated")
