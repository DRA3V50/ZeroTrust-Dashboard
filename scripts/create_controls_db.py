import sqlite3
from pathlib import Path

# Path for database
db_path = Path("data/controls.db")

# Ensure parent directory exists
db_path.parent.mkdir(parents=True, exist_ok=True)

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect(db_path)

# Create the controls table
conn.execute('''
CREATE TABLE IF NOT EXISTS controls (
    control TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print(f"Database initialized at {db_path}")
