from pathlib import Path
import sqlite3
import svgwrite

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "controls.db"
BADGES_DIR = ROOT / "assets/badges"
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label, value, path):
    # Determine color based on value type
    if isinstance(value, int):
        # Zero Trust coverage percentages
        if value >= 80:
            color = "#4c1"        # green
        elif value >= 50:
            color = "#dfb317"     # yellow
        else:
            color = "#e05d44"     # red
        display_value = f"{value}%"
    else:
        # ISO 27001 string statuses
        val_lower = str(value).lower()
        if val_lower == "compliant":
            color = "#4c1"
        elif val_lower == "partial":
            color = "#dfb317"
        else:  # Non-Compliant
            color = "#e05d44"
        display_value = value

    # Create SVG badge
    dwg = svgwrite.Drawing(str(path), size=("120px", "20px"))
    dwg.add(dwg.rect(insert=(0, 0), size=("120px", "20px"), fill=color))
    dwg.add(dwg.text(f"{label}: {display_value}", insert=(5, 15), fill="white", font_size="12px"))
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
