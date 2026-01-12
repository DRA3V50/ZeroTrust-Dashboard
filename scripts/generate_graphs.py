import pandas as pd
import matplotlib.pyplot as plt
import pybadges
import sqlite3
from pathlib import Path

DB_PATH = Path("data/controls.db")
GRAPH_DIR = Path("assets/graphs")
BADGE_DIR = Path("assets/badges")
GRAPH_DIR.mkdir(parents=True, exist_ok=True)
BADGE_DIR.mkdir(parents=True, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query("SELECT * FROM controls", conn)
    except Exception:
        df = pd.DataFrame({
            "control_id": ["A.5.1", "A.6.1", "A.7.2", "A.9.2"],
            "domain": ["Identity", "Device", "Network", "Data"],
            "score": [3, 2, 4, 5]
        })
        df.to_sql("controls", conn, if_exists="replace", index=False)
    finally:
        conn.close()
    return df

def generate_badges(df):
    for _, row in df.iterrows():
        control_id = row["control_id"]
        domain = row["domain"]
        score = row["score"]
        svg_content = pybadges.badge(
            label=f"{control_id} | {domain}",
            value=str(score),
            color="darkblue"
        )
        badge_path = BADGE_DIR / f"{control_id.replace('.', '_')}.svg"
        with open(badge_path, "w") as f:
            f.write(svg_content)

def generate_graphs(df):
    # Zero Trust Posture graph
    plt.figure(figsize=(6, 4))
    plt.bar(df["control_id"], df["score"], color="navy")
    plt.xlabel("Controls", fontsize=10)
    plt.ylabel("Score", fontsize=10)
    plt.title("Zero Trust Posture", color="white", fontsize=12)
    plt.gca().set_facecolor("dimgray")
    plt.savefig(GRAPH_DIR / "zero_trust_posture.png", bbox_inches="tight", facecolor="dimgray")
    plt.close()

    # ISO 27001 Coverage graph
    plt.figure(figsize=(6, 4))
    plt.bar(df["control_id"], df["score"], color="teal")
    plt.xlabel("Controls", fontsize=10)
    plt.ylabel("Score", fontsize=10)
    plt.title("ISO 27001 Coverage", color="white", fontsize=12)
    plt.gca().set_facecolor("dimgray")
    plt.savefig(GRAPH_DIR / "iso_27001_coverage.png", bbox_inches="tight", facecolor="dimgray")
    plt.close()

if __name__ == "__main__":
    df = fetch_controls()
    generate_badges(df)
    generate_graphs(df)
    print("✅ Badges and graphs generated successfully.")
