import sqlite3, pandas as pd, matplotlib.pyplot as plt, os
from datetime import datetime
from generate_badges import generate_badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM controls", conn)
    conn.close()
    return df

def zero_trust_graph(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    fig, ax = plt.subplots(figsize=(10,6))
    colors = ['#3498db' for _ in df['score']]
    ax.bar(df["control_id"], df["score"], color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score (%)")
    ax.set_title("Zero Trust Posture")
    plt.tight_layout()
    filename = f"{GRAPH_DIR}/zero_trust_posture_{timestamp}.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"[OK] Zero Trust graph saved: {filename}")

def iso_graph(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    fig, ax = plt.subplots(figsize=(10,6))
    colors = ['#e67e22' for _ in df['score']]
    ax.bar(df["domain"], df["score"], color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Compliance (%)")
    ax.set_title("ISO 27001 Coverage")
    ax.set_xticks(range(len(df["domain"])))
    ax.set_xticklabels(df["domain"], rotation=30, ha='right')
    plt.tight_layout()
    filename = f"{GRAPH_DIR}/iso_27001_coverage_{timestamp}.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"[OK] ISO 27001 graph saved: {filename}")

if __name__ == "__main__":
    df = fetch_controls()
    zero_trust_graph(df)
    iso_graph(df)
    for _, row in df.iterrows():
        generate_badge(row["control_id"], row["domain"], row["score"])
