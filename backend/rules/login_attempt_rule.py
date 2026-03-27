def detect_failed_logins(user, failed_logins, profiles):
    average = profiles[user]["average_failed_logins"]

    if failed_logins > average + 5:
        return {
            "alert": "Too many failed login attempts",
            "risk": 20
        }

    return None