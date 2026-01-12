import sqlite3
import svgwrite

def generate_badges():
    conn = sqlite3.connect('data/controls.db')
    c = conn.cursor()
    c.execute("SELECT control_id, score FROM controls")
    controls = c.fetchall()
    conn.close()

    for control_id, score in controls:
        dwg = svgwrite.Drawing(f"assets/badges/{control_id.replace('.', '_')}.svg", profile='tiny', size=("150px","30px"))
        dwg.add(dwg.rect(insert=(0,0), size=("150px","30px"), fill='lightgrey'))
        dwg.add(dwg.text(f"{control_id}: {score}%", insert=(5,20), fill='black'))
        dwg.save()
    print("Badges generated successfully.")

if __name__ == '__main__':
    generate_badges()
