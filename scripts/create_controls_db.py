import sqlite3
from pathlib import Path

# Ensure data folder exists
DB_PATH = Path("data/controls.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Connect or create DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create Zero Trust table
cursor.execute("""
CREATE TABLE IF NOT EXISTS zero_trust (
    domain TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

# Create ISO 27001 controls table
cursor.execute("""
CREATE TABLE IF NOT EXISTS iso_controls (
    control TEXT PRIMARY KEY,
    coverage INTEGER
)
""")

conn.commit()
conn.close()
print("Database ready ✅")
