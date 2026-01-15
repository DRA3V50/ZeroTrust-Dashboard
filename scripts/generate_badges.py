#!/usr/bin/env python3
import os
import sqlite3
from pybadges import badge

# Ensure badges folder exists
BADGE_DIR = "outputs/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

# Database path
DB_PATH = "data/controls.db"

# Define controls
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]
ZERO_TRUST_DOMAINS = ["Application", "Data", "Device", "Identity", "Network"]
ALL_CONTROLS = ISO_CONTROLS + ZERO_TRUST_DOMAINS

# Connect to DB and fetch scores
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, score FROM controls")
rows = cursor.fetchall()
conn.close()

# Convert to dictionary for quick lookup
control_scores = {row[0]: row[1] for row in rows}

print("Fetched scores from database:")
for control in ALL_CONTROLS:
    score = control_scores.get(control)
    if score is None:
        print(f"⚠️ Warning: No score found for {control}, defaulting to 0")
        score = 0
        control_scores[control] = 0
    else:
        print(f"{control}: {score}%")

# Generate badge for every control
for control in ALL_CONTROLS:
    score = control_scores[control]
    
    # Assign color based on type
    if control in ISO_CONTROLS:
        if score >= 80:
            color = "blue"
        elif score >= 60:
            color = "orange"
        else:
            color = "red"
    else:  # Zero Trust domains
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

print("All badges generated and updated successfully with ISO blue and Zero Trust green.")

