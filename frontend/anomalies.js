document.addEventListener("DOMContentLoaded", () => {

  // SAMPLE DATA
  const anomalies = [
    {
      type: "Login",
      user: "Employee_01",
      location: "Brazil",
      time: "10:45 AM",
      severity: "high",
      reason: "Unusual location login"
    },
    {
      type: "File Access",
      user: "Employee_02",
      location: "India",
      time: "11:10 AM",
      severity: "medium",
      reason: "Accessed sensitive file"
    },
    {
      type: "Login",
      user: "Employee_03",
      location: "Russia",
      time: "12:00 PM",
      severity: "high",
      reason: "Multiple failed attempts"
    }
  ];

  const list = document.getElementById("anomalyList");
  const details = document.getElementById("detailsPanel");

  // RENDER ANOMALIES
  anomalies.forEach((a, index) => {
    const div = document.createElement("div");
    div.className = `anomaly-card ${a.severity}`;

    div.innerHTML = `
      <h3>⚠ ${a.type} Anomaly</h3>
      <p>User: ${a.user}</p>
      <p>Location: ${a.location}</p>
      <p>Time: ${a.time}</p>
      <p>Severity: ${a.severity.toUpperCase()}</p>
    `;

    div.addEventListener("click", () => {
      details.innerHTML = `
        <h2>🔍 Anomaly Details</h2>
        <p><strong>Type:</strong> ${a.type}</p>
        <p><strong>User:</strong> ${a.user}</p>
        <p><strong>Location:</strong> ${a.location}</p>
        <p><strong>Time:</strong> ${a.time}</p>
        <p><strong>Severity:</strong> ${a.severity}</p>
        <p><strong>Reason:</strong> ${a.reason}</p>

        <div class="actions">
          <button class="confirm">✅ Confirm</button>
          <button class="report">❌ Report</button>
        </div>
      `;
    });

    list.appendChild(div);
  });

  // NAVBAR DROPDOWN
  const icon = document.getElementById("profileIcon");
  const dropdown = document.getElementById("profileDropdown");

  icon.onclick = () => dropdown.classList.toggle("show");

  window.onclick = (e) => {
    if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.remove("show");
    }
  };

  // LOGOUT
  document.getElementById("logoutBtn").onclick = () => {
    localStorage.clear();
    window.location.href = "login.html";
  };

});

// NAVIGATION
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}