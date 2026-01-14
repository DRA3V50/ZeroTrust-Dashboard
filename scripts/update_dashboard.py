import sqlite3
import random
from pathlib import Path

# Ensure data directory exists
data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)
db_path = data_dir / "controls.db"

# Initialize database if missing
from scripts.create_controls_db import db_path as db_check_path
import scripts.create_controls_db

# Connect to database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Update scores randomly (replace with real logic)
controls = c.execute("SELECT control FROM controls").fetchall()
for (control,) in controls:
    new_score = random.randint(70, 100)  # Randomized for demo/testing
    c.execute("UPDATE controls SET score = ? WHERE control = ?", (new_score, control))

conn.commit()
conn.close()
print("Dashboard data updated successfully.")
