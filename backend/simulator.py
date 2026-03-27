# simulator.py
import time
import random
from sample_data import rule_events, honeypot_events

# Live events lists
current_rule_events = list(rule_events)        # start with sample rule events
current_honeypot_events = list(honeypot_events)  # start with sample honeypot events

# Sample events for simulation
sample_rule_events = [
    "Login from new country",
    "Too many login attempts",
    "Accessed restricted file",
]

sample_honeypot_events = [
    "Opened fake admin page",
    "Accessed fake salary file",
    "Hit fake API endpoint",
]

def add_random_event():
    """
    Randomly choose a rule or honeypot event and add it to live events.
    """
    if random.random() < 0.6:  # 60% chance to add rule event
        event = random.choice(sample_rule_events)
        current_rule_events.append(event)
        print(f"[RULE] {event}")
    else:
        event = random.choice(sample_honeypot_events)
        current_honeypot_events.append(event)
        print(f"[HONEYPOT] {event}")

if __name__ == "__main__":
    print("🚨 Starting attack simulator...")
    while True:
        add_random_event()
        time.sleep(random.randint(3, 6))  # generate a new event every 3–6 seconds