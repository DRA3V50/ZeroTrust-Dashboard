import sqlite3
from pathlib import Path

db_path = Path("data/controls.db")

def create_db():
    db_path.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS controls (
            control TEXT PRIMARY KEY,
            domain TEXT,
            score INTEGER
        )
    """)
    # Insert dummy data if table empty
    c.execute("SELECT COUNT(*) FROM controls")
    if c.fetchone()[0] == 0:
        controls_data = [
            ("A.5.1", "InfoSec Policies", 87),
            ("A.6.1", "Org InfoSec", 92),
            ("A.8.2", "Risk Management", 79),
            ("A.9.2", "Access Control", 85),
        ]
        c.executemany("INSERT INTO controls (control, domain, score) VALUES (?, ?, ?)", controls_data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
