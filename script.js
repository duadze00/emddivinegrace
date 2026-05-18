const openBtn = document.querySelector(".hamburger");
const closeBtn = document.querySelector(".close-btn");
const cover = document.querySelector("#cover");
const sideBar = document.querySelector(".sidebar");

function openSideBar() {
  sideBar.classList.add("open");
  cover.classList.add("cover-page");
  closeBtn.style.display = "block";
  openBtn.style.display = "none";
}

function closeSideBar() {
  sideBar.classList.remove("open");
  cover.classList.remove("cover-page");
  closeBtn.style.display = "none";
  openBtn.style.display = "block";
}

openBtn.addEventListener("click", openSideBar);
closeBtn.addEventListener("click", closeSideBar);
cover.addEventListener("click", closeSideBar);
