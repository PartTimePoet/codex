document.addEventListener("DOMContentLoaded", function () {

  // LOGOUT
  const logoutBtn = document.getElementById("logoutBtn");
  if (logoutBtn) {
    logoutBtn.onclick = () => {
      localStorage.clear();
      window.location.href = "login.html";
    };
  }

  // DROPDOWN
  const icon = document.getElementById("profileIcon");
  const dropdown = document.getElementById("profileDropdown");

  if (icon && dropdown) {
    icon.onclick = () => dropdown.classList.toggle("show");

    window.addEventListener("click", (e) => {
      if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove("show");
      }
    });
  }

  // ✅ PROFILE CARD CLICK (THIS IS THE FIX)
  const profileCard = document.getElementById("profileCard");

  if (profileCard) {
    profileCard.addEventListener("click", () => {
      window.location.href = "user-details.html";
    });
  } else {
    console.error("profileCard NOT FOUND");
  }

  // RISK SCORE
  const risk = 65;
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
  }

});