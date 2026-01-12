import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

def fetch_controls():
    print("Fetching control data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    return df

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

def generate_control_badges(df):
    print("Generating badges...")
    for _, row in df.iterrows():
        svg = badge(
            left_text=row['control_id'],
            right_text=f"{row['score']}%",
            right_color="green" if row['score'] >= 80 else "orange" if row['score'] >= 60 else "red"
        )
        file_path = os.path.join(BADGE_DIR, f"{row['control_id'].replace('.', '_')}.svg")
        with open(file_path, 'w') as f:
            f.write(svg)
        print(f"Badge saved: {file_path}")

if __name__ == "__main__":
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
    generate_control_badges(df)
