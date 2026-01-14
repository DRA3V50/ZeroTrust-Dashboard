import sqlite3
import os

# Path for database
db_path = os.path.join("data", "controls.db")

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Connect and create table
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    score INTEGER NOT NULL
)
""")

# Insert initial test data if table empty
cursor.execute("SELECT COUNT(*) FROM controls")
if cursor.fetchone()[0] == 0:
    initial_data = [
        ("A.5.1", "InfoSec Policies", 87),
        ("A.6.1", "Org InfoSec", 92),
        ("A.8.2", "Risk Management", 79),
        ("A.9.2", "Access Control", 85)
    ]
    cursor.executemany("INSERT INTO controls (control, domain, score) VALUES (?, ?, ?)", initial_data)

conn.commit()
conn.close()

print("Database created/verified successfully.")
