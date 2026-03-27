from flask import Flask, request, jsonify
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from sample_data import rule_events, honeypot_events
import json

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_post():
    data = request.json
    rule_events = data.get("rule_events", [])
    honeypot_events = data.get("honeypot_events", [])

    events = merge_events(rule_events, honeypot_events)
    risk = calculate_risk(events)
    timeline = build_timeline(events)
    explanation = generate_explanation(risk)

    return jsonify({
        "risk_score": risk,
        "timeline": timeline,
        "explanation": explanation
    })