// dashboard.js

document.addEventListener("DOMContentLoaded", function () {

  // ---------------- NAVBAR DROPDOWN ----------------
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

  // ---------------- PROFILE CARD CLICK ----------------
  const profileCard = document.getElementById("profileCard");
  if (profileCard) {
    profileCard.addEventListener("click", () => {
      window.location.href = "user-details.html";
    });
  }

  // ---------------- FETCH BACKEND DATA ----------------
  fetchRiskData();  // call backend on page load
});

// ---------------- NAVIGATION ----------------
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}

// ---------------- FETCH AND UPDATE FUNCTIONS ----------------
async function fetchRiskData() {
  try {
    // Replace with your backend API URL
    const response = await fetch("http://127.0.0.1:5000/analyze"); 
    const data = await response.json();

    updateRiskCircle(data.risk_score, data.explanation);
    updateTimeline(data.timeline);

  } catch (error) {
    console.error("Error fetching risk data:", error);
  }
}

// Update the risk circle
function updateRiskCircle(risk, explanation) {
  const circle = document.getElementById("riskCircle");
  const text = document.getElementById("riskText");

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

    // Optional: explanation display
    const explanationDiv = document.getElementById("riskExplanation");
    if (explanationDiv) {
      explanationDiv.innerText = explanation;
    }
  }
}

// Update the threat timeline
function updateTimeline(timeline) {
  const timelineDiv = document.getElementById("timeline");
  if (!timelineDiv) return;

  // Clear old timeline
  timelineDiv.innerHTML = "";

  timeline.forEach(event => {
    const p = document.createElement("p");
    p.innerText = event; // timeline items should already be strings like "09:02 – 5 failed logins"
    timelineDiv.appendChild(p);
  });
}