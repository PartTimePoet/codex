def merge_events(rule_events, honeypot_events):
    events = rule_events + honeypot_events
    events.sort(key=lambda x: x["timestamp"])
    return events


def calculate_risk(events):
    total = 0
    for event in events:
        if event["event"] == "honeypot_access":
            total += event["risk"] * 1.5
        else:
            total += event["risk"]

    return min(int(total), 100)


def build_timeline(events):
    return [f"{e['timestamp']} – {e['details']}" for e in events]


def generate_explanation(risk):
    if risk > 80:
        return "🚨 Critical threat detected. Likely attacker behavior."
    elif risk > 50:
        return "⚠️ Suspicious activity detected."
    else:
        return "✅ Normal activity."