# 🔒 Zero Trust Dashboard

---

## 📂 Overview
The **Zero Trust Dashboard** provides **real-time assessments** of an organization's **Zero Trust posture** and **ISO 27001 compliance**. Leveraging **Python**, **SQLite**, and **GitHub Actions**, this solution automates the generation of **security metrics**, **graphs**, and **reports**, allowing enterprises to stay secure and compliant with minimal manual intervention.

---

## 🛡️ Key Features
- **Zero Trust Posture Evaluation**: Regular assessments across **5 key security domains**:  
  - **Identity**
  - **Device**
  - **Network**
  - **Application**
  - **Data**

- **ISO 27001 Compliance Coverage**: Tracks and reports on real-time adherence to **ISO 27001 security controls**.

- **Automated Daily Updates**: Dashboards, badges, and graphs are updated twice daily via **GitHub Actions** at **8:00 AM and 8:00 PM EST**.

- **Data-Driven Insights**: Live data, processed via **Python** scripts, ensures up-to-date security insights sourced from the **SQLite database**.

---

## 🔑 Key Metrics
- **Zero Trust Domains**:
  - **Identity**: Access control, identity verification, and authentication.
  - **Device**: Device health, endpoint management, and monitoring.
  - **Network**: Secure network architecture, segmentation, and encryption.
  - **Application**: Application security, patch management, and vulnerability mitigation.
  - **Data**: Data integrity, encryption, and secure access management.

- **ISO 27001 Controls**:
  - **A.5.1** - Information Security Policies
  - **A.6.1** - Organization of Information Security
  - **A.8.2** - Risk Management
  - **A.9.2** - Access Control

---

## 🌐 How It Works
1. **Metrics Storage**: Security metrics are stored in the **SQLite database** (`data/controls.db`).
2. **Report Generation**: Dashboards and reports are automatically generated and saved to `latest_report.md`.
3. **Badges and Graphs**:  
   - **Badges** are generated in **SVG** format and stored in `assets/badges/`.
   - **Graphs** are stored as PNGs in `assets/graphs/`.
   
> **⚠️ Note**: Graphs are automatically updated twice a day.

---

## 🕵️‍♂️ Security Audit
The **Zero Trust Dashboard** can be used for regular **security audits** to assess an organization's adherence to security best practices and **ISO 27001** standards. You can use the dashboard to:
- **Track Compliance**: Monitor progress on security controls over time.
- **Identify Gaps**: Visualize and address areas of concern across key domains.
- **Prepare for Audits**: Easily generate reports for security audits and internal reviews.
  
> **Tip**: Customize your dashboard and reports based on specific needs for a more tailored audit experience.

---

## 🔄 Integration with Existing Security Tools
The **Zero Trust Dashboard** is designed to be **flexible** and **integrate** with existing security frameworks, such as:
- **SIEM Systems** (e.g., Splunk, ELK Stack)
- **Identity Providers** (e.g., Okta, Azure AD)
- **Endpoint Management Tools** (e.g., Intune, Jamf)
- **Vulnerability Management Tools** (e.g., Qualys, Nessus)

This allows you to:
- Import **existing security data** directly into the dashboard.
- **Automate updates** from other integrated systems.
- **Combine insights** from various tools to create a unified security report.

> **Example**: Integrating with your SIEM system can automatically pull in logs related to **Identity** and **Device** controls.

---

## 🧩 Customizable Dashboards
If your organization has specific needs or metrics, the **Zero Trust Dashboard** allows easy customization. You can:
- Add or remove specific **Zero Trust domains** based on your requirements.
- Configure **custom alerts** based on thresholds for control compliance.
- Design and integrate **personalized visualizations**.

This feature ensures that the dashboard is always aligned with your organization’s evolving security priorities.

---

## 🚀 Scalability
The **Zero Trust Dashboard** is built to scale with your organization’s growth:
- **Handle large datasets**: The system supports growing compliance data over time.
- **Multiple users**: Add different stakeholders with **view-only** or **admin** permissions.
- **Automate routine checks**: Set up **automated notifications** for anomalies or compliance failures.

---

## 📊 Live Dashboards & Badges
- **Latest Zero Trust Posture**  
  ![Zero Trust Posture](assets/graphs/zero_trust_posture.png)

- **Latest ISO 27001 Control Coverage**  
  ![ISO 27001 Control Coverage](assets/graphs/iso_27001_coverage.png)

- **Real-time Badges**:
  ![A.5.1 - Information Security Policies](assets/badges/A_5_1.svg)  
  ![A.6.1 - Organization of Information Security](assets/badges/A_6_1.svg)  
  ![A.7.2 - Employee Awareness](assets/badges/A_7_2.svg)  
  ![A.9.2 - Access Control](assets/badges/A_9_2.svg)

---

## 📄 Key Files
- **`scripts/`**: Python scripts for dashboard, badges, and graph generation.
  - `create_controls_db.py`: Creates/updates the SQLite database (`data/controls.db`).
  - `update_dashboard.py`: Updates the dashboard report and writes to `latest_report.md`.
  - `generate_badges.py`: Generates SVG badges for Zero Trust and ISO 27001 domains.
  - `generate_graphs.py`: Generates live graphs for Zero Trust and ISO 27001 metrics.
  - **`assets/`**:  
  - **`badges/`**: SVG badges for security domains and controls.  
  - **`graphs/`**: Graphs displaying Zero Trust posture and ISO 27001 control coverage.

- **`data/controls.db`**: SQLite database for tracking security metrics and compliance data.

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for more information.

