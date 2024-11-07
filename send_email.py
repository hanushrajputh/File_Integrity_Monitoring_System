import smtplib
from email.mime.text import MIMEText
import config

def send_alert(file_path):
    msg = MIMEText(f"ALERT: Unauthorized change detected in {file_path}")
    msg['Subject'] = 'File Integrity Alert'
    msg['From'] = config.SMTP_USERNAME
    msg['To'] = config.ALERT_EMAIL

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
        server.sendmail(config.SMTP_USERNAME, config.ALERT_EMAIL, msg.as_string())
