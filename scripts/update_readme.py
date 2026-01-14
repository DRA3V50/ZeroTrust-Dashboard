import os

readme_file = "README.md"
metrics_file = "reports/metrics_table.md"

# Read current README
with open(readme_file, "r") as f:
    lines = f.readlines()

# Find section markers
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

# Update graphs section (inline images)
graph_lines = [
    "### Latest Zero Trust Posture\n",
    "- Updated daily, showing actionable insight for analysts and leadership.\n",
    '<img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block"/>\n',
    '<img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block"/>\n'
]

# Update badges (latest only)
badge_lines = ["### Real-Time Badges\n", "- Summarizes individual control statuses with dynamic updates.\n"]
badge_files = sorted([f for f in os.listdir("outputs/badges") if f.endswith(".svg") and "_" not in f])
for file in badge_files:
    badge_lines.append(f'<img src="outputs/badges/{file}" alt="{file[:-4]}" style="height: 20px; margin-right: 5px;"/>\n')

# Update metrics table
with open(metrics_file, "r") as f:
    table_lines = ["### 🗂 Metrics Table\n"] + f.readlines()

# Replace old sections
lines[start_graph_idx:start_badge_idx] = graph_lines
lines[start_badge_idx:start_table_idx] = badge_lines
lines[start_table_idx:] = table_lines

# Write updated README
with open(readme_file, "w") as f:
    f.writelines(lines)

print("README.md updated with latest graphs, badges, and metrics.")
