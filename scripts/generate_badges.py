#!/usr/bin/env python3
import os
import sqlite3
from pybadges import badge

# Ensure badges folder exists
BADGE_DIR = "outputs/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

# Database path
DB_PATH = "data/controls.db"

# Define all controls: ISO + Zero Trust domains
ALL_CONTROLS = [
    "A.5.1", "A.6.1", "A.8.2", "A.9.2",
    "Application", "Data", "Device", "Identity", "Network"
]

# Connect to DB and fetch scores
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, score FROM controls")
rows = cursor.fetchall()
conn.close()

# Convert to dictionary for quick lookup
control_scores = {row[0]: row[1] for row in rows}

# Generate badge for every control
for control in ALL_CONTROLS:
    score = control_scores.get(control, 0)
    if score >= 80:
        color = "green"
    elif score >= 60:
        color = "orange"
    else:
        color = "red"

    badge_svg = badge(left_text=control, right_text=str(score), right_color=color)
    badge_path = os.path.join(BADGE_DIR, f"{control}.svg")
    with open(badge_path, "w", encoding="utf-8") as f:
        f.write(badge_svg)

print("All badges generated and updated successfully.")
