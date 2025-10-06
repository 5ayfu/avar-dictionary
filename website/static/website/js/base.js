function initMenu() {
  const switcher = document.querySelector('.lang-switcher');
  if (switcher) {
    const btn = switcher.querySelector('.btn-lang');
    if (btn) {
      btn.setAttribute('aria-expanded', 'false');
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const isActive = switcher.classList.toggle('active');
        btn.setAttribute('aria-expanded', String(isActive));
      });
    }

    document.addEventListener('click', function (e) {
      if (!switcher.contains(e.target)) {
        switcher.classList.remove('active');
        if (btn) {
          btn.setAttribute('aria-expanded', 'false');
        }
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        switcher.classList.remove('active');
        if (btn) {
          btn.setAttribute('aria-expanded', 'false');
        }
      }
    });
  }

  const menuBtn = document.querySelector('.btn-menu');
  const nav = document.querySelector('.site-nav');
  if (menuBtn && nav) {
    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      const isOpen = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(isOpen));
    });

    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target) && e.target !== menuBtn) {
        nav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        nav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMenu);
} else {
  initMenu();
}
