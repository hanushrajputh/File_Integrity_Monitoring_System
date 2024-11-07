
# File Integrity Monitoring System (FIMS)

## Overview
The File Integrity Monitoring System (FIMS) is a real-time security solution for detecting unauthorized changes to critical system files, which helps to prevent potential malware attacks and unauthorized modifications. It continuously monitors selected files, verifies their integrity using cryptographic hashes, and notifies users instantly of any suspicious modifications via a web-based dashboard and email alerts.

## Features
- **Real-Time Monitoring**: Uses inotify to monitor file changes in real time.
- **Hash-Based Verification**: SHA-256 hashing for detecting unauthorized modifications.
- **Web Dashboard**: Live interface built with Flask to view alerts and logs.
- **Email Notifications**: Alerts users through email when a monitored file is modified.
- **Log Auditing**: Stores a history of changes for review and analysis.

## Requirements
- **Operating System**: Kali Linux or any Linux distribution
- **Python**: Version 3.x
- **Dependencies**:
  - `Flask` for the web interface (install via `pip install flask`)
  - `inotify-tools` for monitoring (install via `sudo apt install inotify-tools`)
  - `SQLite` (optional) or JSON for hash storage
  - `smtplib` for email alerts (included with Python standard library)

## Installation
1. **Clone this repository**:
    ```bash
    git clone https://github.com/hanushrajputh/File_Integrity_Monitoring_System.git
    cd File_Integrity_Monitoring_System
    ```

2. **Set up a virtual environment** (recommended):
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    sudo apt install inotify-tools
    ```

4. **Configure `config.py`**:
   - Update `MONITORED_DIRECTORIES` with the absolute paths of directories to monitor.
   - Set `ALERT_EMAIL`, `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, and `SMTP_PASSWORD` with your email and SMTP credentials for email alerts.

## Usage
1. **Initialize File Hashes**: Run `initialize_hashes.py` to generate and store SHA-256 hashes of the critical files you want to monitor.
   ```bash
   python initialize_hashes.py
   ```

2. **Start Monitoring**: Run the main script `monitor.py` to start monitoring the specified directories for any changes.
   ```bash
   python monitor.py
   ```

3. **Access the Web Dashboard**: Open the web interface by navigating to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view file status and alerts.

## File Structure
- `monitor.py`: Main monitoring script that uses inotify to detect file changes and triggers hash verification.
- `initialize_hashes.py`: Script to set up initial hashes for the files you want to monitor.
- `hash_check.py`: Contains the function for SHA-256 hash verification.
- `config.py`: Configuration file for email and monitored directories.
- `app.py`: Flask application for the web dashboard.
- `templates/index.html`: Dashboard template to display real-time alerts.
- `send_email.py`: Script to handle email notifications.
- `requirements.txt`: Required Python packages.
- `README.md`: Documentation of the project.

## Sample Configuration (`config.py`)
```python
MONITORED_DIRECTORIES = ['/path/to/directory1', '/path/to/directory2']
ALERT_EMAIL = 'your_email@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
```

## Environment Setup
1. **Activate the Virtual Environment**:
   ```bash
   source myenv/bin/activate
   ```

2. **Start the Flask Application**:
   ```bash
   python app.py
   ```

3. **Run Monitoring Script**:
   ```bash
   python monitor.py
   ```

## Troubleshooting & Common Issues
1. **Error: `FileNotFoundError: [Errno 2] No such file or directory` in `monitor.py`**:
   - This error occurs if a directory specified in `MONITORED_DIRECTORIES` does not exist.
   - **Solution**: Ensure that all paths in `config.py` are valid and accessible on your system. You can create missing directories using `mkdir`:
     ```bash
     mkdir -p /path/to/directory1
     ```

2. **Permission Errors**:
   - Monitoring system-critical files may require elevated permissions.
   - **Solution**: Run scripts with `sudo` if needed or adjust permissions on specific directories.

3. **Email Not Sending**:
   - Check SMTP configurations in `config.py` and confirm they are correct.
   - Ensure your email provider supports SMTP for sending emails from applications.

## Demonstration
1. **File Change Detection**: Modify a monitored file and observe the detection on the dashboard.
2. **Email Alert**: Receive an email notification for the detected change.
3. **Dashboard Alert**: View real-time status on the web dashboard with details of changed files.


## Contributing
Feel free to fork this repository, report issues, and make pull requests!
