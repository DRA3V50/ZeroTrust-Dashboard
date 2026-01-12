import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os
from generate_badges import generate_badge

os.makedirs("assets/graphs", exist_ok=True)

# Fetch data
conn = sqlite3.connect("data/controls.db")
df = pd.read_sql_query("SELECT * FROM controls", conn)
conn.close()
print(f"[DEBUG] Retrieved {len(df)} records from DB")

# Zero Trust Posture graph
plt.figure(figsize=(6,4))
plt.bar(df['domain'], df['score'], color='darkslategray')
plt.ylim(0,100)
plt.title("Zero Trust Posture", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("assets/graphs/zero_trust_posture.png")
plt.close()
print("[DEBUG] Zero Trust graph saved")

# ISO 27001 Coverage graph
plt.figure(figsize=(6,4))
plt.bar(df['domain'], df['score'], color='dimgray')
plt.ylim(0,100)
plt.title("ISO 27001 Coverage", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("assets/graphs/iso_27001_coverage.png")
plt.close()
print("[DEBUG] ISO 27001 graph saved")

# Generate badges
for _, row in df.iterrows():
    generate_badge(row['control_id'], row['domain'], row['score'])
