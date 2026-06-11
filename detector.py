import psutil
import time
from datetime import datetime
import sqlite3

blacklist = [
    "malware.exe",
    "keylogger.exe",
    "hacktool.exe"
]

while True:

    for process in psutil.process_iter(['name']):

        pname = process.info['name']

        if pname in blacklist:
            print("Threat Found:", pname)

    time.sleep(5)
conn = sqlite3.connect("alerts.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO alerts(time,process,severity)
VALUES(?,?,?)
""",
(
datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
pname,
"High"
))

conn.commit()
conn.close()