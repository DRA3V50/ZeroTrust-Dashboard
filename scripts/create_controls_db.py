import sqlite3

def create_db():
    conn = sqlite3.connect('data/controls.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS controls (
            control_id TEXT PRIMARY KEY,
            domain TEXT,
            score INTEGER
        )
    ''')

    # Sample data (update/add real controls as needed)
    sample_controls = [
        ('A.5.1', 'Information Security Policies', 85),
        ('A.6.1', 'Organization of Information Security', 90),
        ('A.7.2', 'Employee Awareness', 75),
        ('A.9.2', 'Access Control', 80)
    ]

    for control in sample_controls:
        c.execute('''
            INSERT OR REPLACE INTO controls (control_id, domain, score)
            VALUES (?, ?, ?)
        ''', control)

    conn.commit()
    conn.close()
    print("Controls database created/updated successfully.")

if __name__ == '__main__':
    create_db()
