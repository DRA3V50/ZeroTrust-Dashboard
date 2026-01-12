import sqlite3
import pandas as pd
import os

# Path to the database and report folder
DB_PATH = 'data/controls.db'
REPORT_PATH = 'reports/latest_report.md'

# Ensure reports folder exists
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

# Function to update the dashboard
def update_dashboard():
    print("Generating latest report...")

    # Connect to SQLite database
    conn = sqlite3.connect(DB_PATH)

    # Fetch all controls data
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()

    # Save report as CSV (or markdown if you prefer)
    df.to_csv(REPORT_PATH, index=False)
    print(f"Dashboard updated and saved to {REPORT_PATH}.")

if __name__ == "__main__":
    update_dashboard()
