import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "data/controls.db"
GRAPH_DIR = "assets/graphs"

ZT_GRAPH = os.path.join(GRAPH_DIR, "zero_trust_posture.png")
ISO_GRAPH = os.path.join(GRAPH_DIR, "iso_27001_coverage.png")

# Ensure graphs directory exists
os.makedirs(GRAPH_DIR, exist_ok=True)


def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT control_id, domain, score FROM controls",
        conn
    )
    conn.close()
    return df


def generate_zero_trust_graph(df):
    zt = df.groupby("domain")["score"].mean().reset_index()

    plt.figure(figsize=(8, 5))
    plt.bar(zt["domain"], zt["score"])
    plt.title("Zero Trust Posture by Domain")
    plt.ylabel("Average Control Score")
    plt.xlabel("Domain")
    plt.tight_layout()
    plt.savefig(ZT_GRAPH)
    plt.close()


def generate_iso_27001_graph(df):
    iso = df[df["control_id"].str.startswith("A.")]

    plt.figure(figsize=(8, 5))
    plt.bar(iso["control_id"], iso["score"])
    plt.title("ISO 27001 Control Coverage")
    plt.ylabel("Control Score")
    plt.xlabel("Control")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(ISO_GRAPH)
    plt.close()


if __name__ == "__main__":
    data = fetch_controls()
    generate_zero_trust_graph(data)
    generate_iso_27001_graph(data)

    print("Graphs generated successfully.")

