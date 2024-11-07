from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Load monitoring log data
    log_file_path = 'monitor.log'
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as f:
            log_data = f.readlines()
    else:
        log_data = ["No monitoring events logged yet."]
        
    return render_template("index.html", logs=log_data)

if __name__ == "__main__":
    app.run(debug=True)
