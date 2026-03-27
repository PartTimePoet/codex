# risk_engine.py
def merge_events(rule_events, honeypot_events):
    events = rule_events + honeypot_events
    events.sort(key=lambda x: x["timestamp"])
    return events

def calculate_risk(events):
    total = 0
    for event in events:
        # Assign risk values based on type
        if event["type"] == "honeypot":
            total += 20  # honeypot access is higher risk
        else:
            total += 10  # normal rule events
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