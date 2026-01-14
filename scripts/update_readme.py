import os
import sqlite3
from create_controls_db import db_path

readme_file = "README.md"

with open(readme_file, "r") as f:
    lines = f.readlines()

# Identify section markers
start_graph_idx = start_badge_idx = start_table_idx = None
for i, line in enumerate(lines):
    if line.startswith("### Latest Zero Trust Posture"):
        start_graph_idx = i
    if line.startswith("### Real-Time Badges"):
        start_badge_idx = i
    if line.startswith("### 🗂 Metrics Table"):
        start_table_idx = i

# Update graphs
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    "![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)\n",
    "![ISO 27001 Coverage](outputs/graphs/iso_27001_coverage.png)\n"
]

# Update badges (sorted by score descending)
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n"]
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

# Sort descending by score
data.sort(key=lambda x: x[1], reverse=True)

for control, score in data:
    badge_lines.append(f"![{control}](outputs/badges/{control}.svg)\n")

# Metrics table (tab-separated)
table_lines = ["### 🗂 Metrics Table\n", "control\tdomain\tscore\n"]
for control, domain, score in data:
    table_lines.append(f"{control}\t{domain}\t{score}\n")

# Replace sections
lines[start_graph_idx:start_badge_idx] = graph_lines
lines[start_badge_idx:start_table_idx] = badge_lines
lines[start_table_idx:] = table_lines

with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics.")
