import os
import sqlite3
import matplotlib.pyplot as plt

try:
    import pandas as pd
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

from scripts.create_controls_db import db_path

os.makedirs("outputs/graphs", exist_ok=True)

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)

# Zero Trust posture bar graph
plt.figure(figsize=(6, 3))
plt.bar(df['domain'], df['score'], color='#4c1')
plt.title("Zero Trust Posture")
plt.ylabel("Score (%)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/graphs/zero_trust_posture.png", dpi=100)
plt.close()

# ISO 27001 coverage graph (same example)
plt.figure(figsize=(6, 3))
plt.bar(df['control'], df['score'], color='#007ec6')
plt.title("ISO 27001 Control Coverage")
plt.ylabel("Score (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/graphs/iso_27001_coverage.png", dpi=100)
plt.close()

conn.close()
print("Graphs generated successfully.")
