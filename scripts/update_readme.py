#!/usr/bin/env python3
import sqlite3

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
        "- Updated daily.\n"
        f'<div style="text-align:center;">\n'
        f'  <img src="{GRAPH_DIR}/zero_trust_posture.png" alt="Zero Trust Scores" width="60%" style="display:inline-block; margin-right:10px;"/>\n'
        f'  <img src="{GRAPH_DIR}/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="35%" style="display:inline-block;"/>\n'
        "</div>\n\n"
    )

def generate_badges_section(metrics):
    md = "### Real-Time Badges\n- Summarizes control statuses.\n<div style='text-align:center;'>\n"
    for control, _, _ in metrics:
        md += f'  <img src="{BADGE_DIR}/{control}.svg" alt="{control}" style="height:20px; margin:2px;"/>\n'
    md += "</div>\n\n"
    return md

def generate_table_section(metrics):
    md = "### 🗂 Metrics Table\n| Control | Domain | Score (%) |\n|---------|--------|-----------|\n"
    for control, domain, score in metrics:
        md += f"| {control} | {domain} | {score} |\n"
    return md + "\n"

def generate_color_codes_box():
    return (
        "## 🚦 Color Codes\n\n"
        "| Color    | Meaning |\n"
        "|----------|---------|\n"
        "| 🔴 Red   | Critical (0-59%) / Non-compliant / Missing |\n"
        "| 🟠 Orange| Warning (60-79%) / Partial / In Progress |\n"
        "| 🟢 Green | Healthy (80-100%) |\n"
        "| 🔵 Blue  | Compliant / Covered ISO |\n"
    )

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    metrics = fetch_metrics()
    new_section = (
        "## 📊 Dashboards and Badges\n\n"
        + generate_graphs_section()
        + generate_badges_section(metrics)
        + generate_table_section(metrics)
        + generate_color_codes_box()
    )

    # Replace old section
    start = next((i for i, line in enumerate(lines) if line.strip() == "## 📊 Dashboards and Badges"), None)
    if start is None:
        raise RuntimeError("Could not find '## 📊 Dashboards and Badges' in README.md")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    updated_lines = lines[:start] + [new_section] + lines[end:]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("README.md updated with latest graphs, badges, table, and color codes.")

if __name__ == "__main__":
    update_readme()
