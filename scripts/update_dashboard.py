import sqlite3
import os

DB_PATH = 'data/controls.db'
REPORT_PATH = 'reports/latest_report.md'

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

def update_dashboard():
    print("Generating latest report...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT control_id, domain, score FROM controls")
    rows = cursor.fetchall()
    conn.close()

    with open(REPORT_PATH, "w") as f:
        f.write("# Zero Trust Dashboard Report\n\n")
        f.write("## Zero Trust Domains\n")
        domain_scores = {}
        for control_id, domain, score in rows:
            domain_scores[domain] = max(domain_scores.get(domain,0), score)
        for domain, score in domain_scores.items():
            f.write(f"- {domain}: {score}% coverage\n")

        f.write("\n## ISO 27001 Controls\n")
        for control_id, domain, score in rows:
            f.write(f"- {control_id} ({domain}): {score}% coverage\n")
    
    print(f"Dashboard updated at {REPORT_PATH}")

if __name__ == "__main__":
    update_dashboard()
