def detect_unauthorized_access(user, resource, profiles):
    if resource not in profiles[user]["usual_resources"]:
        return {
            "alert": "Unauthorized resource access",
            "risk": 25
                 }
    return None