# 🗂️ ZeroTrust-Dashboard

Dynamic enterprise dashboard monitoring **Zero Trust posture** and **ISO 27001 control coverage** in real time.  
Designed for cybersecurity analysts, SOC teams, and governance reviewers to provide **actionable insights** while preserving historical data.

---

## 🔐 Objective
Centralize security metrics to help analysts and leadership:

- Evaluate enterprise security posture across **Identity, Device, Network, Application, and Data domains**  
- Monitor compliance with ISO 27001 controls  
- Automate reporting and badge generation for visual insights  

---

## 📊 Zero Trust Posture
Visualizes coverage across Zero Trust domains with **daily-updated badges**:  

**Domains:**  
Identity | Device | Network | Application | Data  

<!-- Auto-updating badges -->
![Identity Badge](assets/badges/Identity.svg) ![Device Badge](assets/badges/Device.svg) ![Network Badge](assets/badges/Network.svg) ![Application Badge](assets/badges/Application.svg) ![Data Badge](assets/badges/Data.svg)

---

## 📁 ISO 27001 Control Coverage
Track compliance dynamically for ISO 27001 controls:  

**Controls:**  
A.5.1 Information Security Policies | A.6.1 Organization of Information Security | A.7.2 Employee Awareness | A.9.2 Access Control  

<!-- Auto-updating badges -->
![A.5.1](assets/badges/A_5_1.svg) ![A.6.1](assets/badges/A_6_1.svg) ![A.7.2](assets/badges/A_7_2.svg) ![A.9.2](assets/badges/A_9_2.svg)

---

## ⚙️ Methodology
1. **Data Storage:** Metrics stored in `data/controls.db` (SQLite)  
2. **Dashboard Update:** `scripts/update_dashboard.py` generates `reports/latest_report.md`  
3. **Badge Generation:** `scripts/generate_badges.py` creates SVG badges for domains & ISO controls  
4. **Automation:** GitHub Actions updates daily while preserving historical data  

---

## 📈 Analyst Insights
- Identify gaps in Zero Trust coverage or ISO 27001 compliance  
- Track trends over time for informed decision-making  
- Use badges for executive dashboards, audits, and reporting  

---

## 🗃️ Repository Structure
