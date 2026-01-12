# scripts/generate_graphs.py

import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Paths
# -----------------------------
DB_PATH = 'data/controls.db'
GRAPH_FOLDER = 'assets/graphs'
ZERO_TRUST_GRAPH = os.path.join(GRAPH_FOLDER, 'zero_trust_posture.png')
ISO_GRAPH = os.path.join(GRAPH_FOLDER, 'iso_27001_coverage.png')

# -----------------------------
# Ensure folder exists
# -----------------------------
os.makedirs(GRAPH_FOLDER, exist_ok=True)

# -----------------------------
# Fetch data from SQLite
# -----------------------------
def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# -----------------------------
# Generate Zero Trust Posture Graph
# -----------------------------
def generate_zero_trust_graph(df):
    domain_scores = df.groupby('domain')['score'].mean().reindex(
        ['Identity', 'Device', 'Network', 'Application', 'Data']
    )
    
    plt.figure(figsize=(8,6))
    domain_scores.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.ylim(0, 100)
    plt.title('Zero Trust Posture')
    plt.ylabel('Average Score (%)')
    plt.xlabel('Domain')
    plt.tight_layout()
    plt.savefig(ZERO_TRUST_GRAPH)
    plt.close()
    print(f"[✔] Zero Trust graph saved: {ZERO_TRUST_GRAPH}")

# -----------------------------
# Generate ISO 27001 Coverage Graph
# -----------------------------
def generate_iso_graph(df):
    iso_controls = ['A.5.1', 'A.6.1', 'A.7.2', 'A.9.2']
    control_scores = df[df['control_id'].isin(iso_controls)].set_index('control_id')['score']
    control_scores = control_scores.reindex(iso_controls)  # Ensure order
    
    plt.figure(figsize=(8,6))
    control_scores.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.ylim(0, 100)
    plt.title('ISO 27001 Control Coverage')
    plt.ylabel('Score (%)')
    plt.xlabel('Control')
    plt.tight_layout()
    plt.savefig(ISO_GRAPH)
    plt.close()
    print(f"[✔] ISO 27001 graph saved: {ISO_GRAPH}")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == '__main__':
    try:
        df = fetch_data()
        if df.empty:
            print("[⚠] No data found in controls database. Generate controls first!")
        else:
            generate_zero_trust_graph(df)
            generate_iso_graph(df)
            print("[✔] All graphs generated successfully!")
    except Exception as e:
        print(f"[❌] Error generating graphs: {e}")
