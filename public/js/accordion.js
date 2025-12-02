document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".accordion-header").forEach(header => {
    header.addEventListener("click", (e) => {
      e.preventDefault();

      const section = header.parentElement;
      const isOpen = section.classList.contains("open");

      // Close siblings
      section.parentElement
        .querySelectorAll(".accordion-section.open")
        .forEach(s => s.classList.remove("open"));

      // Toggle this one
      if (!isOpen) {
        section.classList.add("open");
      }
    });
  });
});

