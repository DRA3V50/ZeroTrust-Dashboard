import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge as pybadge  # safe import for badges

# Paths
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

def create_controls_db():
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
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    print(f"[DEBUG] Retrieved {len(df)} records.")
    return df

def generate_zero_trust_graph(df):
    plt.style.use('dark_background')
    plt.figure(figsize=(10,6))
    plt.bar(df['domain'], df['score'], color='#1f77b4')
    plt.xlabel('Security Domain', fontsize=12, color='white')
    plt.ylabel('Score', fontsize=12, color='white')
    plt.title('Zero Trust Posture', fontsize=14, color='white')
    plt.xticks(rotation=30, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved: {path}")

def generate_iso_27001_graph(df):
    plt.style.use('dark_background')
    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color='#ff7f0e')
    plt.xlabel('ISO 27001 Control', fontsize=12, color='white')
    plt.ylabel('Score', fontsize=12, color='white')
    plt.title('ISO 27001 Coverage', fontsize=14, color='white')
    plt.xticks(rotation=30, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    path = os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved: {path}")

def generate_control_badge(control_id, domain, score):
    text = f"{control_id}: {domain} = {score}"
    # pybadges only supports left/right, no 'label' or 'color' argument in your version
    svg = pybadge(left=text, right=str(score))
    path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge generated: {path}")

if __name__ == "__main__":
    create_controls_db()
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
