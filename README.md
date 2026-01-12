# ZeroTrust-Dashboard 🔐📊  
**Automated Enterprise Security Posture & ISO 27001 Metrics**

---

## 🔐 Summary
ZeroTrust-Dashboard provides a **real-time, continuously updated view of enterprise security**. It tracks **Zero Trust domain maturity** and **ISO 27001 control coverage**, giving analysts and leadership **actionable insights at a glance**.  

**Built for security analysts, auditors, and leadership dashboards.**  

---

## 🗂️ Key Features
- **Live Zero Trust Posture & ISO 27001 Controls**: Identity, Device, Network, Application, Data, plus policy & compliance coverage, all in one visual view.  
- **Automated Daily Updates**: Python scripts + SQLite + GitHub Actions keep your badges and reports current without overwriting history.  
- **Persistent Data**: Metrics stored in `data/controls.db` allow longitudinal analysis.  
- **Quick Insight for Analysts**: Identify gaps, track trends, and support audits efficiently.

---

## 📊 Live Enterprise Dashboard
### Combined Security & Compliance View
| Domain / Control | Badge |
|-----------------|-------|
| Identity | ![Identity](assets/badges/Identity.svg) |
| Device | ![Device](assets/badges/Device.svg) |
| Network | ![Network](assets/badges/Network.svg) |
| Application | ![Application](assets/badges/Application.svg) |
| Data | ![Data](assets/badges/Data.svg) |
| A.5.1 – Info Security Policies | ![A.5.1](assets/badges/A_5_1.svg) |
| A.6.1 – Org of Info Security | ![A.6.1](assets/badges/A_6_1.svg) |
| A.7.2 – Employee Awareness | ![A.7.2](assets/badges/A_7_2.svg) |
| A.9.2 – Access Control | ![A.9.2](assets/badges/A_9_2.svg) |

> Badges **update daily automatically** while your README and history remain intact.

---

## 📌 How It Works
1. **Metrics Collection** – `scripts/update_dashboard.py` aggregates domain coverage & ISO control status.  
2. **Badge Generation** – `scripts/generate_badges.py` produces visual SVG badges for dashboards and reports.  
3. **Database Persistence** – `scripts/create_controls_db.py` maintains `controls.db` for historical trends.  
4. **Automation Pipeline** – `.github/workflows/daily_update.yml` runs daily to update metrics, badges, and reports.

---

## 📈 Analyst Use Cases
- Quickly identify **high-risk domains or missing controls**  
- Track **Zero Trust maturity over time**  
- Provide leadership **visual dashboards for compliance and posture**  
- Prepare for **audits and evidence-based reviews**  
- Train analysts using **continuous, realistic security data**

---

## 📁 Reports & Assets
- **Latest Report:** [`reports/latest_report.md`](reports/latest_report.md)  
- **Badges Directory:** [`assets/badges`](assets/badges)  
- **Database:** [`data/controls.db`](data/controls.db)

---

ZeroTrust-Dashboard **bridges security operations, compliance tracking, and automated visualization** — just like tools used by federal and corporate security teams for continuous monitoring and leadership reporting.
