from pathlib import Path
import svgwrite
import sqlite3

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "controls.db"
BADGES_DIR = ROOT / "assets/badges"
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, path):
    # Determine color
    color = "#4c1" if isinstance(value,int) and value >= 80 else "#dfb317" if value >= 50 else "#e05d44"
    dwg = svgwrite.Drawing(str(path), size=("120px", "20px"))
    dwg.add(dwg.rect(insert=(0, 0), size=("120px", "20px"), fill=color))
    dwg.add(dwg.text(f"{label}: {value}", insert=(5, 15), fill="white", font_size="12px"))
    dwg.save()

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Zero Trust badges
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    for domain, coverage in cursor.fetchall():
        safe_label = domain.replace(" ", "_").replace("/", "_")
        create_badge(domain, int(coverage), BADGES_DIR / f"{safe_label}.svg")

    # ISO 27001 badges
    cursor.execute("SELECT control, status FROM iso27001")
    for control, status in cursor.fetchall():
        safe_label = control.replace(" ", "_").replace("/", "_")
        create_badge(control, status, BADGES_DIR / f"{safe_label}.svg")

    conn.close()
    print(f"Badges generated successfully at {BADGES_DIR}")

if __name__ == "__main__":
    generate_badges()
