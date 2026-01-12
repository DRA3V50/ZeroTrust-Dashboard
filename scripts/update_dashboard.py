from pathlib import Path
import sqlite3

# Paths
DB_PATH = Path("data/controls.db")
REPORT_PATH = Path("reports/latest_report.md")

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch zero-trust metrics
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = [(row[0], int(row[1])) for row in cursor.fetchall()]

    # Fetch ISO metrics
    cursor.execute("SELECT control, coverage FROM iso_controls")
    iso_controls = [(row[0], int(row[1])) for row in cursor.fetchall()]

    conn.close()
    return zero_trust, iso_controls

def generate_report():
    zero_trust, iso_controls = fetch_metrics()
    
    with open(REPORT_PATH, "w") as f:
        f.write("# Zero Trust Dashboard Report\n\n")
        f.write("## Zero Trust Domains\n")
        for domain, coverage in zero_trust:
            f.write(f"- **{domain}**: {coverage}%\n")
        f.write("\n## ISO Controls\n")
        for control, coverage in iso_controls:
            f.write(f"- **{control}**: {coverage}%\n")
    
    print("Dashboard report updated successfully.")

if __name__ == "__main__":
    generate_report()
