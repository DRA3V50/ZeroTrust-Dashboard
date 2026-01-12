import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os
from generate_badges import generate_badge  # relative import fix

GRAPH_DIR = "assets/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

DB_PATH = "data/controls.db"

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_graphs(df):
    # Zero Trust Posture graph
    plt.figure(figsize=(6, 4))
    plt.bar(df['domain'], df['score'], color="#003366")
    plt.ylim(0, 100)
    plt.title("Zero Trust Posture", color="white")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gcf().patch.set_facecolor('#222')  # dark background
    plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png", facecolor='#222')
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved")

    # ISO 27001 Coverage graph
    plt.figure(figsize=(6, 4))
    plt.bar(df['control_id'], df['score'], color="#005599")
    plt.ylim(0, 100)
    plt.title("ISO 27001 Coverage", color="white")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gcf().patch.set_facecolor('#222')  # dark background
    plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png", facecolor='#222')
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved")

def generate_badges_from_df(df):
    for _, row in df.iterrows():
        generate_badge(row['control_id'], row['domain'], row['score'])

if __name__ == "__main__":
    df = fetch_controls()
    print(f"[DEBUG] Retrieved {len(df)} records from DB")
    generate_graphs(df)
    generate_badges_from_df(df)
