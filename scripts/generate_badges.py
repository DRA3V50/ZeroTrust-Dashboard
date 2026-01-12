from pybadges import badge

def generate_control_badge(control_id, domain, score, color='blue'):
    """
    Generates an SVG badge for a control.
    Compatible with older and newer versions of pybadges.
    """
    try:
        # Try the newer syntax first
        svg = badge(label=control_id, message=domain, right_color=color)
    except TypeError:
        # Fallback for older pybadges versions
        svg = badge(left_text=control_id, right_text=domain, right_color=color)

    # Save the SVG badge
    filename = f"assets/badges/{control_id.replace('.', '_')}.svg"
    with open(filename, 'w') as f:
        f.write(svg)
    print(f"Badge saved: {filename}")
