import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("data/controls.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def create_db():
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame({
        "control_id": ["A.5.1", "A.6.1", "A.7.2", "A.9.2"],
        "domain": ["Identity", "Device", "Network", "Data"],
        "score": [3, 2, 4, 5]
    })
    df.to_sql("controls", conn, if_exists="replace", index=False)
    conn.close()
    print(f"[DEBUG] Database created/populated at {DB_PATH}")

if __name__ == "__main__":
    create_db()
