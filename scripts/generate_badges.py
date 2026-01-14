import pybadges
import pandas as pd
import shutil
from datetime import datetime
import os

# Database path
db_path = "data/controls.db"

# Read data
import sqlite3
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Timestamp
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M")

# Make badges folder if not exists
os.makedirs("outputs/badges", exist_ok=True)

# Generate badges
for _, row in df.iterrows():
    control = row["control"]
    score = row["score"]
    color = "green" if score >= 80 else "orange" if score >= 50 else "red"
    
    badge_svg = pybadges.badge(left=control, right=f"{score}%", right_color=color)
    badge_filename = f"outputs/badges/{control}_{timestamp}.svg"
    with open(badge_filename, "w") as f:
        f.write(badge_svg)
    
    # Copy to latest static file for README
    latest_file = f"outputs/badges/{control}.svg"
    shutil.copyfile(badge_filename, latest_file)
