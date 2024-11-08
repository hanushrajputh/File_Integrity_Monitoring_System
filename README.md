
# File Integrity Monitoring System (FIMS)

## Overview
Imagine this: you're on your computer, unaware that a hidden malware is altering critical files. These changes could compromise your data and system. That’s where the **File Integrity Monitoring System (FIMS)** steps in, like a vigilant security guard monitoring files in real time.

With **SHA-256 hashing**, FIMS detects unauthorized file changes instantly. When it finds an issue, it alerts you right away on a live dashboard and by email.

FIMS isn’t just watching over your files—it’s actively protecting them. In today’s data-driven world, where integrity and security are paramount, FIMS ensures your files stay uncompromised, keeping your operations uninterrupted. It’s more than a tool; it’s essential peace of mind for your digital workspace.

In the future, FIMS will expand to monitor cloud-stored data, providing seamless protection for both local and cloud assets. This upcoming feature will make FIMS a powerful solution for comprehensive data integrity in an increasingly cloud-reliant world.

The File Integrity Monitoring System (FIMS) is a real-time security solution that detects unauthorized changes to critical system files. 
It helps prevent malware attacks and unauthorized modifications by continuously monitoring files, verifying their integrity using cryptographic 
hashes (SHA-256), and notifying users through email alerts and a web dashboard.

## Features
- **Real-Time Monitoring:** Monitors file changes using inotify in real time.
- **Hash-Based Verification:** Uses SHA-256 hashes to detect unauthorized file modifications.
- **Web Dashboard:** A live web interface built with Flask to display alerts and logs.
- **Email Notifications:** Sends email alerts when a monitored file is modified.
- **Log Auditing:** Keeps a history of changes for review and analysis.

## Requirements
- Kali Linux (or any other Linux distribution)
- Python 3.x
- Flask (for the web interface)
- inotify-tools (for monitoring)
- smtplib (for email alerts)
- Optional: SQLite (for database-based hash storage)

## Clone this repository:
```bash
git clone https://github.com/hanushrajputh/File_Integrity_Monitoring_System.git  

cd File_Integrity_Monitoring_System  
```
## Install Python Dependencies
### Create a Virtual Environment (Optional but Recommended):
```bash
python3 -m venv myenv
```

### Activate the Virtual Environment:
For Linux/macOS:
```bash
source myenv/bin/activate
```
For Windows:
```bash
myenv\Scripts\activate
```

### Install Required Python Packages: 
Install the dependencies listed in requirements.txt using pip:
```bash
pip install -r requirements.txt
```

### Install Inotify Tools: 
The system uses inotify-tools to monitor file changes. Install it on your Linux machine:
```bash
sudo apt install inotify-tools
```

## Configuration
Configure the Directories and Email Settings:
1. Open the `config.py` file and update the following variables:
   - `MONITORED_DIRECTORIES`: List of directories to monitor for file changes (e.g., `['/path/to/directory1', '/path/to/directory2']`).
   - `ALERT_EMAIL`: Email address to send alerts to.
   - `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`: SMTP settings for sending email notifications (use your email provider's SMTP settings).

### Sample configuration:
```python
MONITORED_DIRECTORIES = ['/path/to/directory1', '/path/to/directory2']
ALERT_EMAIL = 'your_email@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
```

## Installation and Usage

### 1. Initialize File Hashes
Before starting the monitoring process, you need to generate SHA-256 hashes for the files you want to monitor. This step can be performed by running the `initialize_hashes.py` script.
```bash
python initialize_hashes.py
```
This will generate and store the initial hashes of files in the specified monitored directories in a `file_hashes.json` file.

### 2. Start Monitoring
Run the `monitor.py` script to start monitoring the directories. The script will detect any file changes, compare the file hashes, and send alerts if unauthorized modifications are detected.
```bash
python monitor.py
```
You will see a message like the following indicating that monitoring has started:
```
Monitoring the following directories: ['/path/to/directory1', '/path/to/directory2']
Started monitoring directory: /path/to/directory1
Started monitoring directory: /path/to/directory2
Monitoring started. Waiting for file changes...
```

### 3. Access the Web Dashboard
You can also view a web interface displaying the status of monitored files. To access the dashboard:

1. Run the Flask app by executing `app.py`:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
   The web interface will show real-time alerts and logs.

## File Structure
- **monitor.py**: Main monitoring script that detects file changes using inotify and triggers hash verification.
- **initialize_hashes.py**: Initializes the file hashes for files in the monitored directories.
- **hash_check.py**: Contains the function to verify file integrity using SHA-256 hashes.
- **config.py**: Configuration file for email alerts and monitored directories.
- **app.py**: Flask web application to serve the dashboard.
- **templates/index.html**: Web interface template to display real-time alerts.
- **send_email.py**: Script to handle sending email notifications when a file change is detected.
- **requirements.txt**: Lists the required Python dependencies.

## Example Workflow
1. **Modify a Monitored File**: Change a file in one of the monitored directories.
2. **File Change Detection**: The system detects the change and compares the file hash with the stored hash.
3. **Email Alert**: The system sends an email notification to the configured email address.
4. **Dashboard Alert**: The web dashboard shows the detected file change with details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository, report issues, and make pull requests! Contributions are welcome.

**Note**: Make sure you have the correct permissions for the directories you want to monitor, and that the email credentials in `config.py` are set up correctly for sending alerts.
