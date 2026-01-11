import sqlite3
from pathlib import Path

# Ensure data folder exists
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "controls.db"

# Connect (creates DB if not exists)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS zero_trust (
    domain TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS iso_controls (
    control TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

# Insert sample data if tables empty
cursor.execute("SELECT COUNT(*) FROM zero_trust")
if cursor.fetchone()[0] == 0:
    zero_trust_sample = [
        ("Identity", 90),
        ("Device", 85),
        ("Network", 70),
        ("Application", 75),
        ("Data", 80),
    ]
    cursor.executemany("INSERT INTO zero_trust (domain, coverage) VALUES (?, ?)", zero_trust_sample)

cursor.execute("SELECT COUNT(*) FROM iso_controls")
if cursor.fetchone()[0] == 0:
    iso_sample = [
        ("A.5.1 Information security policies", 80),
        ("A.6.1 Organization of information security", 70),
        ("A.7.2 Employee awareness", 60),
        ("A.9.2 Access control", 75)
    ]
    cursor.executemany("INSERT INTO iso_controls (control, coverage) VALUES (?, ?)", iso_sample)

conn.commit()
conn.close()

print("Database ready at", DB_PATH)
