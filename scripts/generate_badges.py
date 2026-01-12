import os
from datetime import datetime

BADGE_DIR = "outputs/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    # Dynamic colors
    if score >= 80: color = "#27ae60"  # green
    elif score >= 50: color = "#f39c12"  # orange
    else: color = "#c0392b"  # red

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{BADGE_DIR}/{control_id}_{timestamp}.svg"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="340" height="42">
  <rect width="340" height="42" rx="6" fill="#1e1e1e"/>
  <text x="12" y="26" fill="{color}" font-size="14" font-family="Arial">
    {control_id} • {domain} • {score}%
  </text>
</svg>
"""
    with open(filename, "w") as f:
        f.write(svg)
    print(f"[OK] Badge generated: {filename}")
