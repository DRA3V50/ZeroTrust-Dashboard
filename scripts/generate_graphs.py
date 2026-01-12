import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from generate_badges import generate_control_badge

DB_PATH = 'data/controls.db'
GRAPH_PATH = 'assets/graphs/'

os.makedirs(GRAPH_PATH, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def plot_zero_trust(df):
    plt.figure(figsize=(8,6))
    plt.bar(df['domain'], df['score'], color='darkblue')
    plt.title("Zero Trust Posture", color='white')
    plt.ylabel("Score", color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_PATH, "zero_trust_posture.png"), facecolor='#2b2b2b')
    plt.close()
    print(f"[DEBUG] Zero Trust graph saved.")

def plot_iso_27001(df):
    plt.figure(figsize=(8,6))
    plt.bar(df['control_id'], df['score'], color='darkgreen')
    plt.title("ISO 27001 Coverage", color='white')
    plt.ylabel("Score", color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('#2b2b2b')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_PATH, "iso_27001_coverage.png"), facecolor='#2b2b2b')
    plt.close()
    print(f"[DEBUG] ISO 27001 graph saved.")

if __name__ == "__main__":
    df = fetch_controls()
    plot_zero_trust(df)
    plot_iso_27001(df)
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])
