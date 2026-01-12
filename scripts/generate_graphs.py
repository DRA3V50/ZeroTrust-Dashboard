# scripts/generate_graphs.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
DB_PATH = Path("data/controls.db")
GRAPH_DIR = Path("assets/graphs")
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    # Example: Adjust to match your table structure
    df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
    conn.close()
    return df

def generate_domain_graph(df):
    domain_scores = df.groupby('domain')['score'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    domain_scores.plot(kind='bar', color='#4c72b0')
    plt.title("Live Zero Trust Posture")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "zero_trust_posture.png")
    plt.close()

def generate_iso_graph(df):
    iso_scores = df.groupby('control_id')['score'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    iso_scores.plot(kind='bar', color='#dd8452')
    plt.title("ISO 27001 Control Coverage")
    plt.ylabel("Score (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "iso_27001_coverage.png")
    plt.close()

if __name__ == "__main__":
    data = fetch_data()
    generate_domain_graph(data)
    generate_iso_graph(data)
    print("Graphs generated successfully.")
