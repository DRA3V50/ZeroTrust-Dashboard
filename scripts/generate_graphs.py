import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Paths
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Create or update database
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
        print("[DEBUG] Populating database with sample data...")
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

# Fetch data
def fetch_controls():
    print("[DEBUG] Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    print(f"[DEBUG] Retrieved {len(df)} records.")
    return df

# Generate badges
def generate_control_badge(control_id, domain, score):
    control_text = f"{control_id}: {domain}"
    score_text = str(score)
    svg = badge(left=control_text, right=score_text, color='darkblue')  # Requires pybadges >=1.3
    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge generated for {control_id}.")

# Generate Zero Trust graph
def generate_zero_trust_graph(df):
    print("[DEBUG] Generating Zero Trust Posture graph...")
    plt.figure(figsize=(10, 6), facecolor='#2b2b2b')
    plt.bar(df['domain'], df['score'], color='dodgerblue')
    plt.xlabel('Security Domain', color='white')
    plt.ylabel('Score', color='white')
    plt.title('Zero Trust Posture', color='white')
    plt.xticks(rotation=20, ha='right', color='white')
    plt.yticks(color='white')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'), facecolor='#2b2b2b')
    plt.close()
    print("[DEBUG] Zero Trust graph saved.")

# Generate ISO 27001 graph
def generate_iso_27001_graph(df):
    print("[DEBUG] Generating ISO 27001 Coverage graph...")
    plt.figure(figsize=(10, 6), facecolor='#2b2b2b')
    plt.bar(df['control_id'], df['score'], color='orange')
    plt.xlabel('ISO 27001 Control', color='white')
    plt.ylabel('Compliance Score', color='white')
    plt.title('ISO 27001 Control Coverage', color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'), facecolor='#2b2b2b')
    plt.close()
    print("[DEBUG] ISO 27001 graph saved.")

# Main
if __name__ == "__main__":
    create_controls_db()
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
