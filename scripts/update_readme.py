#!/usr/bin/env python3
import os
import sqlite3

DB_PATH = "data/controls.db"
README_PATH = "README.md"

def get_metrics():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT control, domain, score FROM controls ORDER BY control")
    data = c.fetchall()
    conn.close()
    return data

def generate_graphs_section():
    return (
        "### Latest Zero Trust Posture\n"
        "- Updated daily, showing actionable insight for analysts and leadership.\n"
        '<div style="text-align:center;">\n'
        '  <img src="outputs/graphs/zero_trust_posture.png" '
        'alt="Zero Trust Scores" width="45%" style="display:inline-block; margin-right:5px;"/>\n'
        '  <img src="outputs/graphs/iso_27001_coverage.png" '
        'alt="ISO 27001 Coverage" width="45%" style="display:inline-block;"/>\n'
        "</div>\n\n"
    )

def generate_badges_section(metrics_data):
    badges_md = "### Real-Time Badges\n- Summarizes individual control statuses with dynamic updates.\n"
    badges_md += '<div style="text-align:center;">\n'
    for control, _, _ in metrics_data:
        badges_md += (
            f'  <img src="outputs/badges/{control}.svg" alt="{control}" '
            'style="height:20px; margin:2px;"/>\n'
        )
    badges_md += "</div>\n\n"
    return badges_md

def generate_table_section(metrics_data):
    table_md = "### 🗂 Metrics Table\n"
    table_md += "| Control | Domain | Score (%) |\n"
    table_md += "|---------|--------|------------|\n"
    for control, domain, score in metrics_data:
        table_md += f"| {control} | {domain} | {score} |\n"
    table_md += "\n"
    return table_md

def update_readme():
    # Read original README
    with open(README_PATH, "r") as f:
        lines = f.readlines()

    # Load metrics from DB
    metrics_data = get_metrics()

    # Build replacement content
    graphs_section = generate_graphs_section()
    badges_section = generate_badges_section(metrics_data)
    table_section = generate_table_section(metrics_data)

    # Find where to replace
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## 📊 Dashboards and Badges"):
            start_idx = i
            break

    if start_idx is None:
        raise Exception("Could not find '## 📊 Dashboards and Badges' marker in README.md")

    # Find next top-level section (## ) after start_idx
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## ") and j > start_idx:
            end_idx = j
            break
    if end_idx is None:
        end_idx = len(lines)

    # Replace that entire section
    new_section = (
        "## 📊 Dashboards and Badges\n\n"
        + graphs_section
        + badges_section
        + table_section
    )
    updated = lines[:start_idx] + [new_section] + lines[end_idx:]

    # Write updated README
    with open(README_PATH, "w") as f:
        f.writelines(updated)

    print("README.md updated successfully — graphs, badges, and table refreshed.")

if __name__ == "__main__":
    update_readme()
