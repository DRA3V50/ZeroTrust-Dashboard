import sqlite3
import matplotlib.pyplot as plt
import os
from create_controls_db import db_path

os.makedirs("outputs/graphs", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Fetch scores for all controls
c.execute("SELECT control, score FROM controls")
data = c.fetchall()

# Separate controls and scores
controls = [row[0] for row in data]
scores = [row[1] for row in data]

def color_for_score(score):
    if score >= 90:
        return "green"
    elif score >= 75:
        return "orange"
    else:
        return "red"

# Zero Trust Graph - use the scores as-is
colors_zero_trust = [color_for_score(score) for score in scores]

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors_zero_trust)
plt.title("Zero Trust Scores", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/graphs/zero_trust_posture.png", dpi=100)
plt.close()
print("Zero Trust posture graph saved.")

# ISO 27001 Coverage Graph
# For demonstration, use the same scores but change colors slightly to blue shades

def iso_color_for_score(score):
    if score >= 90:
        return "#2ca02c"  # green
    elif score >= 75:
        return "#ff7f0e"  # orange
    else:
        return "#d62728"  # red

colors_iso = [iso_color_for_score(score) for score in scores]

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors_iso)
plt.title("ISO 27001 Coverage", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/graphs/iso_27001_coverage.png", dpi=100)
plt.close()
print("ISO 27001 coverage graph saved.")

conn.close()
