import json
import random
from datetime import datetime, timedelta
import os

# -------------------------------
# Setup paths to ensure correct folder
# -------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# -------------------------------
# Users and options
# -------------------------------
users = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack"]

countries = ["Tokyo", "Osaka", "Singapore", "New York", "London"]
browsers = ["Chrome", "Firefox", "Edge", "Safari"]
resources = ["file1", "file2", "admin_panel", "confidential_doc", "project_data"]

def random_hour(base):
    return (base + random.randint(-2, 2)) % 24

historical_logs = []
new_logs = []

# -------------------------------
# Generate logs per user
# -------------------------------
for user in users:
    usual_country = random.choice(countries)
    usual_browser = random.choice(browsers)
    usual_hours = [random.randint(7, 22) for _ in range(5)]

    # Historical logs (learning)
    for _ in range(30):
        log = {
            "user": user,
            "timestamp": (datetime.now() - timedelta(days=random.randint(1,30))).strftime("%Y-%m-%d %H:%M:%S"),
            "country": usual_country,
            "browser": usual_browser,
            "login_hour": random.choice(usual_hours),
            "resource": random.choice(resources),
            "failed_logins": random.randint(0, 2)
        }
        historical_logs.append(log)
    
    # New activity (today)
    anomaly = random.random() < 0.3  # 30% chance
    new_country = random.choice(countries) if anomaly else usual_country
    new_browser = random.choice(browsers) if anomaly else usual_browser
    failed_logins = random.randint(5,12) if anomaly else random.randint(0,2)
    new_hour = random_hour(random.choice(usual_hours))
    new_resource = random.choice(resources)

    new_log = {
        "user": user,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "country": new_country,
        "browser": new_browser,
        "login_hour": new_hour,
        "resource": new_resource,
        "failed_logins": failed_logins
    }
    new_logs.append(new_log)

# -------------------------------
# Save to data folder
# -------------------------------
with open(os.path.join(DATA_DIR, "historical_logs.json"), "w") as f:
    json.dump(historical_logs, f, indent=4)

with open(os.path.join(DATA_DIR, "new_logs.json"), "w") as f:
    json.dump(new_logs, f, indent=4)

print("✅ Demo logs generated for 10 users with anomalies!")