import os
from create_controls_db import db_path
import sqlite3

readme_file = "README.md"

with open(readme_file, "r") as f:
    lines = f.readlines()

# Find the section start indices for the parts to update
start_graph_idx = None
start_badge_idx = None
start_table_idx = None
end_table_idx = None

for i, line in enumerate(lines):
    if line.strip() == "### Latest Zero Trust Posture":
        start_graph_idx = i
    elif line.strip() == "### Real-Time Badges":
        start_badge_idx = i
    elif line.strip() == "### 🗂 Metrics Table":
        start_table_idx = i

# To find where metrics table ends, look for the next section or end of file
for i in range(start_table_idx + 1, len(lines)):
    if lines[i].startswith("### ") and i > start_table_idx:
        end_table_idx = i
        break
if end_table_idx is None:
    end_table_idx = len(lines)

# Prepare new graph lines (two graphs side by side)
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    '<img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block"/>\n',
    '<img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block"/>\n',
    "\n"
]

# Prepare new badge lines with inline images (small icons)
badge_lines = [
    "### Real-Time Badges\n",
    "- Summarizes individual control statuses with dynamic updates.\n",
    "\n"
]

badge_files = sorted(f for f in os.listdir("outputs/badges") if f.endswith(".svg"))
for file in badge_files:
    control_name = file[:-4]
    badge_lines.append(f'<img src="outputs/badges/{file}" alt="{control_name}" style="height: 20px; margin-right: 5px;"/>\n')

badge_lines.append("\n")

# Prepare metrics table lines (simple markdown table)
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls ORDER BY control")
data = c.fetchall()
conn.close()

table_lines = [
    "### 🗂 Metrics Table\n",
    "| Control | Domain | Score (%) |\n",
    "|---------|--------|-----------|\n",
]

for control, domain, score in data:
    table_lines.append(f"| {control} | {domain} | {score} |\n")

table_lines.append("\n")

# Replace old sections with new lines
lines[start_graph_idx:start_badge_idx] = graph_lines
lines[start_badge_idx:start_table_idx] = badge_lines
lines[start_table_idx:end_table_idx] = table_lines

# Write back updated README
with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics (preserving original structure).")
