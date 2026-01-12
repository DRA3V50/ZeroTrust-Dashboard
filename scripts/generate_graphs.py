import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from generate_badges import generate_badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM controls", conn)
    conn.close()
    return df

def zero_trust_graph(df):
    # smaller figure, dark background, dimmer grid
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 4))  # smaller figure
    ax.set_facecolor("#111111")  # even darker background
    ax.bar(df["control_id"], df["score"], color="#3498db")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score (%)", color="#cccccc")
    ax.set_title("Zero Trust Posture", color="#ffffff")
    ax.grid(True, color="#333333", linestyle="--", linewidth=0.5)  # dimmer grid

    plt.tight_layout()
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png", dpi=150)
    plt.close()
    print("[OK] Zero Trust graph")

def iso_graph(df):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 4))  # smaller figure
    ax.set_facecolor("#111111")  # darker background
    ax.bar(df["domain"], df["score"], color="#e67e22")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Compliance (%)", color="#cccccc")
    ax.set_title("ISO 27001 Coverage", color="#ffffff")
    ax.set_xticklabels(df["domain"], rotation=30, ha="right", color="#cccccc")
    ax.grid(True, color="#333333", linestyle="--", linewidth=0.5)

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
