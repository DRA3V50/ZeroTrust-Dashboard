import pybadges
import os

BADGE_DIR = "outputs/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    badge = pybadges.badge(
        left_text=f"{control_id} ({domain})",
        right_text=f"{score}%",
        right_color="#4c1"
    )
    with open(f"{BADGE_DIR}/{control_id}.svg", "w") as f:
        f.write(badge)
