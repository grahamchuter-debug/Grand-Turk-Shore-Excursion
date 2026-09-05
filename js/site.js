/**
 * Progressive enhancement: primary content is inlined at build time.
 * JS wires mobile nav + active nav state. Partials load only if slots are empty.
 */
(function () {
  function basePath() {
    const base = document.body.dataset.base;
    if (base === undefined || base === '') return '';
    return base.endsWith('/') ? base : base + '/';
  }

  async function loadInto(id, url) {
    const el = document.getElementById(id);
    if (!el || !url) return;
    if (el.dataset.inlined === 'true' || el.innerHTML.trim().length > 40) return;

    try {
      const res = await fetch(basePath() + url);
      if (!res.ok) throw new Error(res.statusText);
      el.innerHTML = await res.text();
    } catch (err) {
      console.error('Layout load failed:', url, err);
    }
  }

  function setActiveNav() {
    const page = document.body.dataset.page;
    if (!page) return;

    document.querySelectorAll('[data-nav]').forEach(function (link) {
      const isActive = link.dataset.nav === page;
      link.classList.toggle('text-ocean-600', isActive);
      link.classList.toggle('font-semibold', isActive);
      link.classList.toggle('text-gray-600', !isActive);
      if (isActive) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  }

  function wireMobileNav() {
    const nav = document.querySelector('#site-nav nav');
    if (!nav) return;
    const btn = nav.querySelector('button[aria-label="Open menu"], button[aria-label="Close menu"]');
    if (!btn) return;

    let panel = nav.querySelector('[data-mobile-panel]');
    if (!panel) {
      panel = document.createElement('div');
      panel.setAttribute('data-mobile-panel', 'true');
      panel.className = 'lg:hidden hidden border-t border-turk-100 bg-white px-4 py-3';
      panel.innerHTML =
        '<div class="flex flex-col gap-3 text-sm font-medium">' +
        '<a href="/" class="py-2 text-gray-700 hover:text-ocean-600">Home</a>' +
        '<a href="/best-grand-turk-shore-excursions" class="py-2 text-gray-700 hover:text-ocean-600">Shore Excursions</a>' +
        '<a href="/best-beaches-in-grand-turk" class="py-2 text-gray-700 hover:text-ocean-600">Best Beaches</a>' +
        '<a href="/gibbs-cay-stingray-excursions" class="py-2 text-gray-700 hover:text-ocean-600">Gibbs Cay</a>' +
        '<a href="/grand-turk-cruise-port-guide" class="py-2 text-gray-700 hover:text-ocean-600">Port Guide</a>' +
        '<a href="/one-day-in-grand-turk" class="py-2 text-gray-700 hover:text-ocean-600">One Day</a>' +
        '<a href="/contact" class="py-2 text-gray-700 hover:text-ocean-600">Contact</a>' +
        '</div>';
      nav.appendChild(panel);
    }

    function setOpen(open) {
      panel.classList.toggle('hidden', !open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    if (btn.dataset.wired === 'true') return;
    btn.dataset.wired = 'true';
    btn.setAttribute('aria-expanded', 'false');

    btn.addEventListener('click', function () {
      setOpen(panel.classList.contains('hidden'));
    });

    panel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        setOpen(false);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', async function () {
    const hero = document.body.dataset.hero;
    const content = document.body.dataset.content;
    const trustStrip = document.body.dataset.trustStrip;

    await Promise.all([
      loadInto('site-nav', 'partials/nav.html'),
      loadInto('site-footer', 'partials/footer.html'),
      loadInto('page-hero', hero),
      loadInto('page-trust-strip', trustStrip),
      loadInto('page-content', content),
    ]);

    setActiveNav();
    wireMobileNav();
  });
})();
