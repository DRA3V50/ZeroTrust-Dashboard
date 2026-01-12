import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Path to the database and graphs folder
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'

# Ensure the graphs directory exists
os.makedirs(GRAPH_DIR, exist_ok=True)

# Function to fetch control data from SQLite DB
def fetch_controls():
    print("Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Generate Zero Trust Posture graph
def generate_zero_trust_graph(df):
    print("Generating Zero Trust Posture graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['domain'], df['score'], color='skyblue')
    plt.xlabel('Security Domain')
    plt.ylabel('Score')
    plt.title('Zero Trust Posture')
    plt.tight_layout()

    # Save the graph to the graphs folder
    plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
    print("Zero Trust graph saved.")

# Generate ISO 27001 Coverage graph
def generate_iso_27001_graph(df):
    print("Generating ISO 27001 Coverage graph...")
    plt.figure(figsize=(10, 6))
    plt.bar(df['control_id'], df['score'], color='orange')
    plt.xlabel('ISO 27001 Control')
    plt.ylabel('Compliance Score')
    plt.title('ISO 27001 Control Coverage')
    plt.tight_layout()

    # Save the graph to the graphs folder
    plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
    print("ISO 27001 graph saved.")

# Main function to generate graphs
def generate_graphs():
    controls_data = fetch_controls()  # Fetch data from the database
    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)

if __name__ == "__main__":
    generate_graphs()
