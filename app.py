<<<<<<< HEAD
import json

from utils.profile_builder import build_profiles
from rules.location_rule import detect_new_location
from rules.login_attempt_rule import detect_failed_logins
from rules.access_rule import detect_unauthorized_access
from rules.browser_rule import detect_new_browser
from rules.login_time_rule import detect_unusual_login_time

with open("data/historical_logs.json", "r") as file:
    historical_logs = json.load(file)

with open("data/new_logs.json", "r") as file:
    new_logs = json.load(file)

profiles = build_profiles(historical_logs)

all_results = []

for event in new_logs:
    user = event["user"]
    alerts = []
    total_risk = 0

    checks = [
        detect_new_location(user, event["country"], profiles),
        detect_failed_logins(user, event["failed_logins"], profiles),
        detect_unauthorized_access(user, event["resource"], profiles),
        detect_new_browser(user, event["browser"], profiles),
        detect_unusual_login_time(user, event["login_hour"], profiles)
    ]
    for result in checks:
        if result:
            alerts.append(result["alert"])
            total_risk += result["risk"]

    if total_risk <= 30:
        risk_level = "Low"
    elif total_risk <= 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    output = {
        "user": user,
        "timestamp": event["timestamp"],
        "alerts": alerts,
        "risk_score": total_risk,
        "risk_level": risk_level
    }

    all_results.append(output)

with open("output/alerts.json", "w") as outfile:
    json.dump(all_results, outfile, indent=4)

print(json.dumps(all_results, indent=4))
=======
from flask import Flask, jsonify
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from sample_data import rule_events, honeypot_events
import json

app = Flask(__name__)

@app.route("/analyze", methods=["GET"])
def analyze():
    events = merge_events(rule_events, honeypot_events)
    risk = calculate_risk(events)
    timeline = build_timeline(events)
    explanation = generate_explanation(risk)

    output = {
        "risk_score": risk,
        "timeline": timeline,
        "explanation": explanation
    }

    # Save for dashboard
    with open("output.json", "w") as f:
        json.dump(output, f, indent=4)

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 0fbd5765d30f3dc4f9647c6ca4725dcc78821c21
