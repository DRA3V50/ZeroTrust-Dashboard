from pathlib import Path
import svgwrite
import sqlite3

DB_PATH = Path("data/controls.db")
BADGES_DIR = Path("assets/badges")

def fetch_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    zero_trust = [(row[0], int(row[1])) for row in cursor.fetchall()]
    cursor.execute("SELECT control, coverage FROM iso_controls")
    iso_controls = [(row[0], int(row[1])) for row in cursor.fetchall()]
    conn.close()
    return zero_trust + iso_controls

def create_badge(label, value, file_path):
    """Creates a simple SVG badge"""
    # Convert value to int if needed
    try:
        value = int(value)
    except:
        value = 0

    # Determine color
    if value >= 80:
        color = "#4c1"
    elif value >= 50:
        color = "#dfb317"
    else:
        color = "#e05d44"

    dwg = svgwrite.Drawing(str(file_path), size=("120px", "20px"))
    dwg.add(dwg.rect(insert=(0, 0), size=("120px", "20px"), rx=3, ry=3, fill=color))
    dwg.add(dwg.text(f"{label}: {value}%", insert=(10, 14), fill="#fff", font_size="12px", font_family="Verdana"))
    dwg.save()

def generate_badges():
    metrics = fetch_metrics()
    BADGES_DIR.mkdir(parents=True, exist_ok=True)

    for label, value in metrics:
        safe_label = label.replace(" ", "_").replace("/", "_").replace(".", "_")
        create_badge(safe_label, value, BADGES_DIR / f"{safe_label}.svg")
    
    print("Badges generated successfully.")

if __name__ == "__main__":
    generate_badges()
