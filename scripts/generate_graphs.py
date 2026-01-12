import os
import sqlite3
import pandas as pd

# For generating SVG badges
from pybadges import badge

# Paths
DB_PATH = 'data/controls.db'
BADGE_DIR = 'assets/badges'

# Ensure badges directory exists
os.makedirs(BADGE_DIR, exist_ok=True)

# Function to fetch controls from SQLite
def fetch_controls():
    print("Fetching control data from SQLite DB...")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT control_id, domain, score FROM controls"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Function to generate badge for a single control
def generate_control_badge(control_id, domain, score):
    label = f"{control_id} - {domain}"
    message = f"{score}%"
    color = "green" if score >= 80 else "orange" if score >= 50 else "red"
    
    svg = badge(
        label=label,
        value=message,
        color=color,
        style='flat'
    )
    
    badge_path = os.path.join(BADGE_DIR, f"{control_id.replace('.', '_')}.svg")
    with open(badge_path, "w") as f:
        f.write(svg)
    
    print(f"Badge for {control_id} saved at {badge_path}")

# Main execution
if __name__ == "__main__":
    controls_data = fetch_controls()
    
    if controls_data.empty:
        print("No control data found! Ensure your database has entries.")
    else:
        for _, row in controls_data.iterrows():
            generate_control_badge(row['control_id'], row['domain'], row['score'])

    print("All badges generated successfully!")
