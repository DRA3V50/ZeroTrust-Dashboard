# scripts/generate_badges.py

import pybadges
import os

ASSETS_DIR = "assets/badges"

os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_badge(control_id: str, domain: str, score: int):
    # Construct the text on the badge
    text = f"{control_id} | {domain} | Score: {score}"

    # pybadges 3.x uses `label` and `value` as separate, `left`/`right` removed
    svg_content = pybadges.badge(
        label=text,       # main label
        value="",         # no separate value
        color="#1f4e79", # dark blue
        label_color="#ffffff", # white text
        style="flat",     # flat style supported
        format="svg"      # output format
    )

    # Save badge
    filename = f"{ASSETS_DIR}/{control_id.replace('.', '_')}.svg"
    with open(filename, "w") as f:
        f.write(svg_content)
