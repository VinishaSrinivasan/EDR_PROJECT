from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Event Handler
class FileMonitor(FileSystemEventHandler):

    def on_created(self, event):
        print(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        print(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        print(f"[MODIFIED] {event.src_path}")

# Folder to monitor
FOLDER_TO_WATCH = r"D:\EDR_Project\TestFolder"

# Create observer
observer = Observer()

# Create event handler
event_handler = FileMonitor()

# Schedule monitoring
observer.schedule(
    event_handler,
    path=FOLDER_TO_WATCH,
    recursive=True
)

# Start monitoring
observer.start()

print(f"Monitoring Started: {FOLDER_TO_WATCH}")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()