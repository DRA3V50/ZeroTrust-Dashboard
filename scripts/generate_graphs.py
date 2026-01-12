import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pybadges import badge

# Path to the database and folders
DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
BADGE_DIR = 'assets/badges'

# Ensure the directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Function to fetch control data from SQLite DB
def fetch_controls():
    print("Fetching data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Generate the Zero Trust Posture graph
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

# Generate the ISO 27001 Coverage graph
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

# Function to generate a badge for a control
def generate_control_badge(control_id, domain, score):
    print(f"Generating badge for {control_id}...")

    # Use 'label' and 'value' for the badge, which pybadges expects
    badge_file = os.path.join(BADGE_DIR, f'{control_id}.svg')

    # Correct usage of pybadges: label and value
    svg = badge(
        label=domain,        # Domain as the label
        value=f"{score}%",    # Score as the value
        color="blue"          # Customize the badge color
    )

    # Save badge as SVG
    with open(badge_file, 'w') as f:
        f.write(svg)
    print(f"Badge saved: {badge_file}")

# Main function to generate graphs and badges
def generate_graphs_and_badges():
    controls_data = fetch_controls()  # Fetch data from the database

    # Generate graphs
    generate_zero_trust_graph(controls_data)
    generate_iso_27001_graph(controls_data)

    # Generate badges for each control
    for control in controls_data.itertuples():
        generate_control_badge(control.control_id, control.domain, control.score)

if __name__ == "__main__":
    generate_graphs_and_badges()

