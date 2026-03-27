// ==========================
// LOGOUT
// ==========================
const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {
  logoutBtn.addEventListener("click", function () {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    window.location.href = "login.html";
  });
}

// ==========================
// PROFILE DROPDOWN
// ==========================
const profileIcon = document.getElementById("profileIcon");
const profileDropdown = document.getElementById("profileDropdown");

profileIcon.addEventListener("click", () => {
  profileDropdown.classList.toggle("show");
});

// CLOSE WHEN CLICK OUTSIDE
window.addEventListener("click", function(e) {
  if (!profileIcon.contains(e.target) && !profileDropdown.contains(e.target)) {
    profileDropdown.classList.remove("show");
  }
});

// ==========================
// NAVIGATION
// ==========================
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}
