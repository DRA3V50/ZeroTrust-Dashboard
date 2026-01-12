import sqlite3
import pandas as pd

def generate_report():
    conn = sqlite3.connect('data/controls.db')
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    df.to_markdown('reports/latest_report.md', index=False)
    conn.close()
    print("Dashboard report updated successfully.")

if __name__ == '__main__':
    generate_report()
