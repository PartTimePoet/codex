document.addEventListener("DOMContentLoaded", function () {

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

  // ✅ PROFILE CARD CLICK (FIXED)
  const profileCard = document.getElementById("profileCard");
  if (profileCard) {
    profileCard.addEventListener("click", () => {
      window.location.href = "user-details.html";
    });
  }

  // RISK SCORE DYNAMIC UPDATER
  const circle = document.getElementById("riskCircle");
  const text = document.getElementById("riskText");

  async function updateRisk() {
    try {
      const response = await fetch("http://127.0.0.1:5000/analyze"); // Flask backend endpoint
      const data = await response.json();
      const risk = data.risk_score;

      if (circle && text) {
        circle.innerText = risk;

        if (risk < 40) {
          circle.style.background = "green";
          text.innerText = "Low risk";
        } else if (risk < 70) {
          circle.style.background = "orange";
          text.innerText = "Moderate risk";
        } else {
          circle.style.background = "red";
          text.innerText = "High risk";
        }
      }

      // Optional: Log timeline to console for now
      console.log("Threat Timeline:", data.timeline);
      console.log("Explanation:", data.explanation);

    } catch (error) {
      console.error("Error fetching risk data:", error);
    }
  }

  // Initial fetch
  updateRisk();
  // Fetch every 5 seconds
  setInterval(updateRisk, 5000);
});

// NAVIGATION FUNCTIONS
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}