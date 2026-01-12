import pybadges
import os

BADGES_DIR = "assets/badges"
os.makedirs(BADGES_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    # Combine text for smaller badges
    left_text = f"{control_id} | {domain}"
    right_text = str(score)
    
    # pybadges v3+ uses `label` and `value` (not left/right)
    svg_content = pybadges.badge(
        label=left_text,
        value=right_text,
        color="darkblue",
        background="#222",  # dim/dark background
        style="flat"
    )
    
    filename = f"{BADGES_DIR}/{control_id.replace('.', '_')}.svg"
    with open(filename, "w") as f:
        f.write(svg_content)
    print(f"[DEBUG] Badge saved: {filename}")
