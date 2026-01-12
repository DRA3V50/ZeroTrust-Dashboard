import pybadges
import os

BADGES_DIR = "assets/badges"
os.makedirs(BADGES_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    """Generate SVG badge using pybadges 3.x API"""
    text = f"{control_id} | {domain} | {score}"

    # Use 'label' and 'value' removed; pybadges 3.x uses single 'text'
    svg = pybadges.badge(
        text=text,
        color="darkblue",      # background color of badge
        label_color="lightgrey", # left side bg if using split badge
        style="flat"           # can be 'flat', 'plastic', etc.
    )

    file_path = os.path.join(BADGES_DIR, f"{control_id.replace('.', '_')}.svg")
    with open(file_path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge generated: {file_path}")
