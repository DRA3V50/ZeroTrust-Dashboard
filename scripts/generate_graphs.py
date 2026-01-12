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
    plt.figure(figsize=(8, 5))

    plt.bar(df["control_id"], df["score"], color="#3498db")
    plt.ylim(0, 100)
    plt.ylabel("Score (%)")
    plt.title("Zero Trust Posture")

    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png", dpi=150)
    plt.close()
    print("[OK] Zero Trust graph")

def iso_graph(df):
    plt.style.use("dark_background")
    plt.figure(figsize=(8, 5))

    plt.bar(df["domain"], df["score"], color="#e67e22")
    plt.xticks(rotation=30, ha="right")
    plt.ylim(0, 100)
    plt.ylabel("Compliance (%)")
    plt.title("ISO 27001 Coverage")

    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png", dpi=150)
    plt.close()
    print("[OK] ISO graph")

if __name__ == "__main__":
    df = fetch()
    zero_trust_graph(df)
    iso_graph(df)

    for _, row in df.iterrows():
        generate_badge(row["control_id"], row["domain"], row["score"])
