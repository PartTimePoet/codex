import threading
import time
import random
from datetime import datetime

# Shared lists for current events
current_rule_events = []
current_honeypot_events = []

# Sample events
rule_samples = [
    {"description": "login from new country", "risk": 20},
    {"description": "too many login attempts", "risk": 25},
    {"description": "accessed restricted file", "risk": 30}
]

honeypot_samples = [
    {"description": "accessed fake admin page", "risk": 40},
    {"description": "accessed fake salary file", "risk": 50},
    {"description": "hit fake API endpoint", "risk": 35}
]

def generate_events():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create dict events for rules
        rule_event_sample = random.choice(rule_samples)
        rule_event = {
            "type": "rule",
            "description": rule_event_sample["description"],
            "timestamp": timestamp,
            "risk": rule_event_sample["risk"]
        }

        # Create dict events for honeypots
        honeypot_event_sample = random.choice(honeypot_samples)
        honeypot_event = {
            "type": "honeypot",
            "description": honeypot_event_sample["description"],
            "timestamp": timestamp,
            "risk": honeypot_event_sample["risk"]
        }

        # Add to shared lists
        current_rule_events.append(rule_event)
        current_honeypot_events.append(honeypot_event)

        # Keep only last 10 events
        if len(current_rule_events) > 10:
            current_rule_events.pop(0)
        if len(current_honeypot_events) > 10:
            current_honeypot_events.pop(0)

        print(f"[RULE] {rule_event['description']} | [HONEYPOT] {honeypot_event['description']}")
        time.sleep(5)  # generate every 5 seconds

# Start simulator in background thread
threading.Thread(target=generate_events, daemon=True).start()