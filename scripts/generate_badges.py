import pybadges
import os

ASSET_DIR = "assets/badges"
os.makedirs(ASSET_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    svg = pybadges.badge(
        label=f"{control_id} | {domain}",
        value=str(score),
        color="darkblue"
    )
    path = os.path.join(ASSET_DIR, f"{control_id}.svg")
    with open(path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge generated: {path}")

if __name__ == "__main__":
    # sample call
    generate_badge("A.5.1", "Identity", 80)
