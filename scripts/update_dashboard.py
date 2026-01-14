import sqlite3
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from pybadges import badge

# --- Configuration ---
DB_PATH = "data/controls.db"
README_PATH = "README.md"
GRAPH_DIR = "outputs/graphs"
BADGE_DIR = "outputs/badges"

ZERO_TRUST_DOMAINS = ["Identity", "Device", "Network", "Application", "Data"]
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

# Ensure directories exist
os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# --- Step 1: Read data from SQLite ---
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, domain, score FROM controls")
rows = cursor.fetchall()
conn.close()

control_scores = {row[0]: row[2] for row in rows}
domain_scores = {row[1]: row[2] for row in rows if row[1] in ZERO_TRUST_DOMAINS}

# --- Step 2: Generate Zero Trust Posture Graph ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8,4))
colors = []
for domain in ZERO_TRUST_DOMAINS:
    score = domain_scores.get(domain, 0)
    if score < 60:
        colors.append("red")
    elif score < 80:
        colors.append("orange")
    else:
        colors.append("green")
ax.bar(ZERO_TRUST_DOMAINS, [domain_scores.get(d,0) for d in ZERO_TRUST_DOMAINS], color=colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("Zero Trust Posture")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png")
plt.close()

# --- Step 3: Generate ISO 27001 Coverage Graph ---
iso_colors = []
for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    if score < 60:
        iso_colors.append("red")
    elif score < 80:
        iso_colors.append("orange")
    else:
        iso_colors.append("blue")  # compliant

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(ISO_CONTROLS, [control_scores.get(c,0) for c in ISO_CONTROLS], color=iso_colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("ISO 27001 Compliance Coverage")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png")
plt.close()

# --- Step 4: Generate badges ---
badge_lines = []
for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    color = "green" if score >= 80 else "orange" if score >= 60 else "red"
    badge_svg = badge(
        label=control,
        message=str(score),
        color=color
    )
    badge_file = f"{BADGE_DIR}/{control}.svg"
    with open(badge_file, "w") as f:
        f.write(badge_svg)
    badge_lines.append(f'<img src="{badge_file}" alt="{control}" style="height:20px; margin:2px;"/>')

# --- Step 5: Generate Metrics Table ---
table_lines = ["| Control | Domain | Score (%) |",
               "|---------|--------|-----------|"]
for control in ISO_CONTROLS:
    domain = next((row[1] for row in rows if row[0] == control), "")
    score = control_scores.get(control, 0)
    table_lines.append(f"| {control} | {domain} | {score} |")

# --- Step 6: Update README ---
with open(README_PATH, "r", encoding="utf-8") as f:
    readme_text = f.read()

readme_text = readme_text.replace("{{BADGES}}", "\n".join(badge_lines))
readme_text = readme_text.replace("{{METRICS_TABLE}}", "\n".join(table_lines))

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(readme_text)

print("README, badges, table, and graphs updated successfully!")
