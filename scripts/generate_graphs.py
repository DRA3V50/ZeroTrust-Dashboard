# scripts/generate_graphs.py

import pandas as pd
import matplotlib.pyplot as plt
from generate_badges import generate_badge
import sqlite3

def fetch_controls():
    conn = sqlite3.connect("data/controls.db")
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_badges_from_df(df):
    for _, row in df.iterrows():
        generate_badge(row['control_id'], row['domain'], row['score'])

def generate_zero_trust_graph(df):
    plt.style.use("dark_background")
    plt.figure(figsize=(6,6))
    plt.bar(df['control_id'], df['score'], color="#1f77b4")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.ylabel("Score")
    plt.title("Zero Trust Posture")
    plt.tight_layout()
    plt.savefig("assets/graphs/zero_trust_posture.png")
    plt.close()

def generate_iso_graph(df):
    plt.style.use("dark_background")
    plt.figure(figsize=(6,6))
    plt.bar(df['control_id'], df['score'], color="#ff7f0e")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.ylabel("Coverage")
    plt.title("ISO 27001 Coverage")
    plt.tight_layout()
    plt.savefig("assets/graphs/iso_27001_coverage.png")
    plt.close()

if __name__ == "__main__":
    df = fetch_controls()
    generate_badges_from_df(df)
    generate_zero_trust_graph(df)
    generate_iso_graph(df)
    print("[DEBUG] Zero Trust graph saved")
    print("[DEBUG] ISO 27001 graph saved")
