import svgwrite
from pathlib import Path
import sqlite3

DB_PATH = Path("data/controls.db")
BADGES_DIR = Path("assets/badges")
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, filepath):
    # Ensure value is int
    if isinstance(value, str):
        value = int(value)

    # Determine badge color
    if value >= 80:
        color = "#4c1"  # green
    elif value >= 50:
        color = "#dfb317"  # yellow
    else:
        color = "#e05d44"  # red

    dwg = svgwrite.Drawing(str(filepath), size=("120px", "20px"))
    dwg.add(dwg.rect(insert=(0, 0), size=("120px", "20px"), rx=3, ry=3, fill=color))
    dwg.add(dwg.text(f"{label}: {value}%", insert=(5, 15), fill="#fff", font_size="10px", font_family="Verdana"))
    dwg.save()

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = cursor.fetchall()

    cursor.execute("SELECT control_id, coverage FROM iso_controls")
    iso_controls = cursor.fetchall()

    conn.close()

    for domain, coverage in zero_trust:
        safe_label = domain.replace(" ", "_")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    for control, coverage in iso_controls:
        safe_label = control.replace(".", "_")
        create_badge(safe_label, coverage, BADGES_DIR / f"{safe_label}.svg")

    print("Badges generated successfully.")

if __name__ == "__main__":
    generate_badges()
