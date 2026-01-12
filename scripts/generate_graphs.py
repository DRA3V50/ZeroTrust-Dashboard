import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from generate_badges import generate_badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"
BADGE_DIR = "outputs/badges"
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

def fetch():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM controls", conn)
    conn.close()
    return df

def zero_trust_graph(df):
    plt.style.use("dark_background")
    # Convert 330px width to inches: 330px / 150 dpi ~ 2.2 inches (height scaled proportionally)
    plt.figure(figsize=(2.2, 1.5))  
    plt.bar(df["control_id"], df["score"], color="#3498db")
    plt.ylim(0, 100)
    plt.ylabel("Score (%)", fontsize=8)
    plt.title("Zero Trust Posture", fontsize=10)
    plt.tight_layout()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture_{timestamp}.png", dpi=150)
    plt.close()
    print("[OK] Zero Trust graph generated")

def iso_graph(df):
    plt.style.use("dark_background")
    plt.figure(figsize=(2.2, 1.5))  # same width ~330px
    plt.bar(df["domain"], df["score"], color="#e67e22")
    plt.xticks(rotation=30, ha="right", fontsize=8)
    plt.ylim(0, 100)
    plt.ylabel("Compliance (%)", fontsize=8)
    plt.title("ISO 27001 Coverage", fontsize=10)
    plt.tight_layout()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage_{timestamp}.png", dpi=150)
    plt.close()
    print("[OK] ISO 27001 graph generated")

if __name__ == "__main__":
    df = fetch()
    zero_trust_graph(df)
    iso_graph(df)

    for _, row in df.iterrows():
        generate_badge(row["control_id"], row["domain"], row["score"])
