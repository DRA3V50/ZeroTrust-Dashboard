# 🔒 Zero Trust Dashboard

---

## 🔎 Overview
The **Zero Trust Dashboard** provides an automated, real-time view of an organization's **Zero Trust security posture** and **ISO 27001 compliance**. By leveraging **Python**, **SQLite**, and **GitHub Actions**, this system ensures metrics, reports, badges, and visualizations are updated twice daily, supporting informed security decision-making.

- Provides consistent, auditable insights for operational and federal security teams.  
- Supports ongoing monitoring without manual intervention.  
- Ideal for ISO-27001 compliance tracking, OSINT analysis, and risk management audits.  

---

## 🛡️ Targeted Features
- **Zero Trust Posture Evaluation**: Continuous assessment across five critical domains — Identity, Device, Network, Application, and Data.  
- **ISO 27001 Compliance Monitoring**: Tracks coverage of key controls, highlighting gaps and compliance levels.  
- **Automated Daily Updates**: Graphs, badges, and reports are refreshed twice daily to reflect the latest data.  
- **Data-Driven Insights**: Supports actionable decision-making through real-time metrics.  
- **Demonstration and Testing**: Graphs and badges can be generated with dynamic or randomized data for testing without affecting production outputs.  

---

## 🔑 Key Metrics

### Zero Trust Domains
- **Identity**: Ensures secure access and user verification.  
- **Device**: Monitors security and health of endpoints.  
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
- **Data Storage**: Security metrics are stored in a structured **SQLite database** (`data/controls.db`).  
- **Report Generation**: Produces structured reports summarizing current security posture and compliance.  
- **Visualizations**:  
  - **Graphs**: Dynamic visual representations of Zero Trust and ISO 27001 coverage. Graphs are dark-themed, updated twice daily, and saved as **latest files**.  
  - **Badges**: Real-time visual summaries of individual controls, always showing the **most recent values**.  

> **⚠️ Note**: Graphs, badges, and metrics tables are automatically updated twice daily by the workflow.

---

## 📊 Dashboards and Badges 📇

### Latest Zero Trust Posture
- Updated automatically.
![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)

### Latest ISO 27001 Control Coverage
- Updated automatically.
![ISO 27001 Control Coverage](outputs/graphs/iso_27001_coverage.png)

### Real-Time Badges
- Summarizes individual control statuses with dynamic updates.
![A.5.1](outputs/badges/A.5.1.svg)  
![A.6.1](outputs/badges/A.6.1.svg)  
![A.8.2](outputs/badges/A.8.2.svg)  
![A.9.2](outputs/badges/A.9.2.svg)

### 🗂 Metrics Table
| Control | Domain | Score (%) |
|---------|--------|-----------|
| A.5.1   | InfoSec Policies | (auto-updated) |
| A.6.1   | Org InfoSec      | (auto-updated) |
| A.8.2   | Risk Management  | (auto-updated) |
| A.9.2   | Access Control   | (auto-updated) |

> **Note**: This table is automatically refreshed by the workflow, always showing the **latest scores**.

---

## 📜 License
