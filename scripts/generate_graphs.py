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
    return df

def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    domains = ['Identity', 'Device', 'Network', 'Application', 'Data']
    df_domains = df[df['control_id'].isin(domains)]
    plt.figure(figsize=(10, 6))
    plt.bar(df_domains['control_id'], df_domains['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    print("Zero Trust graph saved.")

def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    controls = ['A.5.1', 'A.6.1', 'A.8.2', 'A.9.2']
    df_controls = df[df['control_id'].isin(controls)]
    plt.figure(figsize=(10, 6))
    plt.bar(df_controls['control_id'], df_controls['score'], color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    print("ISO 27001 graph saved.")

if __name__ == "__main__":
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_27001_graph(df)
