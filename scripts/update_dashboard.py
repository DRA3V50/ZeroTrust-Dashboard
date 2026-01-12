import sqlite3, pandas as pd, os
from datetime import datetime

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect("data/controls.db")
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
report_file = f"reports/latest_report_{timestamp}.md"

with open(report_file, "w") as f:
    f.write(f"# Zero Trust Dashboard Report ({timestamp})\n\n")
    f.write("## Zero Trust Domains & ISO 27001 Controls\n")
    for _, r in df.iterrows():
        f.write(f"- **{r.control_id}** ({r.domain}): {r.score}%\n")

print(f"[OK] Report updated: {report_file}")
