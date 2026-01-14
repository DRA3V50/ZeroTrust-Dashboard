import sqlite3
import pybadges
import os

# Connect to database
conn = sqlite3.connect("data/controls.db")
cursor = conn.cursor()

# Make sure output folder exists
os.makedirs("outputs/badges", exist_ok=True)

cursor.execute("SELECT control, score FROM controls")
rows = cursor.fetchall()

for control, score in rows:
    # Determine badge color based on score
    if score >= 90:
        color = "green"
    elif score >= 75:
        color = "yellow"
    else:
        color = "red"

    # Use correct pybadges API
    badge_svg = pybadges.badge(
        left_text=control,       # left side of badge
        right_text=f"{score}%",  # right side of badge
        right_color=color
    )

    badge_file = f"outputs/badges/{control}.svg"
    with open(badge_file, "w") as f:
        f.write(badge_svg)

conn.close()
print("Badges generated successfully.")
