# ZeroTrust-Dashboard
Dynamic dashboard assessing enterprise Zero Trust posture and ISO 27001 compliance metrics using Python and SQL.

---
# ZeroTrust-Dashboard

Dynamic enterprise dashboard assessing Zero Trust posture and ISO 27001 compliance using Python and SQL.

## Overview
This repository demonstrates daily-updated assessment of enterprise security, covering:

- **Zero Trust domains**: Identity, Device, Network, Application, Data  
- **ISO 27001 controls**: Policy, Organization, Risk, etc.  

Designed to showcase skills in **data analysis, automation, and security monitoring**.

## Skills Demonstrated
- Python scripting and SQLite database management  
- Data aggregation and reporting  
- Enterprise security frameworks: Zero Trust, ISO 27001  
- GitHub Actions for automated, daily updates  

## Latest Report
![Latest Report](reports/latest_report.md)

## How It Works
1. Metrics stored in `data/controls.db` (SQLite)  
2. `scripts/update_dashboard.py` fetches metrics and generates `reports/latest_report.md`  
3. GitHub Action runs daily, updating the dashboard automatically
