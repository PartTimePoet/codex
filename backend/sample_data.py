rule_events = [
    {"timestamp": "09:02", "event": "failed_login", "details": "5 failed attempts", "risk": 20},
    {"timestamp": "09:05", "event": "new_location", "details": "Login from Germany", "risk": 30}
]

honeypot_events = [
    {"timestamp": "09:07", "event": "honeypot_access", "details": "Accessed /admin-secret", "risk": 80}
]