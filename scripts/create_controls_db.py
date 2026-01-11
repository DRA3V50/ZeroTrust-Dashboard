import sqlite3
from pathlib import Path

# Set paths
ROOT = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "controls.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # ensure data/ exists

# Connect to (or create) the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS zero_trust (
    domain TEXT,
    coverage INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS iso27001 (
    control TEXT,
    status TEXT,
    risk_level TEXT
)
""")

# Insert sample data (only if empty)
cursor.execute("SELECT COUNT(*) FROM zero_trust")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO zero_trust (domain, coverage) VALUES (?, ?)", [
        ('Identity', 85),
        ('Device', 75),
        ('Network', 65),
        ('Application', 90),
        ('Data', 80)
    ])

cursor.execute("SELECT COUNT(*) FROM iso27001")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO iso27001 (control, status, risk_level) VALUES (?, ?, ?)", [
        ('A.5.1 Information Security Policies','Compliant','Low'),
        ('A.6.1 Organization of Info Security','Partial','Medium'),
        ('A.7.2 Employee Awareness','Compliant','Low'),
        ('A.9.2 Access Control','Partial','Medium')
    ])

conn.commit()
conn.close()

print(f"Database created/verified at {DB_PATH}")
