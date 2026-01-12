import sqlite3
import pandas as pd
import os
from datetime import datetime

os.makedirs("reports", exist_ok=True)

DB_PATH = "data/controls.db"
README_PATH = "README.md"
REPORT_PATH = "reports/latest_report.md"

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_md_table(df):
    table = "| Control ID | Domain | Score (%) |\n"
    table += "|------------|--------|-----------|\n"
    for _, row in df.iterrows():
        table += f"| {row['control_id']} | {row['domain']} | {row['score']} |\n"
    return table

def update_latest_report(df):
    with open(REPORT_PATH, "w") as f:
        f.write("# Zero Trust Dashboard Report\n\n")
        f.write(generate_md_table(df))
    print("[OK] Latest report updated")

def update_readme_table(df):
    table_md = generate_md_table(df)
    readme_lines = []
    if os.path.exists(README_PATH):
        with open(README_PATH, "r") as f:
            readme_lines = f.readlines()

    start_tag = "<!-- METRICS_TABLE_START -->\n"
    end_tag = "<!-- METRICS_TABLE_END -->\n"

    # Remove old table if exists
    inside_table = False
    new_lines = []
    for line in readme_lines:
        if line == start_tag:
            inside_table = True
            continue
        if line == end_tag:
            inside_table = False
            continue
        if not inside_table:
            new_lines.append(line)

    # Insert new table
    new_lines.append(start_tag)
    new_lines.append(table_md)
    new_lines.append(end_tag)

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)

    print("[OK] README metrics table updated")

if __name__ == "__main__":
    df = fetch_controls()
    update_latest_report(df)
    update_readme_table(df)
