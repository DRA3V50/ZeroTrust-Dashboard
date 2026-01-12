import os
import shutil

BADGE_DIR = 'assets/badges'
os.makedirs(BADGE_DIR, exist_ok=True)

def generate_badges():
    badges = ['Identity.svg', 'Device.svg', 'Network.svg', 'Application.svg', 'Data.svg']
    for badge in badges:
        path = os.path.join(BADGE_DIR, badge)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write(f'<svg><text>{badge.replace(".svg","")}</text></svg>')
    print(f"Badges generated successfully in {BADGE_DIR}")

if __name__ == "__main__":
    generate_badges()
