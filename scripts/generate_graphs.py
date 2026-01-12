import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Ensure the 'assets/graphs' directory exists
os.makedirs("assets/graphs", exist_ok=True)

# Database path
DB_PATH = "data/controls.db"

# Path for saving graphs
GRAPH_PATH_1 = "assets/graphs/zero_trust_posture.png"
GRAPH_PATH_2 = "assets/graphs/iso_27001_coverage.png"

# Function to fetch data from the SQLite database
def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Function to generate the Zero Trust Posture graph
def generate_zero_trust_posture_graph(df):
    plt.figure(figsize=(10, 6))

    # Assuming 'score' is a percentage or similar metric for Zero Trust posture
    score_by_domain = df.groupby('domain')['score'].mean().sort_values(ascending=False)
    
    score_by_domain.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title("Zero Trust Posture by Domain", fontsize=16)
    plt.xlabel("Security Domains", fontsize=12)
    plt.ylabel("Average Score", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph as a PNG file
    plt.savefig(GRAPH_PATH_1)
    plt.close()

# Function to generate the ISO 27001 Coverage graph
def generate_iso_27001_coverage_graph(df):
    plt.figure(figsize=(10, 6))

    # Assuming we have control coverage metrics for ISO 27001 controls
    control_coverage = df.groupby('control_id')['score'].mean().sort_values(ascending=False)

    control_coverage.plot(kind='bar', color='lightcoral', edgecolor='black')

    plt.title("ISO 27001 Control Coverage", fontsize=16)
    plt.xlabel("ISO 27001 Controls", fontsize=12)
    plt.ylabel("Average Score", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph as a PNG file
    plt.savefig(GRAPH_PATH_2)
    plt.close()

# Main function to generate both graphs
def generate_graphs():
    df = fetch_data()  # Get the data from the SQLite database

    # Generate the Zero Trust Posture graph
    generate_zero_trust_posture_graph(df)

    # Generate the ISO 27001 Coverage graph
    generate_iso_27001_coverage_graph(df)

# Run the script to generate graphs
if __name__ == "__main__":
    generate_graphs()
    print("Graphs generated and saved in the 'assets/graphs' folder.")

