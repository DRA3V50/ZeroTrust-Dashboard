import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os

# Define the path to save the graphs
GRAPH_PATH = 'assets/graphs/'

# Ensure the 'graphs' directory exists
if not os.path.exists(GRAPH_PATH):
    os.makedirs(GRAPH_PATH)

def generate_zero_trust_posture_graph(data):
    """
    Generates a bar graph of Zero Trust posture across domains and saves it to a file.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data['domain'], data['score'], color='blue')
    plt.title("Zero Trust Posture Evaluation")
    plt.xlabel("Domains")
    plt.ylabel("Scores")
    plt.xticks(rotation=45)
    
    # Save the graph
    graph_filename = 'zero_trust_posture.png'
    plt.savefig(os.path.join(GRAPH_PATH, graph_filename))
    print(f"Graph saved to {os.path.join(GRAPH_PATH, graph_filename)}")
    plt.close()

def generate_iso_27001_coverage_graph(data):
    """
    Generates a bar graph of ISO 27001 compliance coverage across controls and saves it to a file.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data['control'], data['coverage'], color='green')
    plt.title("ISO 27001 Control Coverage")
    plt.xlabel("Controls")
    plt.ylabel("Compliance Coverage (%)")
    plt.xticks(rotation=45)

    # Save the graph
    graph_filename = 'iso_27001_coverage.png'
    plt.savefig(os.path.join(GRAPH_PATH, graph_filename))
    print(f"Graph saved to {os.path.join(GRAPH_PATH, graph_filename)}")
    plt.close()

def fetch_zero_trust_posture_data():
    """
    Fetches Zero Trust posture data from the SQLite database.
    """
    conn = sqlite3.connect('data/controls.db')
    query = "SELECT domain, score FROM zero_trust_posture"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def fetch_iso_27001_coverage_data():
    """
    Fetches ISO 27001 control coverage data from the SQLite database.
    """
    conn = sqlite3.connect('data/controls.db')
    query = "SELECT control, coverage FROM iso_27001_controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Fetch data and generate the graphs
zero_trust_data = fetch_zero_trust_posture_data()
generate_zero_trust_posture_graph(zero_trust_data)

iso_27001_data = fetch_iso_27001_coverage_data()
generate_iso_27001_coverage_graph(iso_27001_data)

