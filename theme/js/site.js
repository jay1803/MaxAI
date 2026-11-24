(function () {
  var root = document.documentElement;

  // Theme toggle
  var tbtn = document.getElementById('theme-toggle');
  if (tbtn) tbtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    renderDiagrams();
  });

  // Page index toggle
  var bbtn = document.getElementById('bar-btn');
  var idx = document.getElementById('site-index');
  function setIdx(open) {
    if (!bbtn || !idx) return;
    bbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    idx.hidden = !open;
  }
  if (bbtn) bbtn.addEventListener('click', function () { setIdx(idx.hidden); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setIdx(false); });

  // Wrap tables so wide ones scroll instead of overflowing.
  document.querySelectorAll('.prose table').forEach(function (t) {
    if (t.parentElement.classList.contains('tbl')) return;
    var w = document.createElement('div');
    w.className = 'tbl';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  // Current section in the bar.
  var heads = Array.prototype.slice.call(document.querySelectorAll('.prose h2'));
  var sep = document.getElementById('bar-sep');
  var sec = document.getElementById('bar-sec');
  function headText(h) {
    var c = h.cloneNode(true);
    c.querySelectorAll('.headerlink').forEach(function (a) { a.remove(); });
    return c.textContent.trim();
  }
  function onScroll() {
    if (!sec || !heads.length) return;
    var cur = null;
    for (var i = 0; i < heads.length; i++) {
      if (heads[i].getBoundingClientRect().top < 150) cur = heads[i]; else break;
    }
    if (cur) { sec.textContent = headText(cur); sep.hidden = false; }
    else { sec.textContent = ''; sep.hidden = true; }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Diagrams
  var diagrams = Array.prototype.slice.call(document.querySelectorAll('.mermaid'));
  diagrams.forEach(function (d) { d.setAttribute('data-src', d.textContent); });
  function renderDiagrams() {
    var m = window.__mermaid;
    if (!m || !diagrams.length) return;
    var dark = root.getAttribute('data-theme') === 'dark';
    var css = getComputedStyle(root);
    m.initialize({
      startOnLoad: false,
      theme: 'base',
      fontFamily: css.getPropertyValue('--sans'),
      themeVariables: {
        fontSize: '14px',
        background: css.getPropertyValue('--bg').trim(),
        primaryColor: css.getPropertyValue('--surface').trim(),
        primaryBorderColor: css.getPropertyValue('--rule-strong').trim(),
        primaryTextColor: css.getPropertyValue('--ink').trim(),
        lineColor: css.getPropertyValue('--ink-3').trim(),
        secondaryColor: css.getPropertyValue('--bg').trim(),
        tertiaryColor: css.getPropertyValue('--surface').trim(),
        clusterBkg: css.getPropertyValue('--bg').trim(),
        clusterBorder: css.getPropertyValue('--rule-strong').trim(),
        edgeLabelBackground: css.getPropertyValue('--bg').trim(),
        darkMode: dark
      }
    });
    diagrams.forEach(function (d) {
      d.removeAttribute('data-processed');
      d.textContent = d.getAttribute('data-src');
    });
    m.run({ nodes: diagrams });
  }
  if (window.__mermaid) renderDiagrams();
  else window.addEventListener('mermaid-ready', renderDiagrams, { once: true });
})();
