import sqlite3
from datetime import datetime
import random

events = [
    "Unauthorized Process",
    "PowerShell Execution",
    "Failed Login Attempt",
    "Suspicious File Created",
    "Registry Modification"
]

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

for i in range(50):

    cursor.execute(
        """
        INSERT INTO alerts(time, process, severity)
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            random.choice(events),
            random.choice(["Low", "Medium", "High", "Critical"])
        )
    )

conn.commit()
conn.close()

print("50 alerts inserted successfully")