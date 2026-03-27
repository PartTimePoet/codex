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