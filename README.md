# 🔒 Zero Trust Dashboard

---

## 🔎 Overview
The **Zero Trust Dashboard** provides an automated, real-time view of an organization's **Zero Trust security posture** and **ISO 27001 compliance**. By leveraging **Python**, **SQLite**, and **GitHub Actions**, this system ensures metrics, reports, badges, and visualizations are updated twice daily, supporting informed security decision-making.

- Provides consistent, auditable insights for operational and federal security teams.  
- Supports ongoing monitoring without manual intervention.  
- Ideal for ISO-27001 compliance tracking, OSINT analysis, and risk management audits.  

---

## 🛡️ Targeted Features
- **Zero Trust Posture Evaluation**: Continuous assessment across five critical domains—Identity, Device, Network, Application, and Data.  
- **ISO 27001 Compliance Monitoring**: Tracks coverage of critical controls, highlighting gaps and compliance levels.  
- **Automated Daily Updates**: Graphs, badges, and reports are refreshed twice daily to reflect the latest data.  
- **Data-Driven Insights**: Supports actionable decision-making through real-time metrics.  
- **Demonstration and Testing**: Graphs and badges are generated with dynamic or randomized data for testing, without affecting production outputs.  

---

## 🔑 Key Metrics

### Zero Trust Domains
- **Identity**: Ensures secure access and user verification.  
- **Device**: Monitors the security and health of all devices.  
- **Network**: Protects against unauthorized access and ensures segmentation.  
- **Application**: Evaluates security vulnerabilities and patch compliance.  
- **Data**: Safeguards data integrity, encryption, and controlled access.  

### ISO 27001 Controls
- **A.5.1** – Information Security Policies  
- **A.6.1** – Organization of Information Security  
- **A.8.2** – Risk Management  
- **A.9.2** – Access Control  

---

## 🧮 How It Works
- **Data Storage**: Security metrics stored in a structured **SQLite database** (`data/controls.db`).  
- **Report Generation**: Produces structured reports summarizing current security posture and compliance.  
- **Visualizations**:  
  - **Graphs**: Dynamic visual representation of Zero Trust and ISO-27001 coverage. Updated daily, showing the latest results without overwriting previous data.  
  - **Badges**: Real-time visual summaries of individual controls.  

> **⚠️ Note**: Graphs and badges are updated twice daily to reflect the latest data.

Graphs use a professional dark theme and are sized for readability (~295px wide) on dashboards and reports.

---

## 📝 Security Monitoring and Audit Support
The dashboard supports operational monitoring, compliance tracking, and audit readiness:  

- **Track Compliance**: Monitor controls across domains and ISO 27001 standards.  
- **Identify Gaps**: Highlight areas of insufficient security or non-compliance.  
- **Audit Preparation**: Generate reports suitable for internal and external audits.  

> **Professional Insight:** Dashboards can be customized to focus on specific controls, thresholds, or domains aligned with organizational priorities or OSINT investigations.  

---

## 📊 Dashboards and Badges

### Latest Zero Trust Posture
- Visual representation of domain scores updated daily.  
- Provides actionable insight for analysts and leadership.  
![Zero Trust Posture](assets/graphs/zero_trust_posture.png)

### Latest ISO 27001 Control Coverage
- Daily updated visual representation of control compliance.  
- Highlights strengths and areas needing attention.  
![ISO 27001 Control Coverage](assets/graphs/iso_27001_coverage.png)

### Real-Time Badges
- Summarizes individual control statuses with dynamic updates.  
![A.5.1](assets/badges/A.5.1.svg)  
![A.6.1](assets/badges/A.6.1.svg)  
![A.8.2](assets/badges/A.8.2.svg)  
![A.9.2](assets/badges/A.9.2.svg)

### 🗂 Metrics Table
| Control ID | Domain | Score (%) |
|-----------|--------|-----------|
| A.5.1 | Policy | 85 |
| A.6.1 | Access Control | 75 |
| A.8.2 | Assets | 90 |
| A.9.2 | Monitoring | 60 |

> **Note:** This table is automatically updated daily by the workflow, reflecting the latest Zero Trust and ISO 27001 control scores.

---

## 📜 License
This project is released under the **MIT License**.

