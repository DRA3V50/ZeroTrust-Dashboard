# ZeroTrust-Dashboard 🔐

Dynamic **enterprise Zero Trust posture** and **ISO 27001 control coverage** dashboard with live daily updates.

---

## 📊 Zero Trust Posture
Live visual assessment across all enterprise domains:

- Identity 🗂️  
- Device 🔒  
- Network 🌐  
- Application 🖥️  
- Data 📁  

Graphs update daily with the latest metrics.

![Zero Trust Posture](assets/graphs/zero_trust_posture.png)

---

## 📝 ISO 27001 Control Coverage
Track your ISO 27001 compliance progress with coverage percentages for each control:

- A.5.1 Information Security Policies 📄  
- A.6.1 Organization of Information Security 🏢  
- A.7.2 Employee Awareness 👥  
- A.9.2 Access Control 🔑  

![ISO 27001 Coverage](assets/graphs/iso27001_coverage.png)

---

## 🛠️ How It Works
1. **Data Collection** – Metrics stored in `data/controls.db`.  
2. **Report Generation** – `scripts/update_dashboard.py` updates `reports/latest_report.md`.  
3. **Badges & Graphs** – `scripts/generate_badges.py` & `scripts/generate_graphs.py` produce visuals for live display.  
4. **Automation** – GitHub Actions updates everything daily, preserving README layout and visuals.

---

## 📂 Files & Assets
- `assets/badges/` – Daily badges for Zero Trust domains and ISO controls  
- `assets/graphs/` – Daily bar charts for posture and compliance  
- `data/controls.db` – SQLite database of metrics  
- `reports/latest_report.md` – Latest numeric report  

---

## 👨‍💻 Focus & Skills Demonstrated
- Enterprise security metrics: Zero Trust, ISO 27001  
- Python automation & SQLite database management  
- Data visualization with **Matplotlib** & **SVG badges**  
- Daily CI/CD automation with **GitHub Actions**

---

## ⚡ Usage
Clone the repository and run scripts manually or rely on automated daily updates via GitHub Actions:

```bash
python scripts/create_controls_db.py
python scripts/update_dashboard.py
python scripts/generate_badges.py
python scripts/generate_graphs.py
