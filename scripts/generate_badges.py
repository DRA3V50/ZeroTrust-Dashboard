import sqlite3
from pathlib import Path
import pybadges

# Paths
db_path = Path("data/controls.db")
badges_dir = Path("outputs/badges")
badges_dir.mkdir(parents=True, exist_ok=True)

# Connect to DB
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Generate SVG badges
for _, row in df.iterrows():
    badge_svg = pybadges.badge(
        left_text=row['control'],
        right_text=f"{row['score']}%",
        right_color="#4c1" if row['score'] >= 80 else "#dfb317"
    )
    with open(badges_dir / f"{row['control']}.svg", "w") as f:
        f.write(badge_svg)

print("Badges generated successfully.")
