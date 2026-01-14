import sqlite3
import pybadges
import os
from create_controls_db import db_path
from datetime import datetime

os.makedirs("outputs/badges", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

for control, score in data:
    # Set color thresholds
    if score >= 90:
        color = "green"
    elif score >= 75:
        color = "orange"
    else:
        color = "red"

    # Include timestamp in badge filename
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M")
    badge_file = f"outputs/badges/{control}_{timestamp}.svg"
    badge_svg = pybadges.badge(left_text=control, right_text=f"{score}%", right_color=color)
    with open(badge_file, "w") as f:
        f.write(badge_svg)
    print(f"Badge saved: {badge_file}")

# Optional: create a latest badge without timestamp for README
for control, score in data:
    if score >= 90:
        color = "green"
    elif score >= 75:
        color = "orange"
    else:
        color = "red"
    badge_file = f"outputs/badges/{control}.svg"
    badge_svg = pybadges.badge(left_text=control, right_text=f"{score}%", right_color=color)
    with open(badge_file, "w") as f:
        f.write(badge_svg)
