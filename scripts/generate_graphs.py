import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = 'data/controls.db'
GRAPH_PATH = 'assets/graphs/control_scores.png'

def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT control_id, score FROM controls", conn)
    conn.close()
    return df

def generate_bar_graph(df):
    plt.figure(figsize=(10,6))
    plt.bar(df['control_id'], df['score'], color='steelblue')
    plt.xlabel("Control ID")
    plt.ylabel("Score")
    plt.title("Zero Trust & ISO 27001 Control Scores")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(GRAPH_PATH)
    plt.close()
    print(f"Graph generated at {GRAPH_PATH}")

if __name__ == "__main__":
    df = fetch_data()
    generate_bar_graph(df)
