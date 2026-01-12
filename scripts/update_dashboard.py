import sqlite3
import pandas as pd

DB_PATH = 'data/controls.db'

def update_dashboard():
    print("Generating latest report...")
    conn = sqlite3.connect(DB_PATH)  # plain sqlite connection
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()

    # Save as markdown or CSV
    df.to_csv("latest_report.md", index=False)
    print("Dashboard updated.")
