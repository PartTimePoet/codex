# rules/all_rules.py
from .access_rule import detect_unauthorized_access
from .browser_rule import detect_new_browser
from .location_rule import detect_new_location
from .login_attempt_rule import detect_failed_logins
from .login_time_rule import detect_unusual_login_time

# rules/all_rules.py
def apply_all_rules(events):
    # events: list of dicts with at least keys 'type', 'description', 'timestamp'
    new_events = []
    for event in events:
        # Example: if the event is login_attempt, add some derived event
        if "login" in event["description"]:
            new_events.append({
                "type": "rule",
                "description": "additional login rule triggered",
                "timestamp": event["timestamp"]
            })
    return new_events