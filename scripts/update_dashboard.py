import sqlite3
from pathlib import Path

DB_PATH = Path("data/controls.db")
REPORT_PATH = Path("reports/latest_report.md")
REPORT_PATH.parent.mkdir(exist_ok=True)

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    cursor.execute("SELECT control, coverage FROM iso_27001")
    iso_controls = cursor.fetchall()

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()

    lines = ["# Zero-Trust Dashboard Report\n"]
    lines.append("## Zero Trust Domains\n")
    for domain, coverage in zero_trust:
        lines.append(f"- **{domain}**: {coverage}%")

    lines.append("\n## ISO 27001 Controls\n")
    for control, coverage in iso_controls:
        lines.append(f"- **{control}**: {coverage}%")

    REPORT_PATH.write_text("\n".join(lines))
    print("Dashboard report updated successfully.")

if __name__ == "__main__":
    generate_report()
