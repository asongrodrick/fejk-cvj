// Contact form (demo only)
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();
  alert("Thank you for reaching out! I will get back to you soon.");
  this.reset();
});

// Animate skills when visible
window.addEventListener("scroll", () => {
  document.querySelectorAll(".progress div").forEach(bar => {
    const rect = bar.getBoundingClientRect();
    if(rect.top < window.innerHeight) {
      bar.style.transition = "width 2s";
      bar.style.width = bar.getAttribute("data-width");
    }
  });
});

// Dark mode toggle
const toggleBtn = document.getElementById("darkModeToggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  toggleBtn.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});

// Hamburger menu toggle
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");
hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});