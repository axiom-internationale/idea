const root = document.documentElement;
const toggle = document.querySelector('.theme-toggle');
const themeLabel = (theme) => theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';

const syncThemeColor = (theme) => {
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.setAttribute('content', theme === 'dark' ? '#101111' : '#f4f4f1');
};

const THEME_KEY = 'axiom-theme-v2';

function setTheme(theme, persist = true) {
  root.dataset.theme = theme;
  if (persist) {
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch (e) {}
  }
  syncThemeColor(theme);
  if (!toggle) return;
  toggle.setAttribute('aria-pressed', String(theme === 'dark'));
  toggle.setAttribute('aria-label', themeLabel(theme));
}

// Initial theme comes from the inline head script — never persist it here, or
// a first visit would freeze the auto day/night default into a manual choice.
setTheme(root.dataset.theme || 'light', false);

// Google-Maps-style live update: re-evaluate the day/night default every
// 10 minutes and when the tab regains focus — auto mode only, never
// overriding an explicit manual choice.
const hasManualChoice = () => {
  try {
    return localStorage.getItem(THEME_KEY) !== null;
  } catch (e) {
    return true;
  }
};
const applyAutoTheme = () => {
  if (hasManualChoice()) return;
  const auto = typeof window.__axiomAutoTheme === 'function' ? window.__axiomAutoTheme() : null;
  if (auto && auto !== root.dataset.theme) {
    setTheme(auto, false);
    refreshThemeAutoUi();
  }
};

// Drawer "Follow day & night" reset: clears the saved choice and returns to
// auto. Its sublabel always shows the current mode.
const themeAutoBtn = document.querySelector('[data-theme-auto]');
const refreshThemeAutoUi = () => {
  if (!themeAutoBtn) return;
  let manual = true;
  try {
    manual = localStorage.getItem(THEME_KEY) !== null;
  } catch (e) {
    manual = true;
  }
  const state = themeAutoBtn.querySelector('[data-theme-auto-state]');
  if (state) {
    state.textContent = manual
      ? `Off — using ${root.dataset.theme === 'dark' ? 'Dark' : 'Light'}`
      : 'On — following day & night';
  }
  themeAutoBtn.setAttribute('aria-pressed', String(!manual));
};
if (toggle) {
  toggle.addEventListener('click', () => {
    setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    refreshThemeAutoUi();
  });
}
if (themeAutoBtn) {
  themeAutoBtn.addEventListener('click', () => {
    try {
      localStorage.removeItem(THEME_KEY);
    } catch (e) {}
    applyAutoTheme();
    refreshThemeAutoUi();
  });
}
refreshThemeAutoUi();
setInterval(applyAutoTheme, 10 * 60 * 1000);
document.addEventListener('visibilitychange', () => {
  if (!document.hidden) applyAutoTheme();
});

const dialog = document.querySelector('.brief-dialog');
const openBrief = document.querySelector('[data-open-brief]');
const closeBrief = document.querySelector('.dialog-close');
const understood = document.querySelector('.dialog-button');

if (dialog && openBrief) {
  let lastTrigger = null;
  openBrief.addEventListener('click', () => {
    lastTrigger = document.activeElement;
    dialog.showModal();
    if (closeBrief) closeBrief.focus();
  });
  const restoreFocus = () => {
    if (lastTrigger && document.contains(lastTrigger)) lastTrigger.focus();
    lastTrigger = null;
  };
  dialog.addEventListener('close', restoreFocus);
  if (closeBrief) closeBrief.addEventListener('click', () => dialog.close());
  if (understood) understood.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
}

const menuToggle = document.querySelector('.menu-toggle');
const menuDrawer = document.querySelector('.menu-drawer');
const menuBackdrop = document.querySelector('.menu-backdrop');
const menuClose = document.querySelector('.menu-close');

if (menuToggle && menuDrawer) {
  let menuTrigger = null;
  const openMenu = () => {
    menuTrigger = document.activeElement;
    menuDrawer.classList.add('open');
    if (menuBackdrop) menuBackdrop.classList.add('open');
    document.body.classList.add('menu-open');
    menuToggle.setAttribute('aria-expanded', 'true');
    const firstLink = menuDrawer.querySelector('.menu-link');
    if (firstLink) firstLink.focus();
  };
  const closeMenu = () => {
    menuDrawer.classList.remove('open');
    if (menuBackdrop) menuBackdrop.classList.remove('open');
    document.body.classList.remove('menu-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    if (menuTrigger && document.contains(menuTrigger)) menuTrigger.focus();
    menuTrigger = null;
  };
  menuToggle.addEventListener('click', () => {
    if (menuDrawer.classList.contains('open')) closeMenu();
    else openMenu();
  });
  if (menuClose) menuClose.addEventListener('click', closeMenu);
  if (menuBackdrop) menuBackdrop.addEventListener('click', closeMenu);
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuDrawer.classList.contains('open')) closeMenu();
  });
  // Focus trap: Tab cycles within the open drawer instead of escaping
  // into the page behind the modal backdrop.
  menuDrawer.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') return;
    const items = Array.from(menuDrawer.querySelectorAll('a[href], button:not([disabled])')).filter(
      (el) => el.offsetParent !== null
    );
    if (items.length === 0) return;
    const first = items[0];
    const last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });
}

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

const revealAll = () => {
  document.querySelectorAll('[data-reveal]').forEach((el) => el.classList.add('revealed'));
};

if (supportsMotion && 'IntersectionObserver' in window) {
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
  // Safety net: if the observer never fires (e.g. rendering quirks), never
  // leave content stuck invisible — reveal everything after a timeout.
  setTimeout(() => {
    document.querySelectorAll('[data-reveal]:not(.revealed)').forEach((el) => el.classList.add('revealed'));
  }, 2500);
} else {
  // Reduced motion or no IntersectionObserver: show everything immediately.
  revealAll();
}
