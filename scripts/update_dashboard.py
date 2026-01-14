import os
import sqlite3

# Ensure tabulate is installed for Pandas markdown output
try:
    import pandas as pd
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

try:
    import tabulate
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    import tabulate

from scripts.create_controls_db import db_path  # Use proper relative import

# Ensure outputs folders exist
os.makedirs("outputs/badges", exist_ok=True)
os.makedirs("outputs/graphs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)

# Load controls into DataFrame
df = pd.read_sql("SELECT * FROM controls", conn)

# Write latest report
report_file = os.path.join("reports", "latest_report.md")
df.to_markdown(report_file, index=False)

conn.close()
print("Dashboard data updated successfully.")
