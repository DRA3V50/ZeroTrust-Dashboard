import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scripts.generate_badges import generate_badge

os.makedirs("assets/graphs", exist_ok=True)

DB_PATH = "data/controls.db"

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_graphs(df):
    plt.style.use('dark_background')  # dim background
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(df['control_id'], df['score'], color="#1f77b4")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score %")
    ax.set_title("Zero Trust Posture")
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = "assets/graphs/zero_trust_posture.png"
    plt.savefig(filename)
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved: {filename}")

    # ISO 27001 Coverage Graph
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(df['domain'], df['score'], color="#ff7f0e")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score %")
    ax.set_title("ISO 27001 Coverage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = "assets/graphs/iso_27001_coverage.png"
    plt.savefig(filename)
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved: {filename}")

def generate_badges_from_df(df):
    for _, row in df.iterrows():
        generate_badge(row['control_id'], row['domain'], row['score'])

if __name__ == "__main__":
    df = fetch_controls()
    generate_graphs(df)
    generate_badges_from_df(df)
