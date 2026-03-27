# run_demo.py
import subprocess
import sys
import os

backend_dir = os.path.dirname(os.path.abspath(__file__))

# Start Flask backend
print("🚀 Starting backend (Flask)...")
backend_proc = subprocess.Popen([sys.executable, "app.py"], cwd=backend_dir)

print("✅ Backend running. Simulator is already part of backend.")

try:
    backend_proc.wait()  # Keep backend running
except KeyboardInterrupt:
    print("🛑 Stopping demo...")
    backend_proc.terminate()