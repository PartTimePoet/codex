def detect_unusual_login_time(user, login_hour, profiles):
    if login_hour not in profiles[user]["usual_login_hours"]:
        return {
            "alert": "Unusual login hour",
            "risk": 15
        }

    return None