# SOC Web Dashboard (Flask)

from flask import Flask, render_template
from core.detector import analyze_log

app = Flask(__name__)

@app.route("/")
def index():

    alerts = []

    # Read logs
    with open("data/logs.txt", "r") as file:
        logs = file.readlines()

    # Analyze logs
    for log in logs:
        log = log.strip()
        alert = analyze_log(log)

        if alert:
            alerts.append(alert)

    return render_template("index.html", logs=logs, alerts=alerts)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
