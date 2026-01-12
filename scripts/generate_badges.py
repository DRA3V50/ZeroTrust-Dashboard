import pybadges

def generate_badge(control_id, domain, score, output_path="assets/badges"):
    """
    Generate a single badge using pybadges 3.x
    """
    import os
    os.makedirs(output_path, exist_ok=True)

    # combine text for left side
    left_text = f"{control_id}: {domain}"
    right_text = str(score)

    # badge with dark blue background
    svg_content = pybadges.badge(
        left_text=left_text,
        right_text=right_text,
        left_color="#1f2937",   # dark gray for left
        right_color="#2563eb",  # bright blue for score
        style="flat",           # flat style prevents text overlap
        font_size=11            # smaller font
    )

    file_name = f"{control_id.replace('.', '_')}.svg"
    with open(f"{output_path}/{file_name}", "w") as f:
        f.write(svg_content)
