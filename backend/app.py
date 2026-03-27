# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from sample_data import rule_events, honeypot_events

app = Flask(__name__)
CORS(app)  # allow dashboard/frontend to fetch

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        data = request.json or {}
        rule_events_post = data.get("rule_events", [])
        honeypot_events_post = data.get("honeypot_events", [])
        events = merge_events(rule_events_post, honeypot_events_post)
    else:
        # For GET requests (like dashboard fetch), use sample data
        events = merge_events(rule_events, honeypot_events)

    risk = calculate_risk(events)
    timeline = build_timeline(events)
    explanation = generate_explanation(risk)

    return jsonify({
        "risk_score": risk,
        "timeline": timeline,
        "explanation": explanation
    })


if __name__ == "__main__":
    # Run Flask app on localhost:5000
    app.run(debug=True)