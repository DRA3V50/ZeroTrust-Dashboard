import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import pybadges
import os

os.makedirs("assets/graphs", exist_ok=True)
os.makedirs("assets/badges", exist_ok=True)

DB_PATH = "data/controls.db"

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_control_badge(control_id, domain, score):
    control_text = f"{control_id}: {domain}"
    score_text = str(score)
    # Using pybadges v1.3+: only left/right
    svg_content = pybadges.badge(left=control_id, right=score_text, color="darkblue")
    badge_path = f"assets/badges/{control_id}.svg"
    with open(badge_path, "w") as f:
        f.write(svg_content)
    print(f"[DEBUG] Badge generated: {badge_path}")

def generate_badges(df):
    for _, row in df.iterrows():
        generate_control_badge(row['control_id'], row['domain'], row['score'])

def generate_graphs(df):
    plt.figure(figsize=(8, 6))
    plt.bar(df['domain'], df['score'], color='steelblue')
    plt.title("Zero Trust Posture", fontsize=14, color="white")
    plt.ylabel("Score", fontsize=12, color="white")
    plt.xlabel("Domain", fontsize=12, color="white")
    plt.ylim(0, 100)
    plt.gcf().set_facecolor("#2E2E2E")  # dark background
    plt.savefig("assets/graphs/zero_trust_posture.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("[DEBUG] Zero Trust graph saved: assets/graphs/zero_trust_posture.png")

    plt.figure(figsize=(8, 6))
    plt.bar(df['control_id'], df['score'], color='darkorange')
    plt.title("ISO 27001 Coverage", fontsize=14, color="white")
    plt.ylabel("Score", fontsize=12, color="white")
    plt.xlabel("Control", fontsize=12, color="white")
    plt.ylim(0, 100)
    plt.gcf().set_facecolor("#2E2E2E")
    plt.savefig("assets/graphs/iso_27001_coverage.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("[DEBUG] ISO 27001 graph saved: assets/graphs/iso_27001_coverage.png")

if __name__ == "__main__":
    df = fetch_controls()
    generate_graphs(df)
    generate_badges(df)
