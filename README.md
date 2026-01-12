# ZeroTrust-Dashboard 🔒

**Live Zero Trust Posture & ISO 27001 Control Coverage Dashboard**

---

### 🔹 Overview
ZeroTrust-Dashboard continuously tracks enterprise security posture and ISO 27001 compliance in real-time.  
This repository showcases your ability to monitor, report, and visualize key security metrics across multiple domains, helping organizations maintain robust security practices.

- **Zero Trust Domains:** Identity, Device, Network, Application, Data  
- **ISO 27001 Controls:** Policies, Organization, Access, Risk Management, and more  

---

### 📊 Live Metrics

**Zero Trust Posture**  
![Identity](assets/badges/Identity.svg) ![Device](assets/badges/Device.svg) ![Network](assets/badges/Network.svg) ![Application](assets/badges/Application.svg) ![Data](assets/badges/Data.svg)

**ISO 27001 Control Coverage**  
![A.5.1](assets/badges/A_5_1.svg) ![A.6.1](assets/badges/A_6_1.svg) ![A.7.2](assets/badges/A_7_2.svg) ![A.9.2](assets/badges/A_9_2.svg)

---

### 🛠 How It Works
1. **Data Collection:** Metrics stored in `data/controls.db` (SQLite).  
2. **Reporting:** `scripts/update_dashboard.py` generates `reports/latest_report.md`.  
3. **Visuals:** `scripts/generate_badges.py` updates live SVG badges.  
4. **Automation:** GitHub Actions runs twice daily (morning & night EST) to update reports and badges automatically.  

---

### 📈 Analyst Insights
- Quickly identify coverage gaps across Zero Trust domains and ISO 27001 controls  
- Visualize trends for informed security decisions  
- Keep a historical record of enterprise posture metrics  

---

### 🗂️ Features
- Fully automated dashboard updates  
- Persistent SQLite database ensures data history  
- Professional, enterprise-grade visualization of controls & posture  
- Easy to extend with additional metrics or controls  

---

### 📝 Latest Report
Check out the latest assessment: [`reports/latest_report.md`](reports/latest_report.md)  

---

### 🔗 Repository Links
- [Scripts folder](scripts) – Python scripts for automation  
- [Badges folder](assets/badges) – Live SVG badges  
- [Data folder](data) – SQLite database storing metrics  

---

**ZeroTrust-Dashboard** combines automation, real-time analytics, and professional reporting to help organizations monitor their security posture efficiently.
