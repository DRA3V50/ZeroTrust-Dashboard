import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from scripts.generate_badges import generate_badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "assets/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_graphs():
    df = fetch_controls()
    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color="darkblue")
    plt.xticks(rotation=45, ha="right")
    plt.title("Zero Trust Posture")
    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png")
    print("[DEBUG] Zero Trust graph saved")

    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color="darkgreen")
    plt.xticks(rotation=45, ha="right")
    plt.title("ISO 27001 Coverage")
    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png")
    print("[DEBUG] ISO 27001 graph saved")

    for _, row in df.iterrows():
        generate_badge(row['control_id'], row['domain'], row['score'])

if __name__ == "__main__":
    generate_graphs()
