import sqlite3
import pybadges
import os
from create_controls_db import db_path

os.makedirs("outputs/badges", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

def badge_color(score):
    if score >= 90:
        return "green"
    elif score >= 75:
        return "orange"
    else:
        return "red"

for control, score in data:
    color = badge_color(score)
    badge_svg = pybadges.badge(left_text=control, right_text=f"{score}%", right_color=color)
    badge_file = f"outputs/badges/{control}.svg"
    with open(badge_file, "w") as f:
        f.write(badge_svg)
    print(f"Badge saved to {badge_file}")
