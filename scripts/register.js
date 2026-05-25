const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("user-email").value.trim();
  const password = document.getElementById("password").value.trim();
  const confirmPassword = document
    .getElementById("confirm_password")
    .value.trim();

  const phoneNumber = document.getElementById("user-number").value.trim();

  const dateOfBirth = document.getElementById("date-of-birth").value;

  const course = document.getElementById("course").value;

  /* ===================================== CHECK EMPTY INPUTS ===================================== */

  if (
    !username ||
    !email ||
    !password ||
    !confirmPassword ||
    !phoneNumber ||
    !dateOfBirth ||
    !course
  ) {
    alert("Please fill all fields");
    return;
  }

  /* ===================================== CHECK PASSWORD MATCH ===================================== */

  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return;
  }

  /* ===================================== SEND DATA TO SERVER ===================================== */

  try {
    const response = await fetch(
      "https://emddivinegrace.onrender.com/register",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username,
          email,
          password,
          confirmPassword,
          phoneNumber,
          dateOfBirth,
          course,
        }),
      },
    );

    const data = await response.json();

    if (!response.ok) {
      alert(data.message);
      return;
    }

    alert("Registration Successful");

    /* ===================================== REDIRECT BASED ON COURSE ===================================== */

    if (course === "sonography") {
      window.location.href = "../courses/scan/sonography.html";
    }

    if (course === "programming") {
      window.location.href = "../courses/development/programming.html";
    }

    if (course === "graphic_design") {
      window.location.href = "../courses/graphic_design/design.html";
    }
  } catch (error) {
    console.log(error);

    alert("Something went wrong");
  }
});
