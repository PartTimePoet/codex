from flask import Flask, send_file, render_template_string, request, jsonify
from datetime import datetime
import json
import requests
import os

app = Flask(__name__)

# Person 3's risk engine endpoint (update when they share their URL)
RISK_ENGINE_URL = "http://localhost:5001/trap_alert"

def log_trap(request, trap_type):
    """Log when someone touches a trap and alert Person 3"""
    alert = {
        "timestamp": datetime.utcnow().isoformat(),
        "trap_type": trap_type,
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent", "unknown"),
        "path": request.path,
        "risk_score": 80
    }
    
    # Save to file
    with open("honeypot_alerts.log", "a") as f:
        f.write(json.dumps(alert) + "\n")
    
    print(f"\n🔥 TRAP TRIGGERED: {trap_type} from {request.remote_addr} (+80 risk)")
    
    # Send to Person 3's risk engine
    try:
        response = requests.post(RISK_ENGINE_URL, json=alert, timeout=2)
        print(f"✅ Alert sent to Risk Engine: {response.status_code}")
    except:
        print(f"⚠️ Risk Engine not reachable yet")
    
    return alert

# TRAP 1: Fake Admin Page
@app.route('/admin-secret')
def fake_admin():
    log_trap(request, "fake_admin_page")
    
    admin_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Portal</title>
        <style>
            body { 
                font-family: Arial; 
                background: #1e1e2f; 
                color: white; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh;
                margin: 0;
            }
            .login-box {
                background: #2a2a3a;
                padding: 40px;
                border-radius: 10px;
                width: 350px;
            }
            h2 { text-align: center; color: #ff6b6b; }
            input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: none;
                border-radius: 5px;
            }
            button {
                width: 100%;
                padding: 10px;
                background: #ff6b6b;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .warning {
                background: #ff5252;
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
                text-align: center;
                font-size: 12px;
            }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>Admin Control Panel</h2>
            <form>
                <input type="text" placeholder="Username">
                <input type="password" placeholder="Password">
                <button type="button">Login</button>
            </form>
            <div class="warning">
                Restricted Area - Authorized Personnel Only
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(admin_html)

# TRAP 2: Fake Salary File
@app.route('/files/salary_data.xlsx')
def fake_file():
    log_trap(request, "fake_salary_file")
    
    # Create a simple Excel file without pandas
    try:
        import openpyxl
        from openpyxl import Workbook
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Salaries"
        
        headers = ["Employee", "Department", "Salary", "Bonus"]
        data = [
            ["John Doe", "Engineering", 145000, 25000],
            ["Jane Smith", "Sales", 128000, 22000],
            ["Robert Chen", "IT", 175000, 35000],
            ["Sarah Williams", "HR", 95000, 12000],
            ["Admin User", "Executive", 250000, 50000]
        ]
        
        ws.append(headers)
        for row in data:
            ws.append(row)
        
        filename = "salary_data_demo.xlsx"
        wb.save(filename)
        
        return send_file(filename, as_attachment=True, download_name="confidential_salaries.xlsx")
    except:
        # Fallback if openpyxl not installed
        return "Salary file would be here", 403

# TRAP 3: Fake API Endpoint
@app.route('/api/v1/admin/config')
def fake_api():
    log_trap(request, "fake_api_endpoint")
    
    return jsonify({
        "status": "unauthorized",
        "message": "Authentication required",
        "server": "internal-prod-01",
        "database": {
            "host": "10.0.0.15",
            "port": 3306,
            "name": "corp_production"
        },
        "encryption": {
            "algorithm": "AES-256"
        }
    }), 401

# Status endpoint
@app.route('/honeypot/status')
def status():
    return jsonify({
        "system": "Deception System Active",
        "traps": ["admin_page", "salary_file", "api_endpoint"],
        "status": "ready"
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("DECEPTION SYSTEM ACTIVE")
    print("="*50)
    print("\nTraps:")
    print("  Admin Panel:    http://127.0.0.1:5000/admin-secret")
    print("  Salary File:    http://127.0.0.1:5000/files/salary_data.xlsx")
    print("  API Endpoint:   http://127.0.0.1:5000/api/v1/admin/config")
    print("\nAnyone accessing these = +80 risk points")
    print("Hits logged to: honeypot_alerts.log")
    print("\nServer starting...\n")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)