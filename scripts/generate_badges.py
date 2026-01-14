import pandas as pd
import pybadges
import os
import sqlite3
from create_controls_db import db_path

os.makedirs("outputs/badges", exist_ok=True)

df = pd.read_sql("SELECT * FROM controls", sqlite3.connect(db_path))

for _, row in df.iterrows():
    control = row['control']
    score = row['score']
    # Set badge color
    if score >= 90:
        color = "green"
    elif score >= 75:
        color = "yellow"
    else:
        color = "red"

    badge_svg = pybadges.badge(left_text=control, right_text=f"{score}%", right_color=color)
    with open(f"outputs/badges/{control}.svg", "w") as f:
        f.write(badge_svg)
