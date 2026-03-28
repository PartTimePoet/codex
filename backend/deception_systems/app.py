from flask import Flask, request, redirect, url_for, render_template_string, jsonify, send_file
import datetime
import os
from openpyxl import Workbook


from flask import render_template
import random


app = Flask(__name__)   # 👈 THIS MUST BE BEFORE ANY @app.route


@app.route("/admin-secret")
def fake_admin():
    trap_alert("Fake Admin Page Access")


    hacker_score = 75


    return render_template(
        "honeypot.html",
        ip=request.remote_addr,
        hacker_score=hacker_score,
        risk_percent=(hacker_score / 80) * 100,
        user_agent=request.headers.get("User-Agent", "Unknown"),
        session_id="TRACKED",
        attempt_count=request.cookies.get("trap_triggered", "1"),
        incident_id=f"INC-{random.randint(10000,99999)}"
    )




app = Flask(__name__)


# 🚨 Trap alert function
def trap_alert(trap_name):
    ip = request.remote_addr
    time = datetime.datetime.now()


    print("\n🚨 HONEYPOT ALERT 🚨")
    print(f"Trap Triggered: {trap_name}")
    print(f"IP Address: {ip}")
    print(f"Time: {time}")
    print("Risk Score: HIGH 🔥\n")


# 🏠 Normal homepage
@app.route("/")
def home():
    return """
    <h2>Welcome 👋</h2>
    <p>Nothing to see here...</p>
    """


# 🚨 Suspicious behavior trigger → redirect to honeypot
@app.route("/suspicious")
def suspicious():
    trap_alert("Suspicious Activity Detected")
    return redirect(url_for('fake_admin'))


# 🪤 Fake admin login page
@app.route("/admin-secret", methods=["GET", "POST"])
def fake_admin():
    trap_alert("Fake Admin Page Access")


    fake_html = """
    <html>
    <head>
        <title>Admin Login</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h2>🔐 Admin Panel</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" /><br><br>
            <input type="password" name="password" placeholder="Password" /><br><br>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    """


    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        print("🎯 CREDENTIAL TRAP HIT 🎯")
        print(f"Username: {username}")
        print(f"Password: {password}\n")


        return "Login failed ❌"


    return render_template_string(fake_html)


# 💰 Honeypot file (fake salary data)
@app.route("/salary_data.xlsx")
def honeypot_file():
    trap_alert("Honeypot File Access - salary_data.xlsx")


    file_path = "fake_salary_data.xlsx"


    # Create real Excel file if not exists
    if not os.path.exists(file_path):
        wb = Workbook()
        ws = wb.active
        ws.append(["Employee", "Salary"])
        ws.append(["John", 100000])
        ws.append(["Alice", 120000])
        ws.append(["Bob", 90000])
        wb.save(file_path)


    return send_file(file_path, as_attachment=True)


# 🎛️ Fake API endpoint
@app.route("/api/hidden")
def fake_api():
    trap_alert("Fake API Endpoint Access")
    return jsonify({"error": "Unauthorized access ❌"})


# ▶️ Run server
if __name__ == "__main__":
    app.run(debug=True)