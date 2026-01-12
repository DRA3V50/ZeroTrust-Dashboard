import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "data/controls.db"

def create_and_populate_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS controls (
            control_id TEXT,
            domain TEXT,
            score INTEGER
        )
    """)
    # sample data
    sample_data = [
        ("A.5.1", "Identity", 80),
        ("A.6.1", "Device", 60),
        ("A.7.2", "Network", 70),
        ("A.9.2", "Data", 50)
    ]
    cur.execute("DELETE FROM controls")
    cur.executemany("INSERT INTO controls VALUES (?, ?, ?)", sample_data)
    conn.commit()
    conn.close()

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_zero_trust_graph(df):
    plt.figure(figsize=(10,6))
    ax = df.plot(kind='bar', x='domain', y='score', legend=False, color='#2E3B4E')
    plt.title('Zero Trust Posture', fontsize=16)
    plt.xlabel('Domain', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.ylim(0, 100)
    plt.xticks(rotation=30, fontsize=10)
    plt.yticks(fontsize=10)
    ax.set_facecolor('#1F2833')
    plt.gcf().patch.set_facecolor('#1F2833')
    plt.tight_layout()
    plt.savefig("assets/graphs/zero_trust_posture.png", dpi=150, facecolor='#1F2833')
    plt.close()

def generate_iso_graph(df):
    plt.figure(figsize=(10,6))
    ax = df.plot(kind='bar', x='control_id', y='score', color='#2E3B4E')
    plt.title('ISO 27001 Coverage', fontsize=16)
    plt.xlabel('Control', fontsize=12)
    plt.ylabel('Coverage %', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    ax.set_facecolor('#1F2833')
    plt.gcf().patch.set_facecolor('#1F2833')
    plt.tight_layout()
    plt.savefig("assets/graphs/iso_27001_coverage.png", dpi=150, facecolor='#1F2833')
    plt.close()

if __name__ == "__main__":
    create_and_populate_db()
    df = fetch_controls()
    generate_zero_trust_graph(df)
    generate_iso_graph(df)
    print("[DEBUG] Graphs generated successfully.")
