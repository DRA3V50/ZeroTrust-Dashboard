import pybadges
import os

BADGE_DIR = "outputs/badges"
os.makedirs(BADGE_DIR, exist_ok=True)

def generate_badge(control_id, domain, score):
    """
    Generate an SVG badge for a control
    """
    badge = pybadges.badge(
        left_text=f"{control_id} ({domain})",
        right_text=f"{score}%",
        right_color="#4c1"
    )
    badge_path = os.path.join(BADGE_DIR, f"{control_id}.svg")
    with open(badge_path, "w") as f:
        f.write(badge)
    print(f"[OK] Badge generated: {badge_path}")

if __name__ == "__main__":
    # Example usage for testing
    generate_badge("A.5.1", "Policy", 87)
