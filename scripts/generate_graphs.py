import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from scripts.create_controls_db import db_path

# Ensure database exists
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

graphs_dir = Path("outputs/graphs")
graphs_dir.mkdir(parents=True, exist_ok=True)

# Dark theme
plt.style.use('dark_background')

# Zero Trust Posture Graph
plt.figure(figsize=(6, 4))
plt.bar(df['control'], df['score'], color='deepskyblue')
plt.title("Zero Trust Posture", color="white")
plt.ylabel("Score (%)", color="white")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(graphs_dir / "zero_trust_posture.png")
plt.close()

# ISO 27001 Control Coverage Graph
plt.figure(figsize=(6, 4))
plt.bar(df['control'], df['score'], color='orange')
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score (%)", color="white")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(graphs_dir / "iso_27001_coverage.png")
plt.close()

print("Graphs generated successfully.")
