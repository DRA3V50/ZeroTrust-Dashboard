import pandas as pd
import os
import sqlite3

from create_controls_db import db_path

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

os.makedirs("outputs/badges", exist_ok=True)

# Simple badge generator (replace with your logic)
for _, row in df.iterrows():
    filename = f"outputs/badges/{row['control']}.svg"
    content = f"<svg><text>{row['control']}: {row['score']}%</text></svg>"
    with open(filename, "w") as f:
        f.write(content)

print("Badges generated successfully.")
