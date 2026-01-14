import sqlite3
import os
from pybadges import badge

DB_PATH = "data/controls.db"
BADGE_DIR = "outputs/badges"
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

os.makedirs(BADGE_DIR, exist_ok=True)

# Read data from SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, score FROM controls")
rows = cursor.fetchall()
conn.close()

control_scores = {row[0]: row[1] for row in rows}

for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    # Use pybadges >= 2.0 argument syntax
    color = "green" if score >= 80 else "orange" if score >= 60 else "red"
    badge_svg = badge(left_text=control, right_text=str(score), right_color=color)
    badge_file = f"{BADGE_DIR}/{control}.svg"
    with open(badge_file, "w") as f:
        f.write(badge_svg)

print("Badges updated successfully!")
