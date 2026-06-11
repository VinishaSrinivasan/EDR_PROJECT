import sqlite3
from datetime import datetime

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO alerts(time, process, severity)
VALUES (?, ?, ?)
""",
(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "malware.exe",
    "High"
))

conn.commit()
conn.close()

print("Test alert inserted")