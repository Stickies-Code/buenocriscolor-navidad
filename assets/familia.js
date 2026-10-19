/* Página de familia: galería IA, destacados y todas las referencias */

const FAM_ID = document.body.dataset.family;
const FAM = FAM_BY_ID[FAM_ID];
const FAM_IDX = FAMILIES.findIndex(f => f.id === FAM_ID);
const FAM_REFS = CATALOG.filter(p => p.f === FAM_ID);

const MEDIA_ICON = {
  video: '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5Z"/></svg>',
  foto: '<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/></svg>',
};

/* ── Galería: 1 vídeo + 5 fotos; huecos mientras no haya material ── */
function renderMedia() {
  const m = MEDIA[FAM_ID] || { video: null, poster: null, fotos: [] };
  const ph = (kind, label) => `
    <div class="media-ph">
      <span class="media-ph-icon">${MEDIA_ICON[kind]}</span>
      <span class="media-ph-label">${label}</span>
      <span class="media-ph-note">Próximamente</span>
    </div>`;
  const video = m.video
    ? `<video src="${m.video}" ${m.poster ? `poster="${m.poster}"` : ''} autoplay muted loop playsinline preload="metadata" aria-label="Vídeo de ${escHTML(FAM.name)}"></video>`
    : ph('video', 'Vídeo IA');
  // La galería se adapta a lo que haya: sin vídeo no se reserva hueco,
  // y las fotos se muestran siempre completas (4:3), sin recortar el producto.
  const fotos = (m.fotos || []).slice(0, 5);
  const n = fotos.length;
  const sec = document.getElementById('mediaGrid').closest('section');
  if (!m.video && !n) { if (sec) sec.hidden = true; return; }
  const img = (src, i) => `<img src="${src}" alt="${escHTML(FAM.name)}: imagen ${i + 1}" loading="lazy">`;
  // Reparto de columnas (de 12) para las fotos
  const cols = k => k === 1 ? [12] : k === 2 ? [6, 6] : k === 3 ? [4, 4, 4] : k === 4 ? [6, 6, 6, 6] : [6, 6, 4, 4, 4];
  let slots = [];
  if (m.video && n === 1) {
    slots.push(`<div class="media-slot is-video is-stretch" style="--col:span 7">${video}</div>`);
    slots.push(`<div class="media-slot is-photo" style="--col:span 5">${img(fotos[0], 0)}</div>`);
  } else {
    if (m.video) slots.push(`<div class="media-slot is-video" style="--col:1 / -1">${video}</div>`);
    const c = cols(n);
    fotos.forEach((src, i) => {
      const lastOdd = n % 2 === 1 && i === n - 1 ? ' is-last-odd' : '';
      slots.push(`<div class="media-slot is-photo${lastOdd}" style="--col:span ${c[i]}">${img(src, i)}</div>`);
    });
  }
  const grid = document.getElementById('mediaGrid');
  grid.className = 'media-grid';
  grid.innerHTML = slots.join('');
  revealChildren(grid, '.media-slot', 0.06, 6);
}

/* ── Destacados de la familia ── */
function renderStars() {
  const stars = PRODUCTS.filter(p => p.family === FAM_ID);
  const sec = document.getElementById('famStars');
  if (!stars.length) { sec.hidden = true; return; }
  const grid = document.getElementById('famStarsGrid');
  grid.innerHTML = stars.map(productCardHTML).join('');
  revealChildren(grid, '.product-card');
}

/* ── Todas las referencias ── */
const PAGE = 60;
let refView = 'lista';
let refQuery = '';
let refLimit = PAGE;
try { refView = localStorage.getItem('cc-ref-view') || 'lista'; } catch (e) {}

