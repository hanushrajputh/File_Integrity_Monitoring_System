import os
import hashlib
from inotify_simple import INotify, flags
from hash_check import check_hash
import config
from send_email import send_alert
import datetime

LOG_FILE = 'monitor.log'

def log_event(message, alert=False):
    """Logs monitoring events to a file."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry_type = "ALERT" if alert else "INFO"
    log_message = f"{timestamp} - {entry_type} - {message}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_message)
    
    print(log_message.strip())  # Also print to console

def monitor():
    inotify = INotify()
    watches = []
    
    log_event(f"Monitoring the following directories: {config.MONITORED_DIRECTORIES}")

    # Add each directory to the inotify watch
    for directory in config.MONITORED_DIRECTORIES:
        if os.path.isdir(directory):
            watches.append(inotify.add_watch(directory, flags.MODIFY))
            log_event(f"Started monitoring directory: {directory}")
        else:
            log_event(f"Warning: Directory {directory} does not exist or is not accessible.", alert=True)

    log_event("Monitoring started. Waiting for file changes...")

    while True:
        # Blocking call that waits for file system events
        for event in inotify.read():
            for flag in flags.from_mask(event.mask):
                if flag == flags.MODIFY:
                    file_path = os.path.join(event.wd, event.name)
                    log_event(f"Detected modification in: {file_path}")

                    # Check if the modified file's hash matches the stored hash
                    if not check_hash(file_path):
                        alert_message = f"Unauthorized change detected in {file_path}"
                        log_event(alert_message, alert=True)
                        send_alert(file_path)
                    else:
                        log_event(f"Modification detected but hash is valid for {file_path}")

if __name__ == "__main__":
    monitor()
