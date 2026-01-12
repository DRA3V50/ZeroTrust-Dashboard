import sqlite3
from pathlib import Path

# Define database path
DB_PATH = Path("data/controls.db")
DB_PATH.parent.mkdir(exist_ok=True)  # create 'data' folder if it doesn't exist

# Remove old file if corrupt
if DB_PATH.exists():
    DB_PATH.unlink()

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE zero_trust (
    domain TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

cursor.execute("""
CREATE TABLE iso_controls (
    control_id TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

# Example data
zero_trust_data = [
    ("Identity", 90),
    ("Device", 85),
    ("Network", 75),
    ("Application", 80),
    ("Data", 70),
]

iso_controls_data = [
    ("A.5.1", 80),
    ("A.6.1", 75),
    ("A.7.2", 65),
    ("A.9.2", 70),
]

cursor.executemany("INSERT INTO zero_trust(domain, coverage) VALUES (?, ?)", zero_trust_data)
cursor.executemany("INSERT INTO iso_controls(control_id, coverage) VALUES (?, ?)", iso_controls_data)

conn.commit()
conn.close()

print("Controls database created/updated successfully.")
