import os
import sqlite3
from create_controls_db import db_path

readme_file = "README.md"

# Read existing README
with open(readme_file, "r") as f:
    lines = f.readlines()

# Find section markers
graph_idx = None
badge_idx = None
table_idx = None

for i, line in enumerate(lines):
    if line.startswith("### Latest Zero Trust Posture"):
        graph_idx = i
    if line.startswith("### Real-Time Badges"):
        badge_idx = i
    if line.startswith("### 🗂 Metrics Table"):
        table_idx = i

# Update graphs (side by side)
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    '<div style="text-align:center;">\n',
    '<img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block; margin-right:5px;"/>\n',
    '<img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block;"/>\n',
    '</div>\n'
]

# Update badges (inline, small, unique)
badge_files = sorted(f for f in os.listdir("outputs/badges") if f.endswith(".svg"))
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n", '<div style="text-align:center;">\n']
for file in badge_files:
    badge_lines.append(f'<img src="outputs/badges/{file}" alt="{file[:-4]}" style="height:20px; margin:2px;"/>\n')
badge_lines.append('</div>\n')

# Update metrics table (tab-delimited)
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls ORDER BY control")
data = c.fetchall()
conn.close()

table_lines = ["### 🗂 Metrics Table\n"]
table_lines.append("control\tdomain\tscore\n")
for control, domain, score in data:
    table_lines.append(f"{control}\t{domain}\t{score}\n")

# Replace sections
lines[graph_idx:badge_idx] = graph_lines
lines[badge_idx:table_idx] = badge_lines
lines[table_idx:] = table_lines

# Write back
with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with graphs, badges, and metrics table correctly.")
