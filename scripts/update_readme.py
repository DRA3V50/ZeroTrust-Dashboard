import os
from create_controls_db import db_path
import sqlite3

readme_file = "README.md"

with open(readme_file, "r") as f:
    lines = f.readlines()

# Find section markers to replace graphs and badges
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

# Update graphs
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    "![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)\n",
]

# Update badges
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n"]
badge_files = sorted(os.listdir("outputs/badges"))
for file in badge_files:
    if file.endswith(".svg"):
        badge_lines.append(f"![{file[:-4]}](outputs/badges/{file})\n")

# Update metrics table
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls")
data = c.fetchall()
conn.close()

table_lines = [
    "### 🗂 Metrics Table\n",
    "| Control | Domain | Score (%) |\n",
    "|---------|--------|-----------|\n",
]

for control, domain, score in data:
    table_lines.append(f"| {control} | {domain} | {score} |\n")

# Replace old sections
lines[start_graph_idx:start_badge_idx] = graph_lines
lines[start_badge_idx:start_table_idx] = badge_lines
lines[start_table_idx:] = table_lines

with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics.")
