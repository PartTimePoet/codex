// anomalies.js
document.addEventListener("DOMContentLoaded", () => {

  const list = document.getElementById("anomalyList");
  const details = document.getElementById("detailsPanel");

  // FETCH LIVE ANOMALIES FROM BACKEND
  async function fetchAnomalies() {
    try {
      const response = await fetch("http://127.0.0.1:5000/analyze");
      const data = await response.json();

      // data.timeline is an array of events
      renderAnomalies(data.timeline);
    } catch (error) {
      console.error("Error fetching anomalies:", error);
    }
  }

  function renderAnomalies(events) {
    list.innerHTML = ""; // clear old anomalies

    events.forEach((event, index) => {
      // Map backend event to severity
      const severity = event.toLowerCase().includes("fake") || event.toLowerCase().includes("failed") ? "high" : "medium";

      const div = document.createElement("div");
      div.className = `anomaly-card ${severity}`;

      div.innerHTML = `
        <h3>⚠ Anomaly</h3>
        <p>Event: ${event}</p>
        <p>Severity: ${severity.toUpperCase()}</p>
      `;

      div.addEventListener("click", () => {
        details.innerHTML = `
          <h2>🔍 Anomaly Details</h2>
          <p><strong>Event:</strong> ${event}</p>
          <p><strong>Severity:</strong> ${severity}</p>

          <div class="actions">
            <button class="confirm">✅ Confirm</button>
            <button class="report">❌ Report</button>
          </div>
        `;
      });

      list.appendChild(div);
    });
  }

  // Initial fetch
  fetchAnomalies();

  // Auto-refresh every 5 seconds
  setInterval(fetchAnomalies, 5000);

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