# 🔒 Zero Trust Dashboard

---

## 🔎 Overview
The **Zero Trust Dashboard** provides an automated, real-time view of an organization's **Zero Trust security posture** and **ISO 27001 compliance**. Graphs, badges, and metrics are updated twice daily by GitHub Actions.

---

## 📊 Latest Visualizations

### Zero Trust Posture
Updated daily — dark-themed for better readability.  
![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)

### ISO 27001 Control Coverage
Updated daily — dark-themed graph.  
![ISO 27001 Control Coverage](outputs/graphs/iso_27001_coverage.png)

### Real-Time Badges
Individual control status badges — updated daily.  
![A.5.1](outputs/badges/A.5.1.svg)  
![A.6.1](outputs/badges/A.6.1.svg)  
![A.8.2](outputs/badges/A.8.2.svg)  
![A.9.2](outputs/badges/A.9.2.svg)

### Metrics Table
Automatically updated daily.  
| Control | Domain | Score (%) |
|---------|--------|-----------|
| A.5.1   | InfoSec Policies | 87 |
| A.6.1   | Org InfoSec      | 92 |
| A.8.2   | Risk Management  | 79 |
| A.9.2   | Access Control   | 85 |

> ⚠️ **Note:** All graphs, badges, and metrics are refreshed by the workflow and reflect the latest Zero Trust and ISO 27001 data.

---

## 🧮 How It Works
1. Security metrics stored in **SQLite** (`data/controls.db`).  
2. **Python scripts** generate updated graphs, badges, and reports.  
3. GitHub Actions workflow runs twice daily to commit and update all outputs.  

---

## 📜 License
MIT

## 📜 License
