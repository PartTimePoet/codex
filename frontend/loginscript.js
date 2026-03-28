document.getElementById("loginBtn").addEventListener("click", () => {
    const email = document.getElementById("emailInput").value.trim();
    const password = document.getElementById("passwordInput").value.trim();

    // Basic validation
    if (!email || !password) {
        alert("Please enter both email and password.");
        return;
    }

    // Example: check against your users.json or backend
    fetch("http://localhost:5000/login", { // You can create a /login route
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => {
        if(data.success){
            // Store email in sessionStorage for dashboard
            sessionStorage.setItem("email", email);

            // Redirect to dashboard
            window.location.href = "dashboard.html";
        } else {
            alert("Invalid email or password.");
        }
    })
    .catch(err => {
        console.error("Login error:", err);
        alert("Error connecting to server.");
    });
});