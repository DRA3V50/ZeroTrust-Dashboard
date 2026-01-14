from pathlib import Path

README_FILE = Path("README.md")

def update_readme():
    # Construct updated README with badges and graphs
    content = f"""
# 🔒 Zero Trust Dashboard

## 📊 Latest Visuals

### Zero Trust Posture
![Zero Trust Posture](outputs/graphs/zero_trust_posture.png)

### ISO 27001 Control Coverage
![ISO 27001 Control Coverage](outputs/graphs/iso_27001_coverage.png)

### Real-Time Badges
![A.5.1](outputs/badges/A.5.1.svg)
![A.6.1](outputs/badges/A.6.1.svg)
![A.8.2](outputs/badges/A.8.2.svg)
![A.9.2](outputs/badges/A.9.2.svg)
"""

    README_FILE.write_text(content)
    print("README updated with latest graphs and badges.")

if __name__ == "__main__":
    update_readme()
