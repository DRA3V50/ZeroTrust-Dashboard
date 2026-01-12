import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import pybadges

# Paths
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Create/update database
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

# Fetch data
def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    return df

# Generate badges (compatible with all pybadges versions)
def generate_control_badge(control_id, domain, score):
    text = f"{control_id}: {domain} = {score}"
    svg = pybadges.badge(label=text, value="")  # use label only
    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)

# Graphs with dark background and readable labels
def generate_zero_trust_graph(df):
    plt.figure(figsize=(10,6))
    plt.bar(df['domain'], df['score'], color='#1f77b4')
    plt.xlabel('Security Domain', color='white')
    plt.ylabel('Score', color='white')
    plt.title('Zero Trust Posture', color='white')
    plt.xticks(rotation=20, ha='right', color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.gcf().patch.set_facecolor('#2b2b2b')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    plt.close()

def generate_iso_27001_graph(df):
    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color='#ff7f0e')
    plt.xlabel('ISO 27001 Control', color='white')
    plt.ylabel('Compliance Score', color='white')
    plt.title('ISO 27001 Control Coverage', color='white')
    plt.xticks(rotation=20, ha='right', color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.gcf().patch.set_facecolor('#2b2b2b')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    plt.close()

# Main
if __name__ == "__main__":
    create_controls_db()
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
