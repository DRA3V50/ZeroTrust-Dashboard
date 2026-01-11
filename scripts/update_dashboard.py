import sqlite3
from pathlib import Path

DB_PATH = Path("data/controls.db")
REPORT_PATH = Path("reports/latest_report.md")
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    cursor.execute("SELECT control, coverage FROM iso_controls")
    iso_controls = cursor.fetchall()

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()
    with open(REPORT_PATH, "w") as f:
        f.write("# Zero Trust & ISO 27001 Dashboard Report\n\n")

        f.write("## Zero Trust Coverage\n")
        if zero_trust:
            for domain, coverage in zero_trust:
                f.write(f"- {domain}: {coverage}%\n")
        else:
            f.write("No data yet.\n")

        f.write("\n## ISO 27001 Controls Coverage\n")
        if iso_controls:
            for control, coverage in iso_controls:
                f.write(f"- {control}: {coverage}%\n")
        else:
            f.write("No data yet.\n")

    print("Dashboard report updated successfully ✅")

if __name__ == "__main__":
    generate_report()
