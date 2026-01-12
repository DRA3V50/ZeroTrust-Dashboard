import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from generate_badges import generate_badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "assets/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM controls", conn)
    conn.close()
    return df

def zero_trust_graph(df):
    plt.style.use("dark_background")
    # Width ~295px, convert inches for 150 dpi: width = 295 / 150 ≈ 1.97 in
    plt.figure(figsize=(2.0, 1.5))  # width x height in inches
    plt.bar(df["control_id"], df["score"], color="#3498db")
    plt.ylim(0, 100)
    plt.ylabel("Score (%)", fontsize=8)
    plt.title("Zero Trust Posture", fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png", dpi=150)
    plt.close()
    print("[OK] Zero Trust graph")

def iso_graph(df):
    plt.style.use("dark_background")
    plt.figure(figsize=(2.0, 1.5))
    plt.bar(df["domain"], df["score"], color="#e67e22")
    plt.xticks(rotation=30, ha="right", fontsize=8)
    plt.ylim(0, 100)
    plt.ylabel("Compliance (%)", fontsize=8)
    plt.title("ISO 27001 Coverage", fontsize=10)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png", dpi=150)
    plt.close()
    print("[OK] ISO graph")

if __name__ == "__main__":
    df = fetch()
    zero_trust_graph(df)
    iso_graph(df)

    # Generate badges
    for _, row in df.iterrows():
        generate_badge(row["control_id"], row["domain"], row["score"])
