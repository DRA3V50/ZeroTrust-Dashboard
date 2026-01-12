import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Paths
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure folders exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Fetch control data from DB
def fetch_controls():
    print("Fetching control data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    return df

# Generate Zero Trust Posture graph
def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    plt.figure(figsize=(10,6))
    plt.bar(df['domain'], df['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    plt.close()
    print("Zero Trust graph saved.")

# Generate ISO 27001 Coverage graph
def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    plt.close()
    print("ISO 27001 graph saved.")

# Generate SVG badge for each control
def generate_control_badge(control_id, domain, score):
    svg = badge(
        left_text=control_id,
        right_text=f"{domain} ({score})",
        color='green'
    )
    badge_file = os.path.join(BADGE_DIR, f"{control_id.replace('.', '_')}.svg")
    with open(badge_file, 'w') as f:
        f.write(svg)
    print(f"Badge saved: {badge_file}")

if __name__ == "__main__":
    controls_data = fetch_controls()

    # Generate graphs
    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)

    # Generate badges
    for _, row in controls_data.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
