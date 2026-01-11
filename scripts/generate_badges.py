import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "controls.db"
BADGE_DIR = ROOT / "assets" / "badges"
BADGE_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(name, value):
    # Numeric coverage
    if isinstance(value, str) and value.endswith('%'):
        numeric_value = int(value.rstrip('%'))
        color = "#4c1" if numeric_value >= 80 else "#dfb317" if numeric_value >= 50 else "#e05d44"
    elif isinstance(value, int):
        numeric_value = value
        color = "#4c1" if numeric_value >= 80 else "#dfb317" if numeric_value >= 50 else "#e05d44"
    elif isinstance(value, str):
        # ISO status coloring
        status_lower = value.lower()
        if "compliant" in status_lower:
            color = "#4c1"
        elif "partial" in status_lower:
            color = "#dfb317"
        else:
            color = "#e05d44"
    else:
        color = "#555"

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="150" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <rect width="90" height="20" fill="#555"/>
    <rect x="90" width="60" height="20" fill="{color}"/>
    <rect width="150" height="20" fill="url(#b)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
    <text x="45" y="14">{name}</text>
    <text x="120" y="14">{value}</text>
  </g>
</svg>
"""
    file_path = BADGE_DIR / f"{name.lower().replace(' ','_').replace('/','_')}.svg"
    with open(file_path, 'w') as f:
        f.write(svg)

def generate_badges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Zero Trust badges
    cursor.execute("SELECT domain, coverage FROM zero_trust")
    for domain, coverage in cursor.fetchall():
        create_badge(domain, f"{coverage}%")

    # ISO 27001 badges
    cursor.execute("SELECT control, status FROM iso27001")
    for control, status in cursor.fetchall():
        short_control = control.split(":")[0] if ":" in control else control
        create_badge(short_control, status)

    conn.close()
    print("Badges generated successfully.")

if __name__ == "__main__":
    generate_badges()
