import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
db_path = Path("data/controls.db")
graphs_dir = Path("outputs/graphs")
graphs_dir.mkdir(parents=True, exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Read controls from database
df = pd.read_sql("SELECT * FROM controls", conn)

# Generate Zero Trust posture graph
zt_scores = df.groupby("domain")["score"].mean()
plt.figure(figsize=(4,3))  # small figure for badge-style output
zt_scores.plot(kind="bar", color="teal", edgecolor="black")
plt.ylim(0,100)
plt.title("Zero Trust Posture")
plt.ylabel("Score (%)")
plt.tight_layout()
plt.savefig(graphs_dir / "zero_trust_posture.png", dpi=100)
plt.close()

# Generate ISO 27001 coverage graph
iso_scores = df.groupby("control")["score"].mean()
plt.figure(figsize=(4,3))
iso_scores.plot(kind="bar", color="darkorange", edgecolor="black")
plt.ylim(0,100)
plt.title("ISO 27001 Control Coverage")
plt.ylabel("Score (%)")
plt.tight_layout()
plt.savefig(graphs_dir / "iso_27001_coverage.png", dpi=100)
plt.close()

print("Graphs generated successfully.")
