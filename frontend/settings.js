document.addEventListener("DOMContentLoaded", () => {

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

// CHANGE PASSWORD
function changePassword() {
  const current = document.getElementById("currentPassword").value;
  const newPass = document.getElementById("newPassword").value;
  const confirm = document.getElementById("confirmPassword").value;

  if (!current || !newPass || !confirm) {
    alert("Please fill all fields");
    return;
  }

  if (newPass !== confirm) {
    alert("Passwords do not match");
    return;
  }

  alert("Password updated successfully (demo)");
}

// UPDATE EMAIL
function updateEmail() {
  const email = document.getElementById("secondaryEmail").value;

  if (!email) {
    alert("Enter a valid email");
    return;
  }

  alert("Secondary email updated (demo)");
}

// NAVIGATION
function goToUserDetails() {
  window.location.href = "user-details.html";
}

function goToSettings() {
  window.location.href = "settings.html";
}