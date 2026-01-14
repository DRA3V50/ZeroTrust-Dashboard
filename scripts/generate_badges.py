import sqlite3
from pathlib import Path

# Ensure pandas is available
try:
    import pandas as pd
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

from create_controls_db import db_path

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

Path("outputs/badges").mkdir(parents=True, exist_ok=True)

for _, row in df.iterrows():
    control = row['control']
    score = row['score']
    badge_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="100" height="20"><text x="0" y="15">{control}: {score}%</text></svg>'
    with open(f"outputs/badges/{control}.svg", "w") as f:
        f.write(badge_content)

print("Badges generated successfully.")
