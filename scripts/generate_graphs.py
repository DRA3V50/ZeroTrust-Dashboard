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

# --- Zero Trust Posture Graph ---
# Map colors based on score
colors_zt = []
for score in scores:
    if score >= 90:
        colors_zt.append("green")
    elif score >= 80:
        colors_zt.append("orange")
    else:
        colors_zt.append("red")

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors_zt)
plt.title("Zero Trust Posture Scores", color="white")
plt.ylabel("Score (%)", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.savefig("outputs/graphs/zero_trust_posture.png", dpi=100, bbox_inches='tight')
plt.close()
print("Zero Trust posture graph saved.")

# --- ISO 27001 Coverage Graph ---
# Different coloring for ISO 27001 emphasis
colors_iso = []
for score in scores:
    if score >= 90:
        colors_iso.append("#1f77b4")  # blue
    elif score >= 80:
        colors_iso.append("#ff7f0e")  # orange
    else:
        colors_iso.append("#d62728")  # red

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors_iso)
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score (%)", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.savefig("outputs/graphs/iso_27001_coverage.png", dpi=100, bbox_inches='tight')
plt.close()
print("ISO 27001 coverage graph saved.")
