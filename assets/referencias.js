/* Página «Todas las referencias»: familia elegida + buscador + lista o fotos */
(() => {
  const STEP = 60;
  let fam = 'all', query = '', limit = STEP, view = 'lista';
  try { view = localStorage.getItem('cc-ref-view') || 'lista'; } catch (e) {}
  const params = new URLSearchParams(location.search);
  if (params.get('familia') && FAM_BY_ID[params.get('familia')]) fam = params.get('familia');

  const box = document.getElementById('refsBox');
  const more = document.getElementById('refsMore');
  const list = () => {
    const nq = norm(query.trim());
    return CATALOG.filter(p => (fam === 'all' || p.f === fam) &&
      (!nq || norm(p.n).includes(nq) || p.c.toLowerCase().includes(nq) || p.e.includes(nq)));
  };
  function render() {
    const all = list();
    const shown = all.slice(0, limit);
    const total = fam === 'all' ? CATALOG.length : FAM_BY_ID[fam].count;
    const where = fam === 'all' ? '' : ` en ${FAM_BY_ID[fam].name}`;
    document.getElementById('refsCount').innerHTML = query.trim()
      ? `<strong>${all.length}</strong> de ${total} referencias${where}`
      : `<strong>${total}</strong> referencias${where}`;
    if (!all.length) {
      box.className = 'ref-list';
      box.innerHTML = `<div class="search-no-results">No hay referencias para «<strong>${escHTML(query)}</strong>»${escHTML(where)}. Prueba con otra palabra, el código o el EAN.</div>`;
    } else {
      box.className = view === 'fotos' ? 'ref-grid' : 'ref-list';
      box.innerHTML = shown.map(view === 'fotos' ? refTileHTML : refRowHTML).join('');
    }
    more.hidden = all.length <= limit;
    more.querySelector('button').textContent = `Ver más referencias (${all.length - shown.length} restantes)`;
    document.querySelectorAll('.view-toggle button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.view === view)));
    document.querySelectorAll('.refs-fams .filter-chip').forEach(b => {
      const on = b.dataset.fam === fam;
      b.classList.toggle('active', on); b.setAttribute('aria-pressed', String(on));
    });
  }
  document.querySelector('.refs-fams').addEventListener('click', e => {
    const b = e.target.closest('.filter-chip');
    if (!b) return;
    fam = b.dataset.fam; limit = STEP; render();
    try { history.replaceState(null, '', fam === 'all' ? location.pathname : `?familia=${fam}`); } catch (err) {}
    b.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
  });
  document.getElementById('refSearch').addEventListener('input', e => { query = e.target.value; limit = STEP; render(); });
  document.querySelectorAll('.view-toggle button').forEach(b => b.addEventListener('click', () => {
    view = b.dataset.view; try { localStorage.setItem('cc-ref-view', view); } catch (e) {} render();
  }));
  more.querySelector('button').addEventListener('click', () => { limit += STEP; render(); });
  render();
})();
