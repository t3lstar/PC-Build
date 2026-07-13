(function () {
  function closeLightbox(overlay) {
    overlay.classList.remove("is-open");
    overlay.querySelector("img").removeAttribute("src");
    document.body.style.overflow = "";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var diagrams = Array.prototype.slice.call(
      document.querySelectorAll('.md-typeset img[src*="assets/diagrams"]')
    );

    if (!diagrams.length) {
      return;
    }

    var overlay = document.createElement("div");
    overlay.className = "pc-lightbox";
    overlay.setAttribute("aria-hidden", "true");
    overlay.innerHTML =
      '<button class="pc-lightbox__close" type="button" aria-label="Close diagram">&times;</button>' +
      '<img class="pc-lightbox__image" alt="">';
    document.body.appendChild(overlay);

    var overlayImage = overlay.querySelector("img");
    overlay.querySelector("button").addEventListener("click", function () {
      closeLightbox(overlay);
    });
    overlay.addEventListener("click", function (event) {
      if (event.target === overlay) {
        closeLightbox(overlay);
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && overlay.classList.contains("is-open")) {
        closeLightbox(overlay);
      }
    });

    diagrams.forEach(function (image) {
      image.setAttribute("tabindex", "0");
      image.setAttribute("role", "button");
      image.setAttribute("title", "Click to enlarge");

      var hint = document.createElement("div");
      hint.className = "pc-diagram-hint";
      hint.textContent = "Click to enlarge";
      image.insertAdjacentElement("afterend", hint);

      function open() {
        overlayImage.src = image.currentSrc || image.src;
        overlayImage.alt = image.alt || "Diagram";
        overlay.classList.add("is-open");
        overlay.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
      }

      image.addEventListener("click", open);
      image.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          open();
        }
      });
    });
  });
})();
