import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Path to the database and the badges/graphs directories
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Create or update the controls database
def create_controls_db():
    print("[DEBUG] Creating/updating SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS controls (
        control_id TEXT PRIMARY KEY,
        domain TEXT NOT NULL,
        score INTEGER
    )
    ''')

    cursor.execute('SELECT COUNT(*) FROM controls')
    if cursor.fetchone()[0] == 0:
        print("[DEBUG] Populating the database with sample data...")
        sample_data = [
            ('A.5.1', 'Information Security Policies', 80),
            ('A.6.1', 'Organization of Information Security', 75),
            ('A.8.2', 'Risk Management', 90),
            ('A.9.2', 'Access Control', 85)
        ]
        cursor.executemany('INSERT INTO controls VALUES (?, ?, ?)', sample_data)

    conn.commit()
    conn.close()
    print("[DEBUG] Database ready.")

# Fetch control data from the database
def fetch_controls():
    print("[DEBUG] Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(f"[DEBUG] Retrieved {len(df)} records.")
    return df

# Generate badge for a control using positional args (no keywords)
def generate_control_badge(control_id, domain, score):
    print(f"[DEBUG] Generating badge for {control_id}...")
    left_text = f"{control_id}: {domain}"
    right_text = str(score)
    # Use positional arguments only to avoid TypeError
    svg = badge(left_text, right_text, 'blue')

    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge saved: {badge_path}")

# Generate Zero Trust Posture graph
def generate_zero_trust_graph(df):
    print("[DEBUG] Generating Zero Trust Posture graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['domain'], df['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved: {os.path.join(GRAPH_DIR, 'zero_trust_posture.png')}")

# Generate ISO 27001 Coverage graph
def generate_iso_27001_graph(df):
    print("[DEBUG] Generating ISO 27001 Coverage graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['control_id'], df['score'], color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved: {os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')}")

# Main execution
if __name__ == "__main__":
    create_controls_db()
    controls_data = fetch_controls()

    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)

    for _, row in controls_data.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
