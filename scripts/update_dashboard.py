import sqlite3
from datetime import date

DB_PATH = '../data/controls.db'
REPORT_PATH = '../reports/latest_report.md'

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust_data = cursor.fetchall()

    cursor.execute("SELECT control, status, risk_level FROM iso27001")
    iso_data = cursor.fetchall()

    conn.close()
    return zero_trust_data, iso_data

def generate_report(zero_trust, iso_controls):
    today = date.today().isoformat()
    with open(REPORT_PATH, 'w') as f:
        f.write(f"# Zero Trust Dashboard Report\n\n")
        f.write(f"**Date:** {today}\n\n")

        f.write("## Zero Trust Domain Coverage\n")
        for domain, coverage in zero_trust:
            f.write(f"- {domain}: {coverage}%\n")

        f.write("\n## ISO 27001 Control Status\n")
        for control, status, risk in iso_controls:
            f.write(f"- {control}: {status} (Risk: {risk})\n")

if __name__ == "__main__":
    zero_trust, iso_controls = fetch_metrics()
    generate_report(zero_trust, iso_controls)
