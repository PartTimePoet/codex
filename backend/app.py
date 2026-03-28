# app.py
from flask import Flask, jsonify
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
            "timestamp": e["timestamp"]
        })
    return events

@app.route("/analyze", methods=["GET"])
def analyze():
    try:
        # Load JSON logs
        historical_events = json_to_events(load_json_events(HISTORICAL_FILE))
        new_events = json_to_events(load_json_events(NEW_FILE))

        # Apply person1 rules to simulator events
        new_rule_events = apply_all_rules(current_rule_events)

        # Merge all events
        combined_rule_events = current_rule_events + new_rule_events + historical_events + new_events
        all_events = merge_events(combined_rule_events, current_honeypot_events)

        # Calculate risk & timeline
        risk = calculate_risk(all_events)
        timeline = build_timeline(all_events)
        explanation = generate_explanation(risk)

        # DEBUG
        print(f"🟢 Total events: {len(all_events)}, Risk: {risk}")

        return jsonify({
            "risk_score": risk,
            "timeline": timeline,
            "explanation": explanation
        })

    except Exception as e:
        print(f"❌ Error in /analyze: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🔹 Starting Sentinel backend...")
    app.run(debug=True)