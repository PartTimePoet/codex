# app.py
from flask import Flask, jsonify
from risk_engine import merge_events, calculate_risk, build_timeline, generate_explanation
from simulator import current_rule_events, current_honeypot_events  # import shared lists

app = Flask(__name__)

# Enable CORS if frontend is served differently
from flask_cors import CORS
CORS(app)

@app.route("/analyze", methods=["GET"])
def analyze():
    events = merge_events(current_rule_events, current_honeypot_events)
    risk = calculate_risk(events)
    timeline = build_timeline(events)
    explanation = generate_explanation(risk)
    return jsonify({
        "risk_score": risk,
        "timeline": timeline,
        "explanation": explanation
    })

if __name__ == "__main__":
    print("🔹 Starting Sentinel backend...")
    app.run(debug=True)