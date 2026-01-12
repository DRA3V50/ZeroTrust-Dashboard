import pandas as pd
import matplotlib.pyplot as plt
from scripts.generate_badges import generate_badge
import sqlite3
import os

DB_PATH = "data/controls.db"

def fetch_controls():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_graphs(df):
    os.makedirs("assets/graphs", exist_ok=True)

    # Zero Trust Posture
    plt.figure(figsize=(6, 4))
    plt.bar(df['control_id'], df['score'], color="#2563eb")
    plt.title("Zero Trust Posture", color="white")
    plt.xlabel("Control", color="white")
    plt.ylabel("Score", color="white")
    plt.xticks(rotation=45, ha='right')
    plt.gca().set_facecolor("#1f2937")  # dark background
    plt.savefig("assets/graphs/zero_trust_posture.png", bbox_inches='tight', facecolor="#1f2937")
    plt.close()
    print("[DEBUG] Zero Trust graph saved")

    # ISO 27001 Coverage
    plt.figure(figsize=(6, 4))
    plt.bar(df['control_id'], df['score'], color="#2563eb")
    plt.title("ISO 27001 Coverage", color="white")
    plt.xlabel("Control", color="white")
    plt.ylabel("Score", color="white")
    plt.xticks(rotation=45, ha='right')
    plt.gca().set_facecolor("#1f2937")
    plt.savefig("assets/graphs/iso_27001_coverage.png", bbox_inches='tight', facecolor="#1f2937")
    plt.close()
    print("[DEBUG] ISO 27001 graph saved")

def generate_badges_from_df(df):
    os.makedirs("assets/badges", exist_ok=True)
    for _, row in df.iterrows():
        generate_badge(row['control_id'], row['domain'], row['score'])

if __name__ == "__main__":
    df = fetch_controls()
    generate_graphs(df)
    generate_badges_from_df(df)
