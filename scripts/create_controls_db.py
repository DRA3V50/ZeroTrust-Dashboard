import sqlite3
import os

# Path to database
db_path = os.path.join("data", "controls.db")
os.makedirs("data", exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print(f"Database initialized at {db_path}")
