import pandas as pd
import matplotlib.pyplot as plt
import os
from create_controls_db import db_path

os.makedirs("outputs/graphs", exist_ok=True)

df = pd.read_sql("SELECT * FROM controls", sqlite3.connect(db_path))

# Dark theme settings
plt.style.use('dark_background')

# Zero Trust posture graph
fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(df['control'], df['score'], color='limegreen')
ax.set_ylim(0, 100)
ax.set_title("Zero Trust Posture")
ax.set_ylabel("Score (%)")
fig.tight_layout()
plt.savefig("outputs/graphs/zero_trust_posture.png", dpi=100)
plt.close(fig)

# ISO 27001 coverage graph
fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(df['control'], df['score'], color='deepskyblue')
ax.set_ylim(0, 100)
ax.set_title("ISO 27001 Coverage")
ax.set_ylabel("Score (%)")
fig.tight_layout()
plt.savefig("outputs/graphs/iso_27001_coverage.png", dpi=100)
plt.close(fig)
