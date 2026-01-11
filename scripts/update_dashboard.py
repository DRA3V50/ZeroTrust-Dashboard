import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "controls.db"
REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)
REPORT_FILE = REPORTS_DIR / "latest_report.md"

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch Zero Trust metrics
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    # Fetch ISO 27001 metrics
    cursor.execute("SELECT control, status FROM iso27001")
    iso_controls = cursor.fetchall()

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()
    lines = ["# Zero Trust & ISO 27001 Dashboard\n"]

    lines.append("## Zero Trust Coverage\n")
    for domain, coverage in zero_trust:
        lines.append(f"- **{domain}**: {coverage}%")

    lines.append("\n## ISO 27001 Controls\n")
    for control, status in iso_controls:
        lines.append(f"- **{control}**: {status}")

    REPORT_FILE.write_text("\n".join(lines))
    print(f"Dashboard report updated successfully at {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()
