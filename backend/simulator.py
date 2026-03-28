# simulator.py
import threading
import time
import random
from datetime import datetime

# Shared lists
current_rule_events = []
current_honeypot_events = []

# Sample events
rule_samples = [
    "login from new country",
    "too many login attempts",
    "accessed restricted file"
]

honeypot_samples = [
    "accessed fake admin page",
    "accessed fake salary file",
    "hit fake API endpoint"
]

def generate_events():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Rule event
        rule_event = {
            "type": "rule",
            "description": random.choice(rule_samples),
            "timestamp": timestamp
        }

        # Honeypot event
        honeypot_event = {
            "type": "honeypot",
            "description": random.choice(honeypot_samples),
            "timestamp": timestamp
        }

        current_rule_events.append(rule_event)
        current_honeypot_events.append(honeypot_event)

        # Keep only last 50 events
        if len(current_rule_events) > 50:
            current_rule_events.pop(0)
        if len(current_honeypot_events) > 50:
            current_honeypot_events.pop(0)

        print(f"[RULE] {rule_event['description']} | [HONEYPOT] {honeypot_event['description']}")
        time.sleep(5)

# Start simulator in a separate thread
threading.Thread(target=generate_events, daemon=True).start()