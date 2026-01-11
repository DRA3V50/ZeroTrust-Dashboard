import sqlite3
from pathlib import Path
import svgwrite

DB_PATH = Path("data/controls.db")
BADGES_DIR = Path("assets/badges")
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, path):
    # Ensure value is int
    try:
        value_int = int(value)
    except:
        value_int = 0

    color = "#4c1" if value_int >= 80 else "#dfb317" if value_int >= 50 else "#e05d44"

    dwg = svgwrite.Drawing(str(path), size=(150, 20))
    dwg.add(dwg.rect(insert=(0, 0), size=("150px", "20px"), fill="#555"))
    dwg.add(dwg.rect(insert=(70, 0), size=("80px", "20px"), fill=color))
    dwg.add(dwg.text(label, insert=(5, 14), fill="#fff", font_size="11px", font_family="Verdana"))
    dwg.add(dwg.text(f"{value_int}%", insert=(75, 14), fill="#fff", font_size="11px", font_family="Verdana"))
    dwg.save()

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT domain, coverage FROM zero_trust")
    for domain, coverage in cursor.fetchall():
        safe_label = domain.replace(" ", "_").replace("/", "_")
        create_badge(domain, coverage, BADGES_DIR / f"{safe_label}.svg")

    cursor.execute("SELECT control, coverage FROM iso_controls")
    for control, coverage in cursor.fetchall():
        safe_label = control.replace(" ", "_").replace("/", "_")
        create_badge(control, coverage, BADGES_DIR / f"{safe_label}.svg")

    conn.close()
    print("All badges generated successfully ✅")

if __name__ == "__main__":
    generate_badges()
