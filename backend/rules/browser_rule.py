def detect_new_browser(user, browser, profiles):
    if browser != profiles[user]["usual_browser"]:
        return {
            "alert": "New browser detected",
            "risk": 10
        }

    return None