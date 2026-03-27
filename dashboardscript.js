// LOGOUT
document.getElementById("logoutBtn").onclick = () => {
  localStorage.clear();
  window.location.href = "login.html";
};

// DROPDOWN
const icon = document.getElementById("profileIcon");
const dropdown = document.getElementById("profileDropdown");

icon.onclick = () => dropdown.classList.toggle("show");

window.onclick = (e) => {
  if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
    dropdown.classList.remove("show");
  }
};

// NAVIGATION
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}

// RISK SCORE LOGIC
const risk = 65;
const circle = document.getElementById("riskCircle");
const text = document.getElementById("riskText");

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