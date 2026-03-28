import json

# Load login credentials
def load_users():
    with open("users.json") as f:
        return json.load(f)

# Check login
def check_login(email, password):
    users = load_users()
    for u in users:
        if u["email"] == email and u["password"] == password:
            return True
    return False

# Load historical logs
def load_historical_logs():
    with open("historical_logs.json") as f:
        return json.load(f)

# Filter logs for a specific user (Alice)
def get_user_logs(email):
    logs = load_historical_logs()
    return [e for e in logs if e["user"] == email]

from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
import json
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from simulator import current_rule_events, current_honeypot_events
from rules.all_rules import apply_all_rules  # your person1 rules

app = Flask(__name__)
CORS(app)

# JSON files
DATA_DIR = Path(__file__).parent / "data"
HISTORICAL_FILE = DATA_DIR / "historical_logs.json"
NEW_FILE = DATA_DIR / "new_logs.json"

MAX_RISK_SCORE = 80  # for normalization

# ---------------------- Helper functions ----------------------
def load_json_events(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠ Failed to load {file_path.name}: {e}")
        return []

def json_to_events(json_logs):
    """Convert JSON logs to standard events for risk engine"""
    events = []
    for e in json_logs:
        desc = f"{e['user']} logged in from {e['country']} using {e['browser']} at hour {e['login_hour']} accessing {e['resource']} (failed: {e['failed_logins']})"
        events.append({
            "type": "rule",  # JSON logs treated as rule events
            "description": desc,
            "timestamp": e["timestamp"],
            "user": e["user"]
        })
    return events

# ---------------------- New /analyze route ----------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        email = data.get("email")  # get logged-in user email

        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Load logs
        historical_events = json_to_events(load_json_events(HISTORICAL_FILE))
        new_events = json_to_events(load_json_events(NEW_FILE))

        # Apply rules to simulator events
        new_rule_events = apply_all_rules(current_rule_events)

        # Merge all events
        combined_rule_events = current_rule_events + new_rule_events + historical_events + new_events
        all_events = merge_events(combined_rule_events, current_honeypot_events)

        # Filter events for the logged-in user only
        user_events = [e for e in all_events if e.get("user") == email]

        if not user_events:
            return jsonify({"message": "No events found for this user", "risk_score": 0, "risk_percent": 0, "timeline": [], "explanation": ""})

        # Calculate risk & timeline
        raw_risk = calculate_risk(user_events)
        risk_percent = min(max((raw_risk / MAX_RISK_SCORE) * 100, 0), 100)
        timeline = build_timeline(user_events)
        explanation = generate_explanation(raw_risk)

        # DEBUG
        print(f"🟢 User: {email}, Total events: {len(user_events)}, Risk: {raw_risk}, Risk%: {risk_percent}")

        return jsonify({
            "risk_score": raw_risk,
            "risk_percent": round(risk_percent, 2),
            "timeline": timeline,
            "explanation": explanation
        })

    except Exception as e:
        print(f"❌ Error in /analyze: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🔹 Starting Sentinel backend...")
    app.run(debug=True)