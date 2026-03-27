def detect_new_location(user, country, profiles):
    """
    Detects if the user logs in from a country different than their usual one.
    """
    if country != profiles[user]["usual_country"]:
        return {
            "alert": "New country login detected",
            "risk": 30
        }
    return None