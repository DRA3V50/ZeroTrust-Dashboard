import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge as pybadge  # older version supports only left/right/color

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

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    return df

def generate_control_badge(control_id, domain, score):
    # Use left/right which is compatible with older pybadges
    left_text = f"{control_id}: {domain}"
    right_text = str(score)
    svg = pybadge(left=left_text, right=right_text, color='blue')
    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)

def generate_zero_trust_graph(df):
    plt.figure(figsize=(12, 6))
    plt.bar(df['domain'], df['score'], color='#1f2937')  # dark dimmed background bars
    plt.xlabel('Security Domain', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.title('Zero Trust Posture', fontsize=14)
    plt.xticks(rotation=30, ha='right', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    plt.close()

def generate_iso_27001_graph(df):
    plt.figure(figsize=(12, 6))
    plt.bar(df['control_id'], df['score'], color='#4b5563')  # darker bars
    plt.xlabel('ISO 27001 Control', fontsize=12)
    plt.ylabel('Compliance Score', fontsize=12)
    plt.title('ISO 27001 Control Coverage', fontsize=14)
    plt.xticks(rotation=30, ha='right', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    plt.close()

if __name__ == "__main__":
    create_controls_db()
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
