import sqlite3
from pathlib import Path
import pybadges
import pandas as pd
from scripts.create_controls_db import db_path

# Ensure database exists
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

badges_dir = Path("outputs/badges")
badges_dir.mkdir(parents=True, exist_ok=True)

# Function to determine badge color
def get_color(score):
    if score >= 90:
        return "green"
    elif score >= 75:
        return "yellow"
    else:
        return "red"

for _, row in df.iterrows():
    control = row['control']
    score = row['score']
    color = get_color(score)

    badge_svg = pybadges.badge(
        left_text=control,
        right_text=f"{score}%",
        right_color=color
    )

    with open(badges_dir / f"{control}.svg", "w") as f:
        f.write(badge_svg)

print("Badges generated successfully.")
