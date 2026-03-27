# run_demo.py
import subprocess
import sys
import os

# Paths
backend_dir = os.path.dirname(os.path.abspath(__file__))

# Start Flask backend
print("🚀 Starting backend...")
backend_proc = subprocess.Popen([sys.executable, "app.py"], cwd=backend_dir)

# Start simulator
print("🎯 Starting simulator...")
sim_proc = subprocess.Popen([sys.executable, "simulator.py"], cwd=backend_dir)

print("✅ Demo running. Open dashboard.html and anomalies.html in your browser.")

try:
    # Wait for both processes
    backend_proc.wait()
    sim_proc.wait()
except KeyboardInterrupt:
    print("Stopping demo...")
    backend_proc.terminate()
    sim_proc.terminate()