import os
import sqlite3
from create_controls_db import db_path

readme_file = "README.md"

with open(readme_file, "r") as f:
    lines = f.readlines()

# Locate sections
def find_line_start(prefix):
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            return i
    return None

graph_idx = find_line_start("### Latest Zero Trust Posture")
badge_idx = find_line_start("### Real-Time Badges")
table_idx = find_line_start("### 🗂 Metrics Table")

# --- Graphs ---
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    '<img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block"/>\n',
    '<img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block"/>\n'
]
lines[graph_idx:badge_idx] = graph_lines

# --- Badges ---
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n"]
badge_files = sorted(os.listdir("outputs/badges"))
for file in badge_files:
    if file.endswith(".svg"):
        badge_lines.append(f'<img src="outputs/badges/{file}" alt="{file[:-4]}" style="height: 20px; margin-right: 5px;"/>\n')
lines[badge_idx:table_idx] = badge_lines

# --- Metrics table ---
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
lines[table_idx:table_idx+len(lines)] = table_lines

with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics table.")
