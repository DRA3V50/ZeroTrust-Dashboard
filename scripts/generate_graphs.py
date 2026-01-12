import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data():
    conn = sqlite3.connect('data/controls.db')
    df = pd.read_sql_query("SELECT control_id, score FROM controls", conn)
    conn.close()
    return df

def generate_graphs():
    df = fetch_data()
    plt.figure(figsize=(8,4))
    plt.bar(df['control_id'], df['score'], color='darkblue')
    plt.ylim(0, 100)
    plt.xlabel('Control ID')
    plt.ylabel('Score (%)')
    plt.title('ISO 27001 Control Scores')
    plt.tight_layout()
    plt.savefig('assets/badges/controls_graph.png')
    plt.close()
    print("Graphs generated successfully.")

if __name__ == '__main__':
    generate_graphs()
