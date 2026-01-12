import sqlite3
import os

DB_PATH = 'data/controls.db'
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create controls table
    c.execute('''
        CREATE TABLE IF NOT EXISTS controls (
            control_id TEXT PRIMARY KEY,
            domain TEXT,
            score INTEGER
        )
    ''')

    # Insert sample data
    sample_data = [
        ("A.5.1", "Identity", 85),
        ("A.6.1", "Device", 75),
        ("A.7.2", "Network", 65),
        ("A.9.2", "Data", 90),
    ]
    c.executemany('''
        INSERT OR REPLACE INTO controls (control_id, domain, score)
        VALUES (?, ?, ?)
    ''', sample_data)

    conn.commit()
    conn.close()
    print("[DEBUG] Database created and populated at", DB_PATH)

if __name__ == "__main__":
    create_db()
