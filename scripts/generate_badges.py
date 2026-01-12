import os
import pybadges

os.makedirs("assets/badges", exist_ok=True)

def generate_badge(control_id, domain, score):
    score_text = f"{score}%"
    control_text = f"{control_id} | {domain}"

    svg_content = pybadges.badge(
        left_text=control_text,
        right_text=score_text,
        left_color="#1f77b4",  # dimmer blue
        right_color="#d62728",  # dim red
        height=20,               # smaller to reduce overlap
        font_size=10             # smaller font
    )

    filename = f"assets/badges/{control_id.replace('.', '_')}.svg"
    with open(filename, "w") as f:
        f.write(svg_content)
    print(f"[DEBUG] Badge saved: {filename}")
