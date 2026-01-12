import sqlite3
from pathlib import Path
import svgwrite

DB_PATH = Path("data/controls.db")
BADGES_DIR = Path("assets/badges")
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, filename):
    # Ensure value is int
    try:
        value_int = int(value)
    except ValueError:
        value_int = 0

    # Set color based on coverage
    if value_int >= 80:
        color = "#4c1"
    elif value_int >= 50:
        color = "#dfb317"
    else:
        color = "#e05d44"

    dwg = svgwrite.Drawing(filename, size=("150px", "20px"))
    dwg.add(dwg.rect(insert=(0,0), size=("150px","20px"), fill="#555"))
    dwg.add(dwg.rect(insert=("70px",0), size=("80px","20px"), fill=color))
    dwg.add(dwg.text(label, insert=(5,14), fill="#fff", font_size="11px"))
    dwg.add(dwg.text(f"{value_int}%", insert=(75,14), fill="#fff", font_size="11px"))
    dwg.save()

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Zero Trust badges
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    for domain, coverage in cursor.fetchall():
        safe_label = domain.replace(" ", "_")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    # ISO 27001 badges
    cursor.execute("SELECT control, coverage FROM iso_27001")
    for control, coverage in cursor.fetchall():
        safe_label = control.replace(" ", "_").replace(".", "")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    conn.close()
    print("All badges generated successfully.")

if __name__ == "__main__":
    generate_badges()
