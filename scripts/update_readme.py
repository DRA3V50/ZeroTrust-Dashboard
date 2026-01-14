import os
import sqlite3
from create_controls_db import db_path

readme_file = "README.md"

with open(readme_file, "r") as f:
    lines = f.readlines()

def find_section_index(lines, header):
    for i, line in enumerate(lines):
        if line.strip() == header:
            return i
    return -1

# Find indices of the sections to replace
graph_start = find_section_index(lines, "### Latest Zero Trust Posture")
badge_start = find_section_index(lines, "### Real-Time Badges")
metrics_start = find_section_index(lines, "### 🗂 Metrics Table")

if graph_start == -1 or badge_start == -1 or metrics_start == -1:
    print("Error: Could not find all required section headers in README.md")
    exit(1)

# Find the end of each section (start of next or EOF)
def find_section_end(start_idx):
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith("### ") and i != start_idx:
            return i
    return len(lines)

graph_end = badge_start
badge_end = metrics_start
metrics_end = find_section_end(metrics_start)

# Prepare new content for graphs section
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    "![Zero Trust Scores](outputs/graphs/zero_trust_posture.png)\n",
    "![ISO 27001 Coverage](outputs/graphs/iso_27001_coverage.png)\n",
]

# Prepare new content for badges section
badge_files = sorted(f for f in os.listdir("outputs/badges") if f.endswith(".svg"))
badge_lines = [
    "### Real-Time Badges\n",
    "- Summarizes individual control statuses with dynamic updates.\n",
    "\n"
]
# Add badges inline
for file in badge_files:
    badge_lines.append(f"![{file[:-4]}](outputs/badges/{file}) ")

badge_lines.append("\n\n")

# Prepare new content for metrics table section
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT control, domain, score FROM controls ORDER BY control ASC")
data = c.fetchall()
conn.close()

table_lines = [
    "### 🗂 Metrics Table\n",
    "| Control | Domain | Score (%) |\n",
    "|---------|--------|-----------|\n",
]

for control, domain, score in data:
    table_lines.append(f"| {control} | {domain} | {score} |\n")

# Replace old sections with new content
lines[graph_start:graph_end] = graph_lines
lines[badge_start:badge_end] = badge_lines
lines[metrics_start:metrics_end] = table_lines

# Write back to README.md
with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics.")
