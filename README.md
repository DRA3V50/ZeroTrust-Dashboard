# 🔒 Zero Trust Dashboard

---

## 📝 Summary

The **Zero Trust Dashboard** provides a visual and automated view of your organization's **Zero Trust security posture** and **ISO 27001 compliance**. It refreshes twice daily to help analysts, leadership, and auditors quickly understand your security state.

---

## 📝 Overview

The **Zero Trust Dashboard** provides an automated, real-time view of an organization's **Zero Trust security posture** and **ISO 27001 compliance**. It leverages **Python**, **SQLite**, and **GitHub Actions** to automatically update metrics, reports, badges, and visualizations twice daily.

- Provides consistent, auditable insights for operational and federal security teams.  
- Supports ongoing monitoring without manual intervention.  
- Ideal for ISO-27001 compliance tracking, OSINT analysis, and risk management audits.  

---

## 🛡️ Targeted Features

- **Zero Trust Posture Evaluation**: Continuous assessment across five critical domains — Identity, Device, Network, Application, and Data.  
- **ISO 27001 Compliance Monitoring**: Tracks coverage of key controls, highlighting gaps and compliance levels.  
- **Automated Daily Updates**: Graphs, badges, and reports are refreshed twice daily to reflect the latest data.  
- **Data-Driven Insights**: Supports actionable decision-making through real-time metrics.  
- **Demonstration and Testing**: Graphs and badges can be generated dynamically without affecting production outputs.  

---

## 📊 Key Metrics

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

## ⚙️ How It Works

- **📄 Data Storage**: Security metrics are stored in **SQLite** (`data/controls.db`).  
- **🗂️ Report Generation**: Produces structured reports summarizing current security posture and compliance.  
- **Visualizations**:  
  - **Graphs**: Dark-background graphs representing Zero Trust and ISO 27001 coverage.  
  - **Badges**: Real-time visual summaries of individual controls.  

> **⚠️ Note**: All graphs, badges, and metrics are refreshed daily to reflect the latest data.

---

## 📊 Dashboards and Badges

### 🔹 Graphs
Updated daily to show actionable insight for analysts and leadership.
<div style="text-align:center;">
  <img src="outputs/graphs/zero_trust_posture.png" alt="Zero Trust Scores" width="45%" style="display:inline-block; margin-right:5px;"/>
  <img src="outputs/graphs/iso_27001_coverage.png" alt="ISO 27001 Coverage" width="45%" style="display:inline-block;"/>
</div>

#### Color Codes
- **Zero Trust Posture Graph** (per domain):  
  - 🔴 Critical (0–59%)  
  - 🟠 Warning (60–79%)  
  - 🟢 Healthy (80–100%)  
- **ISO 27001 Coverage Graph**:  
  - 🔴 Non-compliant / Missing  
  - 🟠 Partial / In Progress  
  - 🔵 Compliant / Covered  

---

### 🔹 Real-Time Badges
- Summarizes individual control statuses with dynamic updates.
<div style="text-align:center;">
  <img src="outputs/badges/A.5.1.svg" alt="A.5.1" style="height:20px; margin:2px;"/>
  <img src="outputs/badges/A.6.1.svg" alt="A.6.1" style="height:20px; margin:2px;"/>
  <img src="outputs/badges/A.8.2.svg" alt="A.8.2" style="height:20px; margin:2px;"/>
  <img src="outputs/badges/A.9.2.svg" alt="A.9.2" style="height:20px; margin:2px;"/>
</div>

---

### 🗂 Metrics Table
<div style="text-align:center;">
| Control | Domain | Score (%) |
|---------|--------|-----------|
| A.5.1   | InfoSec Policies | 87 |
| A.6.1   | Org InfoSec      | 92 |
| A.8.2   | Risk Management  | 79 |
| A.9.2   | Access Control   | 85 |
</div>

---

<!-- AUTO-UPDATE-START -->
<!--
The workflow script will completely replace this section with the latest:
1. Graphs (Zero Trust + ISO 27001)
2. Badges for each control
3. Metrics Table
Do NOT manually edit inside this block.
-->
<!-- AUTO-UPDATE-END -->
