import pandas as pd
import os

DB_PATH = 'data/controls.db'
REPORT_PATH = 'latest_report.md'

def update_dashboard():
    print("Generating latest report...")
    df = pd.read_sql_query("SELECT * FROM controls", f"sqlite:///{DB_PATH}")
    with open(REPORT_PATH, 'w') as f:
        f.write("# Zero Trust Dashboard - Latest Report\n\n")
        f.write("## ISO 27001 Control Scores\n\n")
        f.write(df.to_markdown(index=False))
    print(f"Report saved: {REPORT_PATH}")

if __name__ == "__main__":
    update_dashboard()
