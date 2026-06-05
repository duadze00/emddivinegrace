// ==================================== HTML CONTENTS ====================================
const hamburgerBtn = document.querySelector(".navbar__item--hamburger");
const sideBar = document.querySelector(".side-bar__container");
const coverPage = document.querySelector(".overlay-cover");

// ==================================== FUNCTIONS ====================================
// Open function
function openSidebar() {
  sideBar.style.display = "block";
  coverPage.style.display = "block";
  hamburgerBtn.classList.add("active");
}

// Close function
function closeSidebar() {
  sideBar.style.display = "none";
  coverPage.style.display = "none";
  hamburgerBtn.classList.remove("active");
}

// ==================================== EVENT LISTENERS ====================================
// Hamburger
hamburgerBtn.addEventListener("click", () => {
  if (sideBar.style.display === "block") {
    closeSidebar();
  } else {
    openSidebar();
  }
});

// Coverpage
coverPage.addEventListener("click", closeSidebar);

// Reset hamburger when user maximize screen
window.addEventListener("resize", () => {
  if (window.innerWidth >= 768) {
    closeSidebar();
  }
});

// ==================================== USER SELECT DEFAULT COURSE ====================================
// Saving User Selected Course in Index.html and Using it Registration.html
document.querySelectorAll(".features__card--btn").forEach(btn => {
  btn.addEventListener("click", (e) => {
    const course = e.target.dataset.course;

    // store selected course
    localStorage.setItem("selectedCourse", course);
  });
});