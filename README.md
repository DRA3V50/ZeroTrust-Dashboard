# ZeroTrust-Dashboard 🛡️

**Dynamic enterprise security dashboard tracking Zero Trust posture and ISO 27001 control coverage in real-time.**  
This dashboard consolidates security metrics, generates badges, and displays live graphs for enterprise-ready visibility.

---

## 🔐 Zero Trust Posture & ISO 27001 Coverage
**Visual Summary:** Live metrics for Identity, Device, Network, Application, Data domains & ISO 27001 controls A.5–A.18.  
**Goal:** Give security teams and executives immediate insight into compliance and risk posture.

---

## 📊 Live Metrics & Visuals
**Zero Trust Domains:**  
![Identity](assets/badges/Identity.svg)  
![Device](assets/badges/Device.svg)  
![Network](assets/badges/Network.svg)  
![Application](assets/badges/Application.svg)  
![Data](assets/badges/Data.svg)

**ISO 27001 Control Coverage:**  
![A5.1 Information Security Policies](assets/badges/A_5_1.svg)  
![A6.1 Organization of Information Security](assets/badges/A_6_1.svg)  
![A7.2 Employee Awareness](assets/badges/A_7_2.svg)  
![A9.2 Access Control](assets/badges/A_9_2.svg)  

**Enterprise Security Graphs (Live Charts):**  
![Zero Trust Bar Chart](assets/graphs/zero_trust_posture.png)  
![ISO 27001 Control Coverage Chart](assets/graphs/iso27001_coverage.png)  

> ⚠️ Graphs update automatically daily via GitHub Actions; badges refresh in real-time while this text remains static.

---

## 🗂️ Data Sources
- Metrics stored in `data/controls.db` (SQLite)  
- Daily updates generated from Python scripts: `update_dashboard.py`, `generate_badges.py`, `generate_graphs.py`  

---

## ⚙️ Automation
- Fully automated via GitHub Actions workflow  
- Pulls metrics, updates graphs and badges, pushes changes without overwriting static content  
- Uses `PAT_SIM_TOKEN` for authenticated repository updates  

---

## 🔍 Analyst Insights
- Quickly identify high-risk domains and ISO 27001 gaps  
- Track changes over time via badges and bar/column charts  
- Perfect for executives, analysts, and compliance teams needing fast, visual security metrics

---

**License:** MIT  
**Repository:** [ZeroTrust-Dashboard](https://github.com/DRA3V50/ZeroTrust-Dashboard)
