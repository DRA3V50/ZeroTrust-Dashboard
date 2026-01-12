import sqlite3
import pandas as pd

def generate_report():
    conn = sqlite3.connect('data/controls.db')
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()

    try:
        df.to_markdown('reports/latest_report.md', index=False)
        print("Dashboard report updated successfully (Markdown).")
    except ImportError:
        # fallback to CSV if tabulate missing
        df.to_csv('reports/latest_report.csv', index=False)
        print("Tabulate not found. Saved report as CSV instead.")

if __name__ == '__main__':
    generate_report()
