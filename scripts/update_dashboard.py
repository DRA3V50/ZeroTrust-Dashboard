import sqlite3
import pandas as pd
import os

DB_PATH = 'data/controls.db'
REPORT_PATH = 'reports/latest_report.md'

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

def update_dashboard():
    print("Generating latest report...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()

    try:
        # Save as markdown using tabulate
        with open(REPORT_PATH, "w") as f:
            f.write(df.to_markdown(index=False))
    except ImportError:
        # Fallback: save as CSV if tabulate missing
        print("Tabulate not found, saving as CSV instead.")
        df.to_csv(REPORT_PATH, index=False)

    print(f"Dashboard updated and saved to {REPORT_PATH}.")

if __name__ == "__main__":
    update_dashboard()
