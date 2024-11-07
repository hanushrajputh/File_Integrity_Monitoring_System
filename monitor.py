import os
import hashlib
from inotify_simple import INotify, flags
from hash_check import check_hash
import config
from send_email import send_alert

def monitor():
    inotify = INotify()
    watches = []
    for directory in config.MONITORED_DIRECTORIES:
        watches.append(inotify.add_watch(directory, flags.MODIFY))

    while True:
        for event in inotify.read():
            for flag in flags.from_mask(event.mask):
                if flag == flags.MODIFY:
                    file_path = os.path.join(event.wd, event.name)
                    if not check_hash(file_path):
                        print(f"ALERT: Unauthorized change detected in {file_path}")
                        send_alert(file_path)

if __name__ == "__main__":
    monitor()
