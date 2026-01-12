import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge as pybadge

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
    fig, ax = plt.subplots(figsize=(14,8))
    bars = ax.bar(df['domain'], df['score'], color='#1f77b4', width=0.6)

    ax.set_xlabel('Security Domain', fontsize=14, color='white')
    ax.set_ylabel('Score', fontsize=14, color='white')
    ax.set_title('Zero Trust Posture', fontsize=16, color='white')
    
    # Rotate labels and wrap text if too long
    ax.set_xticklabels(df['domain'], rotation=35, ha='right', fontsize=11)
    ax.set_yticks(range(0, 101, 10))
    ax.tick_params(axis='y', labelsize=11)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{height}', ha='center', fontsize=10, color='white')

    plt.tight_layout()
    path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved: {path}")

def generate_iso_27001_graph(df):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(14,8))
    bars = ax.bar(df['control_id'], df['score'], color='#ff7f0e', width=0.6)

    ax.set_xlabel('ISO 27001 Control', fontsize=14, color='white')
    ax.set_ylabel('Score', fontsize=14, color='white')
    ax.set_title('ISO 27001 Coverage', fontsize=16, color='white')
    
    # Rotate labels
    ax.set_xticklabels(df['control_id'], rotation=35, ha='right', fontsize=11)
    ax.set_yticks(range(0, 101, 10))
    ax.tick_params(axis='y', labelsize=11)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{height}', ha='center', fontsize=10, color='white')

    plt.tight_layout()
    path = os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved: {path}")

def generate_control_badge(control_id, domain, score):
    text = f"{control_id}: {domain}"
    svg = pybadge(text, str(score))
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
