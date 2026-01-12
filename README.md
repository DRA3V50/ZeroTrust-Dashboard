# ZeroTrust-Dashboard 🔐📊  
**Automated Enterprise Zero Trust & ISO 27001 Posture Analytics**

---

## Executive Summary
**ZeroTrust-Dashboard** is a continuously updated security posture dashboard that models how large organizations track **Zero Trust maturity** and **ISO 27001 control coverage** over time.

This repository mirrors **real-world compliance monitoring and security governance workflows** used across federal, intelligence, and regulated enterprise environments.

- Live posture indicators (badges)  
- Persistent historical data (SQLite)  
- Fully automated reporting pipeline  
- Designed for analyst, auditor, and leadership visibility  

---

## Mission Relevance
This repository demonstrates skills directly aligned with:
- Security data analysis  
- Continuous monitoring & compliance  
- Zero Trust architecture visibility  
- Automated reporting for decision-makers  

It reflects how security teams **measure, report, and communicate risk**.

---

## Architecture Overview

### Data Layer
- **SQLite Database:**  
  [`data/controls.db`](data/controls.db)  
  Stores Zero Trust domain coverage and ISO 27001 control status (persistent across runs)

### Analytics & Automation
- **Database Initialization / Maintenance:**  
  [`scripts/create_controls_db.py`](scripts/create_controls_db.py)

- **Posture Aggregation & Reporting:**  
  [`scripts/update_dashboard.py`](scripts/update_dashboard.py)

- **Visual Indicator Generation (SVG Badges):**  
  [`scripts/generate_badges.py`](scripts/generate_badges.py)

### Automation Engine
- **GitHub Actions Workflow:**  
  [`.github/workflows/daily_update.yml`](.github/workflows/daily_update.yml)

Runs automatically:
- Updates metrics
- Regenerates badges
- Commits results automatically
- Preserves historical continuity

---

## Live Zero Trust Posture

| Domain | Status |
|--------|--------|
| Identity | ![Identity](assets/badges/Identity.svg) |
| Device | ![Device](assets/badges/Device.svg) |
| Network | ![Network](assets/badges/Network.svg) |
| Application | ![Application](assets/badges/Application.svg) |
| Data | ![Data](assets/badges/Data.svg) |

These indicators reflect **current enterprise coverage levels**, similar to executive dashboards used in governance reviews.

---

## ISO 27001 Control Coverage

| Control | Indicator |
|--------|--------|
| A.5.1 – Information Security Policies | ![A.5.1](assets/badges/A_5_1.svg) |
| A.6.1 – Organization of Information Security | ![A.6.1](assets/badges/A_6_1.svg) |
| A.7.2 – Employee Awareness | ![A.7.2](assets/badges/A_7_2.svg) |
| A.9.2 – Access Control | ![A.9.2](assets/badges/A_9_2.svg) |

---

## Analyst & Leadership Use Cases
- Track Zero Trust maturity across domains  
- Monitor ISO control alignment over time  
- Support audit readiness & compliance reviews  
- Provide leadership with **clear, visual posture indicators**  
- Demonstrate continuous monitoring practices  

---

## Latest Automated Report
- **Current posture snapshot:**  
  [`reports/latest_report.md`](reports/latest_report.md)

This report is regenerated automatically and reflects the same data powering the live badges.

---

## Skills Demonstrated
- Python automation & data processing  
- SQLite schema design & persistence  
- Security framework alignment (Zero Trust, ISO 27001)  
- CI/CD automation using GitHub Actions  
- Operational reporting & visualization  

---

## Why This Matters
ZeroTrust-Dashboard is not a demo or a one-off script.  

It represents how **real security programs measure progress, maintain evidence, and communicate posture** — exactly the skills expected in **federal data analyst, cyber, and intelligence-support roles**.
