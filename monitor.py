import os
import hashlib
from inotify_simple import INotify, flags
from hash_check import check_hash
import config
from send_email import send_alert

def monitor():
    inotify = INotify()
    watches = []

    # Print monitored directories for debugging
    print(f"Monitoring the following directories: {config.MONITORED_DIRECTORIES}")

    # Add each directory to the inotify watch
    for directory in config.MONITORED_DIRECTORIES:
        if os.path.isdir(directory):
            watches.append(inotify.add_watch(directory, flags.MODIFY))
            print(f"Started monitoring directory: {directory}")
        else:
            print(f"Warning: Directory {directory} does not exist or is not accessible.")
    
    print("Monitoring started. Waiting for file changes...")

    while True:
        # Blocking call that waits for file system events
        for event in inotify.read():
            for flag in flags.from_mask(event.mask):
                if flag == flags.MODIFY:
                    file_path = os.path.join(event.wd, event.name)
                    print(f"Detected modification in: {file_path}")

                    # Check if the modified file's hash matches the stored hash
                    if not check_hash(file_path):
                        print(f"ALERT: Unauthorized change detected in {file_path}")
                        send_alert(file_path)
                    else:
                        print(f"Modification detected but hash is valid for {file_path}")

if __name__ == "__main__":
    monitor()
