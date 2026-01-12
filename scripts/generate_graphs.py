import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Paths
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

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

def fetch_controls():
    print("[DEBUG] Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(f"[DEBUG] Retrieved {len(df)} records.")
    return df

def generate_control_badge(control_id, domain, score):
    print(f"[DEBUG] Generating badge for {control_id}...")
    # pybadges usage updated for latest API
    svg = badge(left=control_id + ": " + domain, right=str(score), color='blue')

    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge saved: {badge_path}")

def generate_zero_trust_graph(df):
    print("[DEBUG] Generating Zero Trust Posture graph...")
    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df['domain'], df['score'], color='#3b82f6')  # nice blue

    ax.set_xlabel('Security Domain', fontsize=12, color='white')
    ax.set_ylabel('Score', fontsize=12, color='white')
    ax.set_title('Zero Trust Posture', fontsize=16, color='white')

    plt.xticks(rotation=30, ha='right', fontsize=10, color='white')
    plt.yticks(fontsize=10, color='white')

    # Adjust margins so text doesn't overlap
    plt.tight_layout()

    save_path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(save_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"[DEBUG] Zero Trust graph saved: {save_path}")

def generate_iso_27001_graph(df):
    print("[DEBUG] Generating ISO 27001 Coverage graph...")
    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df['control_id'], df['score'], color='#f59e0b')  # amber/orange

    ax.set_xlabel('ISO 27001 Control', fontsize=12, color='white')
    ax.set_ylabel('Compliance Score', fontsize=12, color='white')
    ax.set_title('ISO 27001 Control Coverage', fontsize=16, color='white')

    plt.xticks(fontsize=10, color='white')
    plt.yticks(fontsize=10, color='white')

    plt.tight_layout()

    save_path = os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')
    plt.savefig(save_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"[DEBUG] ISO 27001 graph saved: {save_path}")

if __name__ == "__main__":
    create_controls_db()
    controls_data = fetch_controls()

    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)

    for idx, row in controls_data.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
