import os
from pybadges import badge

BADGES_DIR = 'assets/badges'
os.makedirs(BADGES_DIR, exist_ok=True)

def generate_control_badge(control_id, domain, score, color='blue'):
    """
    Generates an SVG badge for a control.
    Compatible with older and newer versions of pybadges.
    """
    try:
        # Newer pybadges versions
        svg = badge(label=control_id, message=domain, right_color=color)
    except TypeError:
        # Older pybadges versions
        svg = badge(left_text=control_id, right_text=domain, right_color=color)

    filename = os.path.join(BADGES_DIR, f"{control_id.replace('.', '_')}.svg")
    with open(filename, 'w') as f:
        f.write(svg)
    print(f"Badge saved: {filename}")


# Example usage (replace this with your DataFrame loop)
if __name__ == "__main__":
    sample_controls = [
        ('A.5.1', 'Information Security Policies', 80),
        ('A.6.1', 'Organization of Information Security', 75),
        ('A.8.2', 'Risk Management', 90),
        ('A.9.2', 'Access Control', 85)
    ]
    
    for control_id, domain, score in sample_controls:
        generate_control_badge(control_id, domain, score)
