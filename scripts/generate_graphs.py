import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import os

# Database path
db_path = "data/controls.db"

# Read control data
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

# Create output folder if missing
os.makedirs("outputs/graphs", exist_ok=True)

# General dark theme
plt.style.use('dark_background')

# --- Zero Trust Posture Graph ---
fig, ax = plt.subplots(figsize=(5, 3))  # ~295px width equivalent
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # consistent color palette
ax.bar(df['domain'], df['score'], color=colors)

ax.set_ylim(0, 100)
ax.set_ylabel('Score (%)', color='white')
ax.set_title('Zero Trust Posture', color='white')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(colors='white')

# Save graph
zt_graph_path = "outputs/graphs/zero_trust_posture.png"
plt.tight_layout()
plt.savefig(zt_graph_path, dpi=100)
plt.close(fig)

# --- ISO 27001 Coverage Graph ---
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(df['control'], df['score'], color='#ff7f0e')

ax.set_ylim(0, 100)
ax.set_ylabel('Score (%)', color='white')
ax.set_title('ISO 27001 Control Coverage', color='white')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(colors='white')

# Save graph
iso_graph_path = "outputs/graphs/iso_27001_coverage.png"
plt.tight_layout()
plt.savefig(iso_graph_path, dpi=100)
plt.close(fig)

print("Graphs generated successfully.")
