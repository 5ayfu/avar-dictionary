document.addEventListener('DOMContentLoaded', function() {
  const switcher = document.querySelector('.lang-switcher');
  if (switcher) {
    const btn = switcher.querySelector('.btn-lang');
    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      switcher.classList.toggle('active');
    });
    document.addEventListener('click', function(e) {
      if (!switcher.contains(e.target)) {
        switcher.classList.remove('active');
      }
    });
  }

  const menuBtn = document.querySelector('.btn-menu');
  const nav = document.querySelector('.site-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      nav.classList.toggle('open');
    });
    document.addEventListener('click', function(e) {
      if (!nav.contains(e.target) && e.target !== menuBtn) {
        nav.classList.remove('open');
      }
    });
  }
});
