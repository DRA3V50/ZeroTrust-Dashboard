#!/usr/bin/env python3
import sqlite3
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"

ZERO_TRUST_DOMAINS = ["Identity", "Device", "Network", "Application", "Data"]
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

os.makedirs(GRAPH_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, domain, score FROM controls")
rows = cursor.fetchall()
conn.close()

control_scores = {row[0]: row[2] for row in rows}
domain_scores = {row[1]: row[2] for row in rows if row[1] in ZERO_TRUST_DOMAINS}

# Zero Trust Graph
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,5))

colors = []
scores_list = []
for domain in ZERO_TRUST_DOMAINS:
    score = domain_scores.get(domain, 0)
    scores_list.append(score)
    if score < 60:
        colors.append("#FF4136")
    elif score < 80:
        colors.append("#FF851B")
    else:
        colors.append("#2ECC40")

ax.bar(ZERO_TRUST_DOMAINS, scores_list, color=colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("Zero Trust Posture")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
for i, v in enumerate(scores_list):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png")
plt.close()

# ISO 27001 Graph
fig, ax = plt.subplots(figsize=(10,5))
iso_colors = []
iso_scores = []
for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    iso_scores.append(score)
    if score < 60:
        iso_colors.append("#FF4136")
    elif score < 80:
        iso_colors.append("#FF851B")
    else:
        iso_colors.append("#0074D9")

ax.bar(ISO_CONTROLS, iso_scores, color=iso_colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("ISO 27001 Compliance Coverage")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
for i, v in enumerate(iso_scores):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png")
plt.close()
