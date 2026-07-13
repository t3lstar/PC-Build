(function () {
  const contentSelector = 'main img';
  const excludedSelector = [
    '.pc-qr-codes',
    '.pc-case-view',
    '.pc-connector-map',
    '.pc-cable-routing',
    '.pc-airflow',
    '.pc-exploded',
  ].join(',');

  function shouldEnable(image) {
    if (!image.currentSrc && !image.src) {
      return false;
    }

    if (image.closest(excludedSelector)) {
      return false;
    }

    return true;
  }

  function buildLightbox() {
    const lightbox = document.createElement('div');
    lightbox.className = 'pc-image-lightbox';
    lightbox.setAttribute('role', 'dialog');
    lightbox.setAttribute('aria-modal', 'true');
    lightbox.setAttribute('aria-label', 'Enlarged image');
    lightbox.hidden = true;

    lightbox.innerHTML = [
      '<button class="pc-image-lightbox__close" type="button" aria-label="Close enlarged image">Close</button>',
      '<figure class="pc-image-lightbox__figure">',
      '<img class="pc-image-lightbox__image" alt="">',
      '<figcaption class="pc-image-lightbox__caption"></figcaption>',
      '</figure>',
    ].join('');

    document.body.append(lightbox);
    return lightbox;
  }

  function init() {
    const images = Array.from(document.querySelectorAll(contentSelector)).filter(shouldEnable);
    if (images.length === 0) {
      return;
    }

    const lightbox = buildLightbox();
    const lightboxImage = lightbox.querySelector('.pc-image-lightbox__image');
    const caption = lightbox.querySelector('.pc-image-lightbox__caption');
    const closeButton = lightbox.querySelector('.pc-image-lightbox__close');
    let previousFocus = null;

    function close() {
      lightbox.hidden = true;
      lightboxImage.removeAttribute('src');
      document.documentElement.classList.remove('pc-image-lightbox-open');
      if (previousFocus) {
        previousFocus.focus();
      }
    }

    function open(image) {
      previousFocus = document.activeElement;
      const source = image.currentSrc || image.src;
      const label = image.alt || 'Documentation image';

      lightboxImage.src = source;
      lightboxImage.alt = label;
      caption.textContent = label;
      lightbox.hidden = false;
      document.documentElement.classList.add('pc-image-lightbox-open');
      closeButton.focus();
    }

    images.forEach((image) => {
      image.classList.add('pc-lightbox-source');
      image.setAttribute('tabindex', '0');
      image.setAttribute('role', 'button');
      image.setAttribute('aria-label', `Enlarge image: ${image.alt || 'documentation image'}`);

      image.addEventListener('click', () => open(image));
      image.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          open(image);
        }
      });
    });

    closeButton.addEventListener('click', close);
    lightbox.addEventListener('click', (event) => {
      if (event.target === lightbox) {
        close();
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && !lightbox.hidden) {
        close();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
