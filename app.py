from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    # Load file hash log and pass to the template
    with open('file_hashes.json', 'r') as f:
        hashes = json.load(f)
    return render_template("index.html", hashes=hashes)

if __name__ == "__main__":
    app.run(debug=True)
