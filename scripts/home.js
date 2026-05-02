const toggleBtn = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

toggleBtn.addEventListener("click", () => {
  navLinks.classList.toggle("mobile-active");

  if (navLinks.classList.contains("mobile-active")) {
    toggleBtn.textContent = "✕";
  } else {
    toggleBtn.textContent = "☰";
  }
});
document.addEventListener("click", (e) => {
  if (!e.target.closest(".nav")) {
    navLinks.classList.remove("mobile-active");
  }
});
