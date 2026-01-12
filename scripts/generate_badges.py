#import pybadges
import os

ASSETS_DIR = "assets/badges"
os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_badge(control_id: str, domain: str, score: int):
    text = f"{control_id} | {domain} | Score: {score}"
    svg_content = pybadges.badge(
        label=text,
        value="",
        color="#1f4e79",
        label_color="#ffffff",
        style="flat",
        format="svg"
    )
    filename = f"{ASSETS_DIR}/{control_id.replace('.', '_')}.svg"
    with open(filename, "w") as f:
        f.write(svg_content)
