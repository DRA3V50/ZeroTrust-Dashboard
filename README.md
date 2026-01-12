# 🔒 Zero Trust Dashboard

---

## 📂 Overview
The **Zero Trust Dashboard** provides real-time assessments of an organization's **Zero Trust posture** and **ISO 27001 compliance**. This project integrates **Python**, **SQLite**, and **GitHub Actions** to automate the generation of security metrics and reports. The dashboard displays live security trends, control coverage, and other key data to help enterprises stay secure and compliant.

## 🛡️ Key Features
- **Zero Trust Posture Evaluation**: Regular assessment across **5 key security domains**: Identity, Device, Network, Application, and Data.
- **ISO 27001 Compliance Coverage**: Tracks real-time adherence to ISO 27001 security controls.
- **Automated Daily Reports**: Dashboards and badges are automatically updated twice a day through **GitHub Actions**.
- **Data-Driven Insights**: Live data sourced from **SQLite** and processed by **Python** scripts ensures up-to-date insights.

## 🔑 Key Metrics
- **Zero Trust Domains**:  
  - **Identity**: Secure access, identity verification, and authentication.
  - **Device**: Device health, endpoint management, and monitoring.
  - **Network**: Secure network architecture and segmentation.
  - **Application**: Application security, patch management, and vulnerabilities.
  - **Data**: Data integrity, encryption, and secure access management.

- ** 🗂️ ISO 27001 Controls**:  
  - **A.5.1** - Information Security Policies  
  - **A.6.1** - Organization of Information Security  
  - **A.8.2** - Risk Management  
  - **A.9.2** - Access Control  

## 🌐 How It Works
- **Metrics** are stored in the **SQLite database** (`data/controls.db`) and updated by automated scripts.
- **Dashboard Reports** are automatically generated and saved in `latest_report.md` for quick access.
- **Badges** and **graphs** are generated and stored in `assets/badges/` and `assets/graphs/` folders respectively.
> *⚠️ Graphs update automatically daily*

## 📊 Live Dashboards & Badges
### Latest Zero Trust Posture
![Zero Trust Posture](assets/graphs/zero_trust_posture.png)

### Latest ISO 27001 Control Coverage
![ISO 27001 Control Coverage](assets/graphs/iso_27001_coverage.png)

### Real-time Badges
![A.5.1 - Information Security Policies](assets/badges/A_5_1.svg)  
![A.6.1 - Organization of Information Security](assets/badges/A_6_1.svg)  
![A.7.2 - Employee Awareness](assets/badges/A_7_2.svg)  
![A.9.2 - Access Control](assets/badges/A_9_2.svg)

## ⚙️ Automation & Setup
### Requirements
- Python 3.11+
- Install dependencies with `pip install -r requirements.txt`

### GitHub Actions Workflow
- **Twice-Daily Automation**: The dashboard, badges, and graphs are automatically updated at **8:00 AM and 8:00 PM EST** via GitHub Actions.

### 📄 Key Files
- **`scripts/`**: Python scripts that generate dashboards, badges, and graphs.
  - `create_controls_db.py`: Creates or updates the SQLite database (`data/controls.db`).
  - `update_dashboard.py`: Updates the dashboard report and writes to `latest_report.md`.
  - `generate_badges.py`: Generates SVG badges for Zero Trust and ISO 27001 domains.
  - `generate_graphs.py`: Generates live graphs for Zero Trust and ISO 27001 metrics.
- **`assets/badges/`**: Folder containing generated SVG badges for security domains and controls.
- **`assets/graphs/`**: Folder containing graphs that track Zero Trust posture and ISO 27001 coverage.
- **`data/controls.db`**: SQLite database for tracking Zero Trust and ISO 27001 compliance metrics.

## 📝 How To Contribute
- Fork the repository and create a new branch for your changes.
- Open a pull request with a detailed description of your improvements.
- Ensure the code follows best practices and is tested for functionality.

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
