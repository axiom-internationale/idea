const root = document.documentElement;
const toggle = document.querySelector('.theme-toggle');
const themeLabel = (theme) => theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';

function setTheme(theme) {
  root.dataset.theme = theme;
  localStorage.setItem('axiom-theme', theme);
  toggle.setAttribute('aria-pressed', String(theme === 'dark'));
  toggle.setAttribute('aria-label', themeLabel(theme));
}

setTheme(root.dataset.theme || 'light');
toggle.addEventListener('click', () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark'));

const dialog = document.querySelector('.brief-dialog');
const openBrief = document.querySelector('[data-open-brief]');
const closeBrief = document.querySelector('.dialog-close');
const understood = document.querySelector('.dialog-button');

openBrief.addEventListener('click', () => dialog.showModal());
closeBrief.addEventListener('click', () => dialog.close());
understood.addEventListener('click', () => dialog.close());
dialog.addEventListener('click', (event) => {
  if (event.target === dialog) dialog.close();
});

const supportsMotion = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const isFinePointer = window.matchMedia('(pointer: fine)').matches;

if (supportsMotion && isFinePointer) {
  document.querySelectorAll('[data-bento]').forEach((bento) => {
    const cards = bento.querySelectorAll('[data-depth]');
    bento.addEventListener('pointermove', (event) => {
      const bounds = bento.getBoundingClientRect();
      const x = (event.clientX - bounds.left) / bounds.width - 0.5;
      const y = (event.clientY - bounds.top) / bounds.height - 0.5;
      cards.forEach((card) => {
        const depth = Number(card.dataset.depth);
        card.style.transform = `translate3d(${x * depth}px, ${y * depth}px, 0)`;
      });
    });
    bento.addEventListener('pointerleave', () => {
      cards.forEach((card) => { card.style.transform = ''; });
    });
  });
}

if (supportsMotion) {
  const reveals = document.querySelectorAll('[data-reveal]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const card = entry.target;
        const siblings = Array.from(card.parentElement.querySelectorAll('[data-reveal]'));
        const idx = siblings.indexOf(card);
        card.style.transitionDelay = `${idx * 70}ms`;
        card.classList.add('revealed');
        observer.unobserve(card);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  reveals.forEach((el) => observer.observe(el));
}
