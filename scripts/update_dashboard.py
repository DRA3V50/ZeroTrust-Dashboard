import sqlite3
from pathlib import Path
from create_controls_db import create_db, db_path

# Ensure database exists
create_db()

# Connect to DB
conn = sqlite3.connect(db_path)

# Read controls data
try:
    import pandas as pd
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Save a latest report
Path("reports").mkdir(exist_ok=True)
report_file = Path("reports/latest_report.md")
df.to_markdown(report_file, index=False)
print("Dashboard data updated successfully.")
