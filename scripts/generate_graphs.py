import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'

os.makedirs(GRAPH_DIR, exist_ok=True)

def fetch_controls():
    print("Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    print(f"Fetched {len(df)} rows from database.")
    return df

def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    # Select rows where domain matches the Zero Trust domains
    zt_domains = ['Identity', 'Device', 'Network', 'Application', 'Data']
    df_domains = df[df['control_id'].isin(zt_domains)]
    if df_domains.empty:
        print("Warning: No Zero Trust domain data found! Graph will use all domain entries.")
        df_domains = df[df['domain'].isin(zt_domains)]

    plt.figure(figsize=(10, 6))
    plt.bar(df_domains['control_id'], df_domains['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    graph_path = os.path.join(GRAPH_DIR, 'zero_trust_posture.png')
    plt.savefig(graph_path)
    plt.close()
    print(f"Zero Trust graph saved: {graph_path}")

def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    iso_controls = ['A.5.1', 'A.6.1', 'A.8.2', 'A.9.2']
    df_controls = df[df['control_id'].isin(iso_controls)]
    if df_controls.empty:
        print("Warning: No ISO 27001 control data found! Graph will use all control entries.")
        df_controls = df[df['control_id'].str.startswith('A.')]

    plt.figure(figsize=(10, 6))
    plt.bar(df_controls['control_id'], df_controls['score'], color='orange')
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
