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

# Zero Trust Posture graph with color thresholds
colors = []
for s in scores:
    if s >= 90:
        colors.append("green")
    elif s >= 75:
        colors.append("orange")
    else:
        colors.append("red")

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors)
plt.title("Zero Trust / ISO 27001 Scores", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
graph_file = "outputs/graphs/zero_trust_posture.png"
plt.savefig(graph_file, dpi=100, bbox_inches="tight")
plt.close()
print("Zero Trust posture graph saved.")

# ISO 27001 coverage graph (blue by default)
plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color="#1f77b4")
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
graph_file_iso = "outputs/graphs/iso_27001_coverage.png"
plt.savefig(graph_file_iso, dpi=100, bbox_inches="tight")
plt.close()
print("ISO 27001 coverage graph saved.")
