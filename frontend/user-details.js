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

// SAMPLE USER DATA (replace with real data later)
const user = {
  username: "ExampleUser",
  email: "example@example.com",
  company: "ExampleCorp",
  attendance: 78
};

// SET DATA
document.getElementById("username").innerText = user.username;
document.getElementById("email").innerText = user.email;
document.getElementById("company").innerText = user.company;

// CUSTOM PLUGIN FOR CENTER TEXT
const centerTextPlugin = {
  id: 'centerText',
  beforeDraw(chart) {
    const { width } = chart;
    const { height } = chart;
    const ctx = chart.ctx;

    ctx.restore();

    const fontSize = (height / 120).toFixed(2);
    ctx.font = `${fontSize}em Raleway`;
    ctx.textBaseline = "middle";
    ctx.fillStyle = "#67FFF2"; // neon cyan

    const text = user.attendance + "%";
    const textX = Math.round((width - ctx.measureText(text).width) / 2);
    const textY = height / 2;

    ctx.fillText(text, textX, textY);
    ctx.save();
  }
};

// CHART
const ctx = document.getElementById('attendanceChart').getContext('2d');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [user.attendance, 100 - user.attendance],
      backgroundColor: [
        '#67FFF2',
        '#446B5C'
      ],
      borderWidth: 0
    }]
  },
  options: {
    cutout: '75%',
    plugins: {
      legend: {
        display: false
      }
    }
  },
  plugins: [centerTextPlugin]
});