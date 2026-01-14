import sqlite3
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

DB_PATH = "data/controls.db"
GRAPH_DIR = "outputs/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

ZERO_TRUST_DOMAINS = ["Identity", "Device", "Network", "Application", "Data"]
ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT control, domain, score FROM controls")
rows = cursor.fetchall()
conn.close()

# Aggregate domain scores: average scores for each domain (if multiple controls per domain)
domain_scores = {}
domain_counts = {}
for _, domain, score in rows:
    if domain in ZERO_TRUST_DOMAINS:
        domain_scores[domain] = domain_scores.get(domain, 0) + score
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

# Calculate average scores per domain
for domain in ZERO_TRUST_DOMAINS:
    if domain in domain_scores and domain_counts.get(domain, 0) > 0:
        domain_scores[domain] = domain_scores[domain] / domain_counts[domain]
    else:
        domain_scores[domain] = 0

# Prepare colors for Zero Trust graph
colors = []
for domain in ZERO_TRUST_DOMAINS:
    score = domain_scores.get(domain, 0)
    if score < 60:
        colors.append("red")
    elif score < 80:
        colors.append("orange")  # Use proper orange, not goldish
    else:
        colors.append("green")

# Plot Zero Trust Posture
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))  # Larger figure for readability
bars = ax.bar(ZERO_TRUST_DOMAINS, [domain_scores[d] for d in ZERO_TRUST_DOMAINS], color=colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)", fontsize=14)
ax.set_title("Zero Trust Posture", fontsize=16)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add numeric labels on bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset label slightly above bar
                textcoords="offset points",
                ha='center', va='bottom', fontsize=12, color='white')

plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/zero_trust_posture.png")
plt.close()

# Prepare ISO controls scores & colors
control_scores = {row[0]: row[2] for row in rows}
iso_colors = []
for control in ISO_CONTROLS:
    score = control_scores.get(control, 0)
    if score < 60:
        iso_colors.append("red")
    elif score < 80:
        iso_colors.append("orange")
    else:
        iso_colors.append("blue")

# Plot ISO 27001 Coverage
fig, ax = plt.subplots(figsize=(12, 6))  # Larger figure
bars = ax.bar(ISO_CONTROLS, [control_scores.get(c, 0) for c in ISO_CONTROLS], color=iso_colors)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)", fontsize=14)
ax.set_title("ISO 27001 Compliance Coverage", fontsize=16)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=12, color='white')

plt.tight_layout()
plt.savefig(f"{GRAPH_DIR}/iso_27001_coverage.png")
plt.close()

print("Graphs generated with improved style and correct data.")
