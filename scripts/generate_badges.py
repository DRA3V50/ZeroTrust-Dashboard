import os

BADGE_DIR = "assets/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    bg = "#1e1e1e"
    text = "#ffffff"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="340" height="42">
  <rect width="340" height="42" rx="6" fill="{bg}"/>
  <text x="12" y="26" fill="{text}" font-size="14" font-family="Arial">
    {control_id} • {domain} • {score}%
  </text>
</svg>
"""

    with open(f"{BADGE_DIR}/{control_id}.svg", "w") as f:
        f.write(svg)
