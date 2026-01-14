import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
db_path = Path("data/controls.db")
graphs_dir = Path("outputs/graphs")
graphs_dir.mkdir(parents=True, exist_ok=True)

# Connect to DB
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Zero Trust Posture Graph
domains = df['domain'].tolist()
scores = df['score'].tolist()
plt.figure(figsize=(6,3))
plt.bar(domains, scores, color='teal')
plt.title("Zero Trust Posture")
plt.ylim(0,100)
plt.savefig(graphs_dir / "zero_trust_posture.png", dpi=150)
plt.close()

# ISO 27001 Coverage Graph
plt.figure(figsize=(6,3))
plt.bar(df['control'], df['score'], color='orange')
plt.title("ISO 27001 Control Coverage")
plt.ylim(0,100)
plt.savefig(graphs_dir / "iso_27001_coverage.png", dpi=150)
plt.close()

print("Graphs generated successfully.")
