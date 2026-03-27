# utils/profile_builder.py
from collections import Counter

def build_profiles(logs):
    profiles = {}

    for log in logs:
        user = log["user"]

        if user not in profiles:
            profiles[user] = {
                "countries": [],
                "hours": [],
                "browsers": [],
                "resources": [],
                "failed_logins": []
            }

        profiles[user]["countries"].append(log["country"])
        profiles[user]["hours"].append(log["login_hour"])
        profiles[user]["browsers"].append(log["browser"])
        profiles[user]["resources"].append(log["resource"])
        profiles[user]["failed_logins"].append(log["failed_logins"])

    final_profiles = {}
    for user, data in profiles.items():
        final_profiles[user] = {
            "usual_country": Counter(data["countries"]).most_common(1)[0][0],
            "usual_browser": Counter(data["browsers"]).most_common(1)[0][0],
            "usual_login_hours": list(set(data["hours"])),
            "usual_resources": list(set(data["resources"])),
            "average_failed_logins": sum(data["failed_logins"]) / len(data["failed_logins"])
        }

    return final_profiles