import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "controls.db"
REPORT_FILE = ROOT / "reports" / "latest_report.md"

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Zero Trust
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    # ISO 27001
    cursor.execute("SELECT control, status FROM iso27001")
    iso_controls = cursor.fetchall()

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()
    lines = ["# Zero Trust Dashboard Report\n"]

    lines.append("## Zero Trust Coverage")
    for domain, coverage in zero_trust:
        lines.append(f"- {domain}: {coverage}%")

    lines.append("\n## ISO 27001 Controls")
    for control, status in iso_controls:
        lines.append(f"- {control}: {status}")

    REPORT_FILE.write_text("\n".join(lines))
    print("Dashboard report updated successfully.")

if __name__ == "__main__":
    generate_report()
