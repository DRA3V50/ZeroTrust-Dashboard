import svgwrite
from pathlib import Path
import sqlite3

DATA_DIR = Path("data")
DB_PATH = DATA_DIR / "controls.db"
BADGES_DIR = Path("assets/badges")
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, file_path):
    # Convert value to int safely
    try:
        value_int = int(value)
    except ValueError:
        value_int = 0

    if value_int >= 80:
        color = "#4c1"  # green
    elif value_int >= 50:
        color = "#dfb317"  # yellow
    else:
        color = "#e05d44"  # red

    dwg = svgwrite.Drawing(file_path, size=("120px", "20px"))
    dwg.add(dwg.rect(insert=(0,0), size=("120px","20px"), fill=color))
    dwg.add(dwg.text(f"{label}: {value_int}%", insert=(5,15), fill="white", font_size="12px"))
    dwg.save()

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Zero Trust badges
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    for domain, coverage in cursor.fetchall():
        safe_label = domain.replace(" ", "_").replace("/", "_")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    # ISO badges
    cursor.execute("SELECT control, coverage FROM iso_controls")
    for control, coverage in cursor.fetchall():
        safe_label = control.replace(" ", "_").replace("/", "_")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    conn.close()
    print("Badges generated successfully.")

if __name__ == "__main__":
    generate_badges()
