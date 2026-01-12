import sqlite3
from pathlib import Path

# Ensure data folder exists
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "controls.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop tables if exist (optional, for reset)
    cursor.execute("DROP TABLE IF EXISTS zero_trust")
    cursor.execute("DROP TABLE IF EXISTS iso_27001")

    # Create Zero Trust table
    cursor.execute("""
        CREATE TABLE zero_trust (
            domain TEXT PRIMARY KEY,
            coverage INTEGER
        )
    """)

    # Create ISO 27001 table
    cursor.execute("""
        CREATE TABLE iso_27001 (
            control TEXT PRIMARY KEY,
            coverage INTEGER
        )
    """)

    # Sample initial data
    zero_trust_data = [
        ("Identity", 80),
        ("Device", 70),
        ("Network", 60),
        ("Application", 90),
        ("Data", 85)
    ]
    iso_data = [
        ("A.5.1 Information security policies", 75),
        ("A.6.1 Organization of information security", 80),
        ("A.7.2 Employee awareness", 70),
        ("A.9.2 Access control", 65)
    ]

    cursor.executemany("INSERT INTO zero_trust VALUES (?,?)", zero_trust_data)
    cursor.executemany("INSERT INTO iso_27001 VALUES (?,?)", iso_data)

    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    create_db()
