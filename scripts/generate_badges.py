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
        control_text = row['control_id']
        score_text = str(row['score'])
        print(f"Generating badge for {control_text}...")
        svg = pybadges.badge(
            left_text=control_text,
            right_text=score_text,
            right_color="blue"
        )
        path = os.path.join(BADGE_DIR, f"{control_text}.svg")
        with open(path, "w") as f:
            f.write(svg)
        print(f"Badge saved for {control_text}")

if __name__ == "__main__":
    generate_control_badges()
