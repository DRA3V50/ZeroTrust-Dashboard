import sqlite3

DB_PATH = 'data/controls.db'

def create_controls_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS controls (
            control_id TEXT PRIMARY KEY,
            domain TEXT,
            score INTEGER
        )
    """)

    # Optional: insert example controls if empty
    cursor.execute("SELECT COUNT(*) FROM controls")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ('A.5.1', 'Policy', 80),
            ('A.6.1', 'Organization', 75),
            ('A.7.2', 'Asset Management', 90),
            ('A.9.2', 'Access Control', 85)
        ]
        cursor.executemany("INSERT INTO controls (control_id, domain, score) VALUES (?, ?, ?)", sample_data)

    conn.commit()
    conn.close()
    print("Controls database created/updated successfully.")

if __name__ == "__main__":
    create_controls_db()
