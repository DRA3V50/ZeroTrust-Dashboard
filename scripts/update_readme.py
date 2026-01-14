import pandas as pd
from create_controls_db import db_path
import sqlite3

df = pd.read_sql("SELECT * FROM controls", sqlite3.connect(db_path))

# Generate metrics table Markdown
metrics_table = df.to_markdown(index=False)

# Generate badges Markdown
badges_md = "\n".join([f"![{row['control']}](outputs/badges/{row['control']}.svg)" for _, row in df.iterrows()])

# Update README.md
with open("README.md", "w") as f:
    f.write(f"""# 🔒 Zero Trust Dashboard

---

## 🔎 Overview
The **Zero Trust Dashboard** provides automated daily insights of Zero Trust posture and ISO 27001 compliance using Python, SQLite, and GitHub Actions.

---

## 📊 Latest Graphs

### Zero Trust Posture
![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)

### ISO 27001 Coverage
![ISO 27001 Coverage](outputs/graphs/iso_27001_coverage.png)

---

## 🏷 Badges
{badges_md}

---

## 🗂 Metrics Table
{metrics_table}

> Updated automatically by GitHub Actions workflow.
""")
