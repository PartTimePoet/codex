document.addEventListener("DOMContentLoaded", () => {
    const circle = document.getElementById("riskCircle");
    const text = document.getElementById("riskText");
    const anomalyList = document.getElementById("anomalyList");
    const details = document.getElementById("detailsPanel");

    const icon = document.getElementById("profileIcon");
    const dropdown = document.getElementById("profileDropdown");

    icon.onclick = () => dropdown.classList.toggle("show");
    window.onclick = (e) => {
        if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.classList.remove("show");
        }
    };

    document.getElementById("logoutBtn").onclick = () => {
        sessionStorage.clear();
        window.location.href = "login.html";
    };

    window.goToUserDetails = () => window.location.href = "user-details.html";
    window.goToSettings = () => window.location.href = "settings.html";

    const email = sessionStorage.getItem("email");
    if(!email){
        // Not logged in, redirect to login
        window.location.href = "login.html";
    }

    async function updateDashboard() {
        try {
            const response = await fetch("http://127.0.0.1:5000/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email })
            });

            const data = await response.json();
            if(data.error){
                console.error(data.error);
                return;
            }

            const risk = data.risk_score;

            if(circle && text){
                circle.innerText = risk;
                if(risk < 40){
                    circle.style.background = "green";
                    text.innerText = "Low risk";
                } else if(risk < 70){
                    circle.style.background = "orange";
                    text.innerText = "Moderate risk";
                } else {
                    circle.style.background = "red";
                    text.innerText = "High risk";
                }
            }

            // Clear old anomalies
            anomalyList.innerHTML = "";

            data.anomalies.forEach((eventStr) => {
                const div = document.createElement("div");
                // Simple severity: based on risk
                let severity = "low";
                if(risk > 80) severity = "high";
                else if(risk > 50) severity = "medium";

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

                anomalyList.appendChild(div);
            });

        } catch(err){
            console.error("Dashboard fetch error:", err);
        }
    }

    updateDashboard();
    setInterval(updateDashboard, 5000);
});