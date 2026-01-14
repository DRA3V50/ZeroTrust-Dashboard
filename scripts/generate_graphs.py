import sqlite3
import matplotlib.pyplot as plt
import os
from create_controls_db import db_path

os.makedirs("outputs/graphs", exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT control, score FROM controls")
data = c.fetchall()
conn.close()

controls = [row[0] for row in data]
scores = [row[1] for row in data]

plt.figure(figsize=(5, 3))
plt.bar(controls, scores, color="#1f77b4")
plt.title("Zero Trust / ISO 27001 Scores", color="white")
plt.ylabel("Score %", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#2E2E2E")  # Dark background
plt.gcf().patch.set_facecolor('#2E2E2E')

graph_file = f"outputs/graphs/zero_trust_posture.png"
plt.savefig(graph_file, dpi=100, bbox_inches='tight')
plt.close()
print(f"Graph saved to {graph_file}")
