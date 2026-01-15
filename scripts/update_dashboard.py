#!/usr/bin/env python3
import sqlite3
import os
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from pybadges import badge

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"
BADGE_DIR = "outputs/badges"

ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]
ZERO_TRUST_DOMAINS = ["Identity", "Device", "Network", "Application", "Data"]

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(BADGE_DIR, exist_ok=True)

# Fetch data
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls")
rows = c.fetchall()
conn.close()

control_scores = {r[0]: r[2] for r in rows}
domain_scores = {r[0]: r[2] for r in rows if r[0] in ZERO_TRUST_DOMAINS}

# --- Zero Trust Graph ---
fig, ax = plt.subplots(figsize=(10,5))
scores_zt = [domain_scores.get(d, 0) for d in ZERO_TRUST_DOMAINS]
colors_zt = [
    "#FF4136" if s < 60 else "#FF851B" if s < 80 else "#2ECC40"
    for s in scores_zt
]
ax.bar(ZERO_TRUST_DOMAINS, scores_zt, color=colors_zt)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("Zero Trust Posture")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
for i, v in enumerate(scores_zt):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png")
plt.close()

# --- ISO 27001 Graph ---
fig, ax = plt.subplots(figsize=(10,5))
scores_iso = [control_scores.get(c, 0) for c in ISO_CONTROLS]
colors_iso = [
    "#FF4136" if s < 60 else "#FF851B" if s < 80 else "#0074D9"
    for s in scores_iso
]
ax.bar(ISO_CONTROLS, scores_iso, color=colors_iso)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("ISO 27001 Compliance Coverage")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
for i, v in enumerate(scores_iso):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png")
plt.close()

# --- Generate Badges ---
for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    color = "green" if score >= 80 else "orange" if score >= 60 else "red"
    svg = badge(left_text=control, right_text=str(score), right_color=color)
    with open(f"{BADGE_DIR}/{control}.svg", "w") as f:
        f.write(svg)
