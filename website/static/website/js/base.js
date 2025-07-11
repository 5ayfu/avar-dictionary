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
});
