import sqlite3
from pathlib import Path

DATA_DIR = Path("data")
DB_PATH = DATA_DIR / "controls.db"
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)
REPORT_PATH = REPORTS_DIR / "latest_report.md"

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch zero trust metrics
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    # Fetch ISO controls metrics
    cursor.execute("SELECT control, coverage FROM iso_controls")
    iso_controls = cursor.fetchall()

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()
    lines = ["# Zero-Trust & ISO 27001 Dashboard Report\n"]

    lines.append("## Zero-Trust Coverage\n")
    for domain, coverage in zero_trust:
        lines.append(f"- **{domain}**: {coverage}%")

    lines.append("\n## ISO 27001 Controls Coverage\n")
    for control, coverage in iso_controls:
        lines.append(f"- **{control}**: {coverage}%")

    REPORT_PATH.write_text("\n".join(lines))
    print("Dashboard report updated successfully.")

if __name__ == "__main__":
    generate_report()
