import sqlite3
from datetime import datetime
import pandas as pd
import os

from create_controls_db import db_path

os.makedirs("reports", exist_ok=True)

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

report_file = f"reports/latest_report_{datetime.utcnow().strftime('%Y-%m-%d_%H%M')}.md"
df.to_markdown(report_file, index=False)
print(f"Dashboard report updated: {report_file}")
