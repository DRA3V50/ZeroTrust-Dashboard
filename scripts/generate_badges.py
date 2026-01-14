import pandas as pd
import sqlite3
from pathlib import Path

# Paths
db_path = Path("data/controls.db")
badges_dir = Path("outputs/badges")
badges_dir.mkdir(parents=True, exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Read controls from database
df = pd.read_sql("SELECT * FROM controls", conn)

# Function to generate SVG badge for a control
def create_badge(control_name, score):
    if score >= 90:
        color = "brightgreen"
    elif score >= 75:
        color = "yellow"
    else:
        color = "red"

    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
      <rect width="150" height="20" fill="#555"/>
      <rect x="80" width="70" height="20" fill="{color}"/>
      <text x="40" y="14" fill="#fff" font-family="Verdana" font-size="11">{control_name}</text>
      <text x="115" y="14" fill="#fff" font-family="Verdana" font-size="11">{score}%</text>
    </svg>"""
    return svg_template

# Generate badges
for _, row in df.iterrows():
    badge_file = badges_dir / f"{row['control']}.svg"
    badge_file.write_text(create_badge(row["control"], row["score"]))

print("Badges generated successfully.")
