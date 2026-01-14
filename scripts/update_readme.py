# scripts/update_readme.py
import os
import sqlite3
from create_controls_db import db_path

readme_file = "README.md"
with open(readme_file, "r") as f:
    lines = f.readlines()

# Preserve everything, only update badges, graphs, table
start_graph_idx = None
start_badge_idx = None
start_table_idx = None

for i, line in enumerate(lines):
    if line.startswith("### Latest Zero Trust Posture"):
        start_graph_idx = i
    if line.startswith("### Real-Time Badges"):
        start_badge_idx = i
    if line.startswith("### 🗂 Metrics Table"):
        start_table_idx = i

# Graph section
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    '<img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block"/>\n',
    '<img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block"/>\n'
]

# Badge section
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n"]
badge_files = sorted([f for f in os.listdir("outputs/badges") if f.endswith(".svg")])
for file in badge_files:
    badge_lines.append(f'<img src="outputs/badges/{file}" alt="{file[:-4]}" style="height:20px; margin-right:5px;"/>\n')

# Metrics table
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls ORDER BY control")
data = c.fetchall()
conn.close()

table_lines = [
    "### 🗂 Metrics Table\n",
    "control\tdomain\tscore\n"
]
for control, domain, score in data:
    table_lines.append(f"{control}\t{domain}\t{score}\n")

# Replace sections
lines[start_graph_idx:start_badge_idx] = graph_lines
lines[start_badge_idx:start_table_idx] = badge_lines
lines[start_table_idx:] = table_lines

with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated successfully with latest graphs, badges, and metrics.")
