import os
import sqlite3
import pandas as pd
import pybadges

DB_PATH = 'data/controls.db'
BADGE_DIR = 'assets/badges'

os.makedirs(BADGE_DIR, exist_ok=True)

def fetch_controls():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM controls", conn)
    conn.close()
    return df

def generate_control_badges():
    df = fetch_controls()
    for _, row in df.iterrows():
        control_text = f"{row['control_id']}: {row['domain']}"
        score_text = str(row['score'])

        # POSITONAL ONLY, no keywords
        # This will work on any pybadges version
        svg = pybadges.badge(control_text, score_text)

        badge_path = os.path.join(BADGE_DIR, f"{row['control_id']}.svg")
        with open(badge_path, "w") as f:
            f.write(svg)
        print(f"Badge saved: {badge_path}")

if __name__ == "__main__":
    generate_control_badges()

