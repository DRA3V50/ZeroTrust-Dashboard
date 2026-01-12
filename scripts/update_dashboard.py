import sqlite3
import pandas as pd
import os

DB_PATH = 'data/controls.db'
REPORT_PATH = 'reports/latest_report.md'

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

def update_dashboard():
    print("[DEBUG] Generating latest report...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    try:
        df.to_markdown(REPORT_PATH, index=False)
    except:
        df.to_csv(REPORT_PATH, index=False)  # fallback if tabulate not installed
    print(f"[DEBUG] Dashboard updated: {REPORT_PATH}")

if __name__ == "__main__":
    update_dashboard()
