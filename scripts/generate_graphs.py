# Keep imports
import os
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'

os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_zero_trust_graph(df):
    domains = df['domain'].unique()
    scores = [df[df['domain'] == d]['score'].mean() for d in domains]
    plt.figure(figsize=(10,6))
    plt.bar(domains, scores, color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    graph_path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(graph_path)
    plt.close()
    print(f"Zero Trust graph saved: {graph_path}")

def generate_iso_27001_graph(df):
    controls = df['control_id']
    scores = df['score']
    plt.figure(figsize=(10,6))
    plt.bar(controls, scores, color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()
    graph_path = os.path.join(GRAPH_DIR, 'iso_27001_coverage.png')
    plt.savefig(graph_path)
    plt.close()
    print(f"ISO 27001 graph saved: {graph_path}")

if __name__ == "__main__":
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)

