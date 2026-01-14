import sqlite3
import matplotlib.pyplot as plt
import os
from create_controls_db import db_path

os.makedirs("outputs/graphs", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

controls = [row[0] for row in data]
scores = [row[1] for row in data]

# Define colors for Zero Trust graph: green >=90, yellow 80-89, red <80
colors = ["green" if s >= 90 else "orange" if s >= 80 else "red" for s in scores]

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors)
plt.title("Zero Trust / ISO 27001 Scores", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor('#2E2E2E')

graph_file = "outputs/graphs/zero_trust_posture.png"
plt.savefig(graph_file, dpi=100, bbox_inches='tight')
plt.close()
print(f"Graph saved to {graph_file}")

# ISO 27001 coverage graph (all blue for clarity)
plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color="#1f77b4")
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor('#2E2E2E')

iso_graph_file = "outputs/graphs/iso_27001_coverage.png"
plt.savefig(iso_graph_file, dpi=100, bbox_inches='tight')
plt.close()
print(f"ISO 27001 coverage graph saved to {iso_graph_file}")
