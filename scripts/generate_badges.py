import os
import sqlite3

try:
    import pandas as pd
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

from scripts.create_controls_db import db_path

os.makedirs("outputs/badges", exist_ok=True)

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)

for _, row in df.iterrows():
    badge_file = os.path.join("outputs/badges", f"{row['control']}.svg")
    # Simple SVG badge
    svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
  <rect width="120" height="20" fill="#555"/>
  <rect x="60" width="60" height="20" fill="#4c1"/>
  <text x="30" y="14" fill="#fff" font-family="Verdana" font-size="11">{row['control']}</text>
  <text x="90" y="14" fill="#fff" font-family="Verdana" font-size="11">{row['score']}%</text>
</svg>
"""
    with open(badge_file, "w") as f:
        f.write(svg_content.strip())

conn.close()
print("Badges generated successfully.")
