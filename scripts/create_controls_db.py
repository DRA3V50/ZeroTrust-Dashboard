from pathlib import Path
import sqlite3

DB_PATH = Path("data/controls.db")
DB_PATH.parent.mkdir(exist_ok=True)  # Ensure 'data/' folder exists

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables if not exist
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

# Optional: seed with initial values (can be empty or placeholders)
zero_trust_samples = [
    ("Identity", 70),
    ("Network", 85),
    ("Device", 60),
    ("Application", 90),
    ("Data", 50)
]

iso_controls_samples = [
    ("A.5.1 Information security policies", 75),
    ("A.6.1 Organization of information security", 80),
    ("A.7.2 Employee awareness", 65),
    ("A.9.2 Access control", 70)
]

cursor.executemany("INSERT OR REPLACE INTO zero_trust (domain, coverage) VALUES (?, ?)", zero_trust_samples)
cursor.executemany("INSERT OR REPLACE INTO iso_controls (control, coverage) VALUES (?, ?)", iso_controls_samples)

conn.commit()
conn.close()
print(f"Database created/updated at {DB_PATH}")
