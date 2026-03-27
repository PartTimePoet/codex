document.addEventListener("DOMContentLoaded", () => {

  // SAMPLE DATA
  const data = {
    total: 22,
    high: 8,
    resolved: 12,
    trend: [2, 4, 6, 5, 8, 10, 12]
  };

  // UPDATE CARDS
  document.getElementById("totalAnomalies").innerText = data.total;
  document.getElementById("highRisk").innerText = data.high;
  document.getElementById("resolved").innerText = data.resolved;

  // CHART
  const ctx = document.getElementById("reportChart");

  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      datasets: [{
        label: "Anomalies Detected",
        data: data.trend,
        borderColor: "#22d3ee",
        backgroundColor: "rgba(34, 211, 238, 0.2)",
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      plugins: {
        legend: {
          labels: {
            color: "white"
          }
        }
      },
      scales: {
        x: {
          ticks: { color: "white" }
        },
        y: {
          ticks: { color: "white" }
        }
      }
    }
  });

  // DROPDOWN
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

// DOWNLOAD REPORT
function downloadReport() {
  const content = `
Sentinel Security Report

Total Anomalies: 22
High Risk: 8
Resolved: 12
  `;

  const blob = new Blob([content], { type: "text/plain" });
  const link = document.createElement("a");

  link.href = URL.createObjectURL(blob);
  link.download = "report.txt";
  link.click();
}

// NAVIGATION
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}