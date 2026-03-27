document.addEventListener("DOMContentLoaded", () => {

  const list = document.getElementById("anomalyList");
  const details = document.getElementById("detailsPanel");

  // NAVBAR DROPDOWN
  const icon = document.getElementById("profileIcon");
  const dropdown = document.getElementById("profileDropdown");

  icon.onclick = () => dropdown.classList.toggle("show");

  window.onclick = (e) => {
    if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.remove("show");
    }
  };

  document.getElementById("logoutBtn").onclick = () => {
    localStorage.clear();
    window.location.href = "login.html";
  };

  // NAVIGATION
  window.goToUserDetails = () => window.location.href = "user-details.html";
  window.goToSettings = () => window.location.href = "settings.html";

  // Render anomalies dynamically
  async function updateAnomalies() {
    try {
      const response = await fetch("http://127.0.0.1:5000/analyze");
      const data = await response.json();

      // Clear existing list
      list.innerHTML = "";

      // Use timeline events as anomalies
      data.timeline.forEach((eventStr, index) => {
        // Determine severity from risk contribution
        let severity = "low";
        if (data.risk_score > 80) severity = "high";
        else if (data.risk_score > 50) severity = "medium";

        const div = document.createElement("div");
        div.className = `anomaly-card ${severity}`;
        div.innerHTML = `
          <h3>⚠ Anomaly Detected</h3>
          <p>${eventStr}</p>
          <p>Severity: ${severity.toUpperCase()}</p>
        `;

        div.addEventListener("click", () => {
          details.innerHTML = `
            <h2>🔍 Anomaly Details</h2>
            <p><strong>Event:</strong> ${eventStr}</p>
            <p><strong>Severity:</strong> ${severity}</p>
            <p><strong>Explanation:</strong> ${data.explanation}</p>
            <div class="actions">
              <button class="confirm">✅ Confirm</button>
              <button class="report">❌ Report</button>
            </div>
          `;
        });

        list.appendChild(div);
      });

    } catch (error) {
      console.error("Error fetching anomalies:", error);
    }
  }

  // Initial fetch and refresh every 5 seconds
  updateAnomalies();
  setInterval(updateAnomalies, 5000);

});