import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "controls.db"

# Delete invalid DB file if it exists
if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create Zero Trust table
cursor.execute("""
CREATE TABLE zero_trust (
    domain TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

# Create ISO 27001 table
cursor.execute("""
CREATE TABLE iso27001 (
    control TEXT PRIMARY KEY,
    status TEXT
)
""")

# Insert sample data (you can expand later)
zero_trust_data = [
    ("Identity", 90),
    ("Device", 75),
    ("Network", 60),
    ("Application", 85),
    ("Data", 80)
]

iso_data = [
    ("A.5.1 Information security policies", "Compliant"),
    ("A.6.1 Organization of information security", "Partial"),
    ("A.7.2 Employee awareness", "Non-Compliant"),
    ("A.9.2 Access control", "Compliant")
]

cursor.executemany("INSERT INTO zero_trust(domain, coverage) VALUES (?, ?)", zero_trust_data)
cursor.executemany("INSERT INTO iso27001(control, status) VALUES (?, ?)", iso_data)

conn.commit()
conn.close()

print(f"Database created successfully at {DB_PATH}")
