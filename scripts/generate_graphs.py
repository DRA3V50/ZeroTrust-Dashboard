import sqlite3
from pathlib import Path

# Ensure pandas and matplotlib are available
try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas matplotlib"])
    import pandas as pd
    import matplotlib.pyplot as plt

from create_controls_db import db_path

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM controls", conn)
conn.close()

Path("outputs/graphs").mkdir(parents=True, exist_ok=True)

# Zero Trust Posture Graph
plt.figure(figsize=(4,2))
plt.bar(df['control'], df['score'], color='darkblue')
plt.title("Zero Trust & ISO 27001 Controls")
plt.ylim(0, 100)
plt.savefig("outputs/graphs/zero_trust_posture.png", dpi=150)
plt.close()

# ISO 27001 Coverage Graph (example same as above for simplicity)
plt.figure(figsize=(4,2))
plt.bar(df['control'], df['score'], color='darkgreen')
plt.title("ISO 27001 Coverage")
plt.ylim(0, 100)
plt.savefig("outputs/graphs/iso_27001_coverage.png", dpi=150)
plt.close()

print("Graphs generated successfully.")
