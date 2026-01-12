import os
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # <-- important for GitHub Actions
import matplotlib.pyplot as plt
from pybadges import badge

DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    # Use all unique domains in database
    if 'domain' not in df.columns:
        print("Error: 'domain' column missing in DB")
        return
    domains = df['domain'].unique()
    scores = [df[df['domain'] == d]['score'].mean() for d in domains]

    plt.figure(figsize=(10,6))
    plt.bar(domains, scores, color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    graph_path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(graph_path)
    plt.close()
    print(f"Zero Trust graph saved: {graph_path}")

def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    if 'control_id' not in df.columns:
        print("Error: 'control_id' column missing in DB")
        return
    controls = df['control_id']
    scores = df['score']

    plt.figure(figsize=(10,6))
    plt.bar(controls, scores, color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()
    graph_path = os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')
    plt.savefig(graph_path)
    plt.close()
    print(f"ISO 27001 graph saved: {graph_path}")

def generate_control_badges(df):
    for _, row in df.iterrows():
        svg = badge(
            label=f"{row['control_id']}: {row['domain']}",
            value=row['score'],
            color='blue'
        )
        badge_path = os.path.join(BADGE_DIR, f"{row['control_id']}.svg")
        with open(badge_path, "w") as f:
            f.write(svg)
        print(f"Badge saved: {badge_path}")

if __name__ == "__main__":
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    generate_control_badges(df)
