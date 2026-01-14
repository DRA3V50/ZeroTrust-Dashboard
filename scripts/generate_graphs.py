import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3

from create_controls_db import db_path

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

os.makedirs("outputs/graphs", exist_ok=True)

# Zero Trust graph
plt.figure(figsize=(4,2))
plt.bar(df['control'], df['score'], color='skyblue')
plt.title("Zero Trust & ISO 27001 Control Scores")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/graphs/zero_trust_posture.png")
plt.close()

# ISO 27001 coverage graph (same example)
plt.figure(figsize=(4,2))
plt.bar(df['control'], df['score'], color='salmon')
plt.title("ISO 27001 Control Coverage")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/graphs/iso_27001_coverage.png")
plt.close()

print("Graphs generated successfully.")
