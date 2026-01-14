#!/usr/bin/env python3
import sqlite3
from datetime import datetime

# Paths
DB_PATH = "data/controls.db"
README_PATH = "README.md"

# Load metrics from database
def load_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT control, domain, score FROM controls ORDER BY control")
    data = cursor.fetchall()
    conn.close()
    return data

# Generate Markdown table
def generate_metrics_table(data):
    table_md = "| Control | Domain | Score |\n"
    table_md += "|---------|------------------|-------|\n"
    for control, domain, score in data:
        table_md += f"| {control} | {domain} | {score} |\n"
    return table_md

# Generate badges Markdown
def generate_badges(data):
    badges_md = '<div style="text-align:center;">\n'
    for control, _, _ in data:
        badges_md += f'  <img src="outputs/badges/{control}.svg" alt="{control}" style="height:20px; margin:2px;"/>\n'
    badges_md += "</div>\n"
    return badges_md

# Generate graphs Markdown
def generate_graphs_md():
    graphs_md = """
<div style="text-align:center;">
  <img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block; margin-right:5px;"/>
  <img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block;"/>
</div>
"""
    return graphs_md

# Main update function
def update_readme():
    # Load metrics
    data = load_metrics()

    # Generate sections
    metrics_table_md = generate_metrics_table(data)
    badges_md = generate_badges(data)
    graphs_md = generate_graphs_md()

    # Read current README
    with open(README_PATH, "r") as f:
        readme_lines = f.readlines()

    # Define markers to replace section
    start_marker = "## 📊 Dashboards and Badges"
    start_idx = None
    for i, line in enumerate(readme_lines):
        if line.strip() == start_marker:
            start_idx = i
            break

    if start_idx is None:
        raise ValueError(f"Start marker '{start_marker}' not found in README.md")

    # Replace everything after the marker until next H2 (##) or end of file
    end_idx = len(readme_lines)
    for i in range(start_idx + 1, len(readme_lines)):
        if readme_lines[i].startswith("## "):
            end_idx = i
            break

    new_section = f"{start_marker}\n\n### Latest Zero Trust Posture\n- Updated daily, showing actionable insight for analysts and leadership.\n{graphs_md}\n### Real-Time Badges\n- Summarizes individual control statuses with dynamic updates.\n{badges_md}\n### 🗂 Metrics Table\n{metrics_table_md}\n"

    updated_lines = readme_lines[:start_idx] + [new_section] + readme_lines[end_idx:]

    # Write back
    with open(README_PATH, "w") as f:
        f.writelines(updated_lines)

    print("README.md updated successfully.")

if __name__ == "__main__":
    update_readme()