function refRowHTML(p) {
  return `
    <button type="button" class="ref-row" onclick="openProduct('${p.c}')">
      <span class="ref-row-thumb"><img src="${photoMini(p.e)}" alt="" loading="lazy"></span>
      <span class="ref-row-code">${escHTML(p.c)}</span>
      <span class="ref-row-name">${escHTML(p.n)}${STAR_SET.has(p.c) ? ' <span class="ref-row-star">Destacado</span>' : ''}</span>
      <span class="ref-row-meta">${p.p ? `<span>${p.p} uds/paq.</span>` : ''}${p.x ? `<span>${p.x} uds/caja</span>` : ''}</span>
      <span class="ref-row-ean">EAN ${p.e}</span>
    </button>`;
}
function refTileHTML(p) {
  return `
    <button type="button" class="ref-tile" onclick="openProduct('${p.c}')">
      <span class="ref-tile-img"><img src="${photoFoto(p.e)}" alt="" loading="lazy"></span>
      <span class="ref-tile-body">
        <span class="ref-tile-code">Ref. ${escHTML(p.c)}</span>
        <span class="ref-tile-name">${escHTML(p.n)}</span>
        <span class="ref-tile-meta">${p.x ? `${p.x} uds/caja` : ''}${p.x && p.p ? ' · ' : ''}${p.p ? `${p.p} uds/paq.` : ''}</span>
      </span>
    </button>`;
}

function filteredRefs() {
  const nq = norm(refQuery.trim());
  return FAM_REFS.filter(p => !nq || norm(p.n).includes(nq) || p.c.toLowerCase().includes(nq) || p.e.includes(nq));
}

function renderRefs() {
  const list = filteredRefs();
  const shown = list.slice(0, refLimit);
  const box = document.getElementById('refsBox');
  document.getElementById('refsCount').innerHTML = refQuery.trim()
    ? `<strong>${list.length}</strong> de ${FAM_REFS.length} referencias`
    : `<strong>${FAM_REFS.length}</strong> referencias`;
  if (!list.length) {
    box.className = '';
    box.innerHTML = `<div class="ref-list"><div class="search-no-results">No hay referencias para «<strong>${escHTML(refQuery)}</strong>» en ${escHTML(FAM.name)}. Prueba con otra palabra, el código o el EAN.</div></div>`;
  } else if (refView === 'fotos') {
    box.className = 'ref-grid';
    box.innerHTML = shown.map(refTileHTML).join('');
  } else {
    box.className = 'ref-list';
    box.innerHTML = shown.map(refRowHTML).join('');
  }
  const more = document.getElementById('refsMore');
  more.hidden = list.length <= refLimit;
  more.querySelector('button').textContent = `Ver más referencias (${list.length - shown.length} restantes)`;
  document.querySelectorAll('.view-toggle button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.view === refView)));
}
function setRefView(v) {
  refView = v;
  try { localStorage.setItem('cc-ref-view', v); } catch (e) {}
  renderRefs();
}
function onRefSearch(v) { refQuery = v; refLimit = PAGE; renderRefs(); }
function showMoreRefs() { refLimit += PAGE; renderRefs(); }

/* ── Familia anterior / siguiente ── */
function renderFamNav() {
  const prev = FAMILIES[(FAM_IDX - 1 + FAMILIES.length) % FAMILIES.length];
  const next = FAMILIES[(FAM_IDX + 1) % FAMILIES.length];
  const back = '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>';
  document.getElementById('famNav').innerHTML = `
    <a class="fam-nav-card" href="${familyUrl(prev.id)}">
      <img src="${famCardImg(prev.id)}" alt="" loading="lazy">
      <span><span class="fam-nav-kicker">${back} Familia anterior · ${prev.num}</span><span class="fam-nav-name">${prev.name}</span></span>
    </a>
    <a class="fam-nav-card is-next" href="${familyUrl(next.id)}">
      <img src="${famCardImg(next.id)}" alt="" loading="lazy">
      <span><span class="fam-nav-kicker">Familia siguiente · ${next.num} ${ICON.arrow}</span><span class="fam-nav-name">${next.name}</span></span>
    </a>`;
}

if (FAM) {
  renderMedia();
  renderStars();
  renderRefs();
  renderFamNav();
}
