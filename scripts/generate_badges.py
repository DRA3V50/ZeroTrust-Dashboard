import sqlite3
import pybadges
import os
import pandas as pd

# Path to DB
db_path = "data/controls.db"

# Path to output badges
output_dir = "outputs/badges"
os.makedirs(output_dir, exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)

# Read all controls
df = pd.read_sql("SELECT * FROM controls", conn)

for _, row in df.iterrows():
    control = row["control"]
    score = row["score"]

    # Determine badge color
    if score >= 90:
        color = "green"
    elif score >= 75:
        color = "yellow"
    else:
        color = "red"

    # Create badge using older pybadges syntax
    badge_svg = pybadges.badge(label=control, value=f"{score}%", color=color)

    # Save badge
    badge_file = os.path.join(output_dir, f"{control}.svg")
    with open(badge_file, "w") as f:
        f.write(badge_svg)

print("Badges generated successfully.")
