import sqlite3
import matplotlib.pyplot as plt
import os
from create_controls_db import db_path

# Ensure output directory exists
os.makedirs("outputs/graphs", exist_ok=True)

# Read data from database
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

controls = [row[0] for row in data]
scores = [row[1] for row in data]

# -------------------------------
# Zero Trust Posture Graph
# -------------------------------
# Color logic:
# 🔴 Red     = score < 60  (Critical)
# 🟠 Orange  = 60 <= score < 80 (Warning)
# 🟢 Green   = score >= 80 (Healthy)
colors_zt = []
for score in scores:
    if score >= 80:
        colors_zt.append("green")
    elif score >= 60:
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
plt.ylim(0, 100)

zero_trust_file = "outputs/graphs/zero_trust_posture.png"
plt.savefig(zero_trust_file, dpi=100, bbox_inches="tight")
plt.close()
print(f"Zero Trust posture graph saved: {zero_trust_file}")

# -------------------------------
# ISO 27001 Coverage Graph
# -------------------------------
# Color logic:
# 🔴 Red     = score < 60  (Non‑compliant)
# 🟠 Orange  = 60 <= score < 80 (Partial / Warning)
# 🔵 Blue    = score >= 80 (Compliant / Covered)
colors_iso = []
for score in scores:
    if score >= 80:
        colors_iso.append("#1f77b4")  # Blue for compliant/covered
    elif score >= 60:
        colors_iso.append("orange")
    else:
        colors_iso.append("red")

plt.figure(figsize=(6, 4))
plt.bar(controls, scores, color=colors_iso)
plt.title("ISO 27001 Control Coverage", color="white")
plt.ylabel("Score (%)", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")
plt.gcf().patch.set_facecolor("#2E2E2E")
plt.ylim(0, 100)

iso_coverage_file = "outputs/graphs/iso_27001_coverage.png"
plt.savefig(iso_coverage_file, dpi=100, bbox_inches="tight")
plt.close()
print(f"ISO 27001 coverage graph saved: {iso_coverage_file}")
