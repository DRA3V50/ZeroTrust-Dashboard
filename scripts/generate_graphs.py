# scripts/generate_graphs.py
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

# Zero Trust posture graph with color coding
colors = []
for s in scores:
    if s >= 90:
        colors.append('green')
    elif s >= 75:
        colors.append('orange')
    else:
        colors.append('red')

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors)
plt.title("Zero Trust / ISO 27001 Scores", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.ylim(0, 100)

graph_file = "outputs/graphs/zero_trust_posture.png"
plt.savefig(graph_file, dpi=100, bbox_inches='tight')
plt.close()
print(f"Zero Trust posture graph saved: {graph_file}")

# ISO 27001 coverage graph (simple blue bar)
plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color="#1f77b4")
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.ylim(0, 100)

iso_graph_file = "outputs/graphs/iso_27001_coverage.png"
plt.savefig(iso_graph_file, dpi=100, bbox_inches='tight')
plt.close()
print(f"ISO 27001 coverage graph saved: {iso_graph_file}")
