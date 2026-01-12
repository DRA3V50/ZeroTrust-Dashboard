import sqlite3
import pandas as pd
import os
from datetime import datetime

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect("data/controls.db")
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

report_file = "reports/latest_report.md"
now = datetime.now().strftime("%Y-%m-%d %H:%M")

with open(report_file, "w") as f:
    # Header
    f.write("# 🔒 Zero Trust Dashboard\n\n")
    f.write(f"*Report generated: {now}*\n\n")
    
    # Overview
    f.write("## 🔎 Overview\n")
    f.write("Automated real-time view of Zero Trust posture and ISO 27001 compliance.\n\n")
    
    # Metrics Table
    f.write("## ⚠️ Critical Metrics Snapshot\n")
    f.write("| Control ID | Domain | Score | Status |\n")
    f.write("|------------|--------|-------|--------|\n")
    
    for _, row in df.iterrows():
        status = "✅ Good" if row.score >= 70 else "⚠️ Needs Attention"
        f.write(f"| {row.control_id} | {row.domain} | {row.score}% | {status} |\n")
    
    f.write("\n> Updated daily along with graphs and badges, providing a quick view of areas to focus remediation.\n")
