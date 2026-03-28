# risk_manager.py

from datetime import datetime

# risk_engine.py
def merge_events(rule_events, honeypot_events):
    events = rule_events + honeypot_events
    # sort by timestamp
    events.sort(key=lambda x: x["timestamp"])
    return events

def calculate_risk(events):
    total = 0
    for event in events:
        # Assign risk values based on type
        if event.get("type") == "honeypot":
            total += 20  # higher risk
        else:
            # factor failed logins or resources
            desc = event.get("description", "")
            if "failed: 0" in desc:
                total += 5
            elif "failed: 1" in desc:
                total += 10
            elif "failed: 2" in desc:
                total += 15
            else:
                total += 10
    return min(total, 100)

def build_timeline(events):
    return [f"{e['timestamp']} – {e['description']}" for e in events]

def generate_explanation(risk):
    if risk > 80:
        return "🚨 Critical threat detected. Likely attacker behavior."
    elif risk > 50:
        return "⚠️ Suspicious activity detected."
    else:
        return "✅ Normal activity."