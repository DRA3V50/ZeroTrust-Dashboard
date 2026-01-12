import sqlite3
import os

# Path to the database
DB_PATH = 'data/controls.db'

# Ensure data folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def create_controls_db():
    print("Creating/updating SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the controls table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS controls (
        control_id TEXT PRIMARY KEY,
        domain TEXT NOT NULL,
        score INTEGER
    )
    ''')

    # Populate with sample data if the table is empty
    cursor.execute('SELECT COUNT(*) FROM controls')
    if cursor.fetchone()[0] == 0:
        print("Populating the database with sample data...")
        sample_data = [
            ('A.5.1', 'Information Security Policies', 80),
            ('A.6.1', 'Organization of Information Security', 75),
            ('A.8.2', 'Risk Management', 90),
            ('A.9.2', 'Access Control', 85)
        ]
        cursor.executemany('INSERT INTO controls VALUES (?, ?, ?)', sample_data)

    conn.commit()
    conn.close()
    print("Database created/updated successfully.")

if __name__ == "__main__":
    create_controls_db()
