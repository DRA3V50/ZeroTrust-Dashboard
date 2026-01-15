#!/usr/bin/env python3
import os
import sqlite3
from pybadges import badge

import matplotlib
matplotlib.use("Agg")  # Ensure headless backend

DB_PATH = "data/controls.db"
BADGE_DIR = "outputs/badges"
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

os.makedirs(BADGE_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, score FROM controls")
rows = cursor.fetchall()
conn.close()

control_scores = {row[0]: row[1] for row in rows}

for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    if score >= 80:
        color = "green"
    elif score >= 60:
        color = "orange"
    else:
        color = "red"

    badge_svg = badge(left_text=control, right_text=str(score), right_color=color)
    with open(f"{BADGE_DIR}/{control}.svg", "w") as f:
        f.write(badge_svg)
