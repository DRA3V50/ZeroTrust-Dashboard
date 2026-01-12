import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = 'data/controls.db'
GRAPH_DIR = 'assets/graphs'
os.makedirs(GRAPH_DIR, exist_ok=True)

# Fetch data
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT control_id, domain, score FROM controls", conn)
conn.close()

# Zero Trust Posture graph
plt.figure(figsize=(12,7))
plt.bar(df['domain'], df['score'], color='#1f77b4')
plt.xlabel('Security Domain', color='white', fontsize=12)
plt.ylabel('Score', color='white', fontsize=12)
plt.title('Zero Trust Posture', color='white', fontsize=14)
plt.xticks(rotation=30, ha='right', color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)
plt.gca().set_facecolor('#2b2b2b')
plt.gcf().patch.set_facecolor('#2b2b2b')
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'zero_trust_posture.png'))
plt.close()

# ISO 27001 Coverage graph
plt.figure(figsize=(12,7))
plt.bar(df['control_id'], df['score'], color='#ff7f0e')
plt.xlabel('ISO 27001 Control', color='white', fontsize=12)
plt.ylabel('Compliance Score', color='white', fontsize=12)
plt.title('ISO 27001 Control Coverage', color='white', fontsize=14)
plt.xticks(rotation=30, ha='right', color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)
plt.gca().set_facecolor('#2b2b2b')
plt.gcf().patch.set_facecolor('#2b2b2b')
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'iso_27001_coverage.png'))
plt.close()
