import sqlite3
import pandas as pd
import os

os.makedirs("reports", exist_ok=True)
DB_PATH = "data/controls.db"

def update_dashboard():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    
    report_path = "reports/latest_report.md"
    df.to_markdown(index=False)
    with open(report_path, "w") as f:
        f.write("# Latest Zero Trust Dashboard Report\n\n")
        f.write(df.to_markdown(index=False))
    print(f"[DEBUG] Latest report saved: {report_path}")

if __name__ == "__main__":
    update_dashboard()
