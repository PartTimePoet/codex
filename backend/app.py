# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import json
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from simulator import current_rule_events, current_honeypot_events
from rules.all_rules import apply_all_rules  # your rules

app = Flask(__name__)
CORS(app)

# Load users
with open("users.json") as f:
    users = json.load(f)  # [{"email": "alice124@gmail.com", "password": "Alice@123"}, ...]

# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    user = next((u for u in users if u["email"] == email and u["password"] == password), None)
    if user:
        return jsonify({"success": True})
    return jsonify({"success": False})


# Paths to JSON logs
DATA_DIR = Path(__file__).parent / "data"
HISTORICAL_FILE = DATA_DIR / "historical_logs.json"
NEW_FILE = DATA_DIR / "new_logs.json"

def load_json_events(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠ Failed to load {file_path.name}: {e}")
        return []

def json_to_events(json_logs):
    events = []
    for e in json_logs:
        desc = f"{e['user']} logged in from {e['country']} using {e['browser']} at hour {e['login_hour']} accessing {e['resource']} (failed: {e['failed_logins']})"
        events.append({
            "type": "rule",
            "description": desc,
            "timestamp": e["timestamp"],
            "user": e["user"],                  # crucial for filtering by login
            "is_anomaly": True  # default True if not specified
        })
    return events


# Analyze route – expects POST with {"email": "<user email>"}
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        email = data.get("email")

        # Load historical and new events
        historical_events = json_to_events(load_json_events(HISTORICAL_FILE))
        new_events = json_to_events(load_json_events(NEW_FILE))
        new_rule_events = apply_all_rules(current_rule_events)

        # Merge events
        combined_rule_events = current_rule_events + new_rule_events + historical_events + new_events
        all_events = merge_events(combined_rule_events, current_honeypot_events)

        # Calculate risk and timeline
        risk = calculate_risk(all_events)
        timeline = build_timeline(all_events)
        explanation = generate_explanation(risk)

        # Filter anomalies for logged-in user
        anomalies = [e["description"] for e in all_events if e.get("user") == email and e.get("is_anomaly")]

        return jsonify({
            "risk_score": risk,
            "risk_percent": min(int(risk), 100),
            "timeline": timeline,
            "anomalies": anomalies,
            "explanation": explanation
        })

    except Exception as e:
        print(f"❌ Error in /analyze: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🔹 Starting Sentinel backend...")
    app.run(debug=True)