import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Path to the database and graphs folder
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'

# Ensure the graphs directory exists (create it if it doesn't)
os.makedirs(GRAPH_DIR, exist_ok=True)

# Function to create a SQLite database and table if not present
def create_controls_db():
    print("Creating/updating SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS controls (
        control_id TEXT PRIMARY KEY,
        domain TEXT NOT NULL,
        score INTEGER
    )
    ''')

    # Populate the table with sample data if it's empty
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

# Fetch the control data from the database
def fetch_controls():
    print("Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Generate the Zero Trust Posture graph
def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['domain'], df['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()

    # Save the graph to the graphs folder
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    print("Zero Trust graph saved.")

# Generate the ISO 27001 Coverage graph
def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['control_id'], df['score'], color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()

    # Save the graph to the graphs folder
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    print("ISO 27001 graph saved.")

# Main function to execute the script
if __name__ == "__main__":
    create_controls_db()  # Ensure the database is created/updated
    controls_data = fetch_controls()  # Fetch data from the database

    # Generate graphs
    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)
