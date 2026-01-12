import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Paths
DB_PATH = "data/controls.db"
GRAPH_DIR = "assets/graphs"
BADGE_DIR = "assets/badges"

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# ---------- DATABASE ----------

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS controls (
            control_id TEXT PRIMARY KEY,
            domain TEXT,
            score INTEGER
        )
    ''')
    # Sample data
    sample_data = [
        ("A.5.1", "Identity", 85),
        ("A.6.1", "Device", 75),
        ("A.7.2", "Network", 65),
        ("A.9.2", "Data", 90),
    ]
    c.executemany('''
        INSERT OR REPLACE INTO controls (control_id, domain, score)
        VALUES (?, ?, ?)
    ''', sample_data)
    conn.commit()
    conn.close()
    print("[DEBUG] Database created/populated at", DB_PATH)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

# ---------- GRAPH & BADGES ----------

def generate_graphs(df):
    # Zero Trust Posture graph
    plt.figure(figsize=(6, 6))
    plt.bar(df['domain'], df['score'], color='darkblue')
    plt.ylim(0, 100)
    plt.title("Zero Trust Posture", color='white')
    plt.xlabel("Domain", color='white')
    plt.ylabel("Score", color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.gcf().patch.set_facecolor('#2b2b2b')
    plt.xticks(color='white')
    plt.yticks(color='white')
    graph_path = os.path.join(GRAPH_DIR, "zero_trust_posture.png")
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved: {graph_path}")

    # ISO 27001 Coverage graph
    plt.figure(figsize=(6, 6))
    plt.bar(df['control_id'], df['score'], color='darkgreen')
    plt.ylim(0, 100)
    plt.title("ISO 27001 Coverage", color='white')
    plt.xlabel("Control", color='white')
    plt.ylabel("Score", color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.gcf().patch.set_facecolor('#2b2b2b')
    plt.xticks(color='white')
    plt.yticks(color='white')
    iso_graph_path = os.path.join(GRAPH_DIR, "iso_27001_coverage.png")
    plt.tight_layout()
    plt.savefig(iso_graph_path)
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved: {iso_graph_path}")

def generate_badges(df):
    for _, row in df.iterrows():
        control_text = f"{row['control_id']} | {row['domain']}"
        score_text = str(row['score'])
        svg_content = badge(left=control_text, right=score_text, color='blue')
        badge_path = os.path.join(BADGE_DIR, f"{row['control_id'].replace('.', '_')}.svg")
        with open(badge_path, "w") as f:
            f.write(svg_content)
        print(f"[DEBUG] Badge generated: {badge_path}")

# ---------- MAIN ----------

if __name__ == "__main__":
    create_db()
    df = fetch_controls()
    print("[DEBUG] Retrieved", len(df), "records from DB")
    generate_graphs(df)
    generate_badges(df)
