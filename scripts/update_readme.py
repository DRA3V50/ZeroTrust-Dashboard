#!/usr/bin/env python3
import sqlite3
import os

README_PATH = "README.md"
GRAPH_DIR = "outputs/graphs"
BADGE_DIR = "outputs/badges"
DB_PATH = "data/controls.db"

ISO_CONTROLS = ["A.5.1", "A.6.1", "A.8.2", "A.9.2"]

def fetch_metrics():
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
        f'<div style="text-align:center;">\n'
        f'  <img src="{GRAPH_DIR}/zero_trust_posture.png" alt="Zero Trust Scores" width="80%" '
        'style="display:block; margin: 10px auto;"/>\n'
        f'  <img src="{GRAPH_DIR}/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="80%" '
        'style="display:block; margin: 10px auto;"/>\n'
        "</div>\n\n"
    )

def generate_badges_section(metrics):
    md = "### Real-Time Badges\n- Summarizes individual control statuses with dynamic updates.\n"
    md += '<div style="text-align:center;">\n'
    for control, _, _ in metrics:
        md += f'  <img src="{BADGE_DIR}/{control}.svg" alt="{control}" style="height:20px; margin:2px;"/>\n'
    md += "</div>\n\n"
    return md

def generate_table_section(metrics):
    md = "### 🗂 Metrics Table\n"
    md += "| Control | Domain | Score (%) |\n"
    md += "|---------|--------|-----------|\n"
    for control, domain, score in metrics:
        md += f"| {control} | {domain} | {score} |\n"
    md += "\n"
    return md

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    metrics = fetch_metrics()

    graphs_sec = generate_graphs_section()
    badges_sec = generate_badges_section(metrics)
    table_sec = generate_table_section(metrics)

    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip() == "## 📊 Security Dashboard 🗂️":
            start = i
            break
    if start is None:
        raise RuntimeError("Could not find '## 📊 Security Dashboard 🗂️' in README.md")

    # Find next section header after start (to mark end of current section)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## ") and j > start:
            end = j
            break
    if end is None:
        end = len(lines)

    # Replace entire section with new content (without Color Codes)
    new_section = (
        "## 📊 Security Dashboard 🗂️\n\n"
        + graphs_sec
        + badges_sec
        + table_sec
    )

    updated_lines = lines[:start] + [new_section] + lines[end:]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("README.md updated with latest graphs, badges, and table (Color Codes removed from dynamic update).")

if __name__ == "__main__":
    update_readme()
