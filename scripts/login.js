const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("user-email").value.trim();
  const password = document.getElementById("password").value.trim();

  // 1. Validate empty fields
  if (!email || !password) {
    alert("Please fill all fields");
    return;
  }

  try {
    const response = await fetch("https://emddivinegrace.onrender.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        password,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      alert(data.message);
      return;
    }

    // Save token (important for future authentication)
    localStorage.setItem("token", data.token);

    alert("Login successful");

    // Redirect based on course
    if (data.course === "sonography") {
      window.location.href = "../courses/scan/sonography.html";
    }

    if (data.course === "programming") {
      window.location.href = "../courses/development/programming.html";
    }

    if (data.course === "graphic_design") {
      window.location.href = "../courses/graphic_design/design.html";
    }
  } catch (error) {
    console.log(error);
    alert("Server error");
  }
});
