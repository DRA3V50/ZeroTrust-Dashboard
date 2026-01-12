import os
import sqlite3
import pandas as pd
from pybadges import badge

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
        try:
            # Newer pybadges syntax
            svg = badge(
                label=f"{row['control_id']}: {row['domain']}",
                value=row['score'],
                color='blue'
            )
        except TypeError:
            # Older pybadges fallback
            svg = badge(
                left=f"{row['control_id']}: {row['domain']}",
                right=str(row['score']),
                color='blue'
            )

        badge_path = os.path.join(BADGE_DIR, f"{row['control_id']}.svg")
        with open(badge_path, "w") as f:
            f.write(svg)
        print(f"Badge saved: {badge_path}")

if __name__ == "__main__":
    generate_control_badges()
