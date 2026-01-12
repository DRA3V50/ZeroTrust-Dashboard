import pybadges
import os

BADGE_PATH = 'assets/badges/'
os.makedirs(BADGE_PATH, exist_ok=True)

def generate_control_badge(control_id, domain, score):
    control_text = f"{control_id}: {domain}"
    score_text = str(score)
    # Corrected pybadges call
    svg = pybadges.badge(left_text=control_text, right_text=score_text, color='darkblue')
    file_name = f"{control_id.replace('.', '_')}.svg"
    path = os.path.join(BADGE_PATH, file_name)
    with open(path, "w") as f:
        f.write(svg)
    print(f"[DEBUG] Badge generated: {path}")

if __name__ == "__main__":
    # Example for testing
    generate_control_badge("A.5.1", "Identity", 85)
