import os
import sqlite3
from pybadges import badge

DB_PATH = 'data/controls.db'
BADGE_DIR = 'assets/badges'

os.makedirs(BADGE_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
controls = conn.execute("SELECT control_id, domain, score FROM controls").fetchall()
conn.close()

for control_id, domain, score in controls:
    print(f"Generating badge for {control_id}...")
    svg = badge(
        left_text=f"{control_id}: {domain}",
        right_text=str(score),
        right_color="blue"
    )
    with open(os.path.join(BADGE_DIR, f"{control_id}.svg"), "w") as f:
        f.write(svg)
print("All badges generated.")
