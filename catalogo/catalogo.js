/* ═══════════════════════════════════════════════════════════
   CRISCOLOR · Catálogo interactivo Navidad 2026
   Datos: /assets/catalog.js (CATALOG, FAMILIES, STAR_CODES)
          /catalogo/modelos.js (MODELS: referencias agrupadas)
   Libro: StPageFlip (MIT) en /catalogo/vendor
═══════════════════════════════════════════════════════════ */
(() => {
'use strict';

/* ── VÍDEOS Y AMBIENTES ────────────────────────────────────
   Vídeo en un producto: añade su código de referencia, p. ej.
     '43030': { src: '/media/catalogo/43030.mp4', poster: '/media/catalogo/43030.webp' }
   (sirve cualquier referencia del modelo). La ficha lo reproduce
   y la tarjeta del libro muestra un icono de vídeo.
   Página de ambiente por familia (foto o vídeo IA a sangre):
     papel: { img: '/media/catalogo/papel.webp?v=4' }  o  { video: '…mp4', poster: '…webp' }
────────────────────────────────────────────────────────── */
const VIDEOS = {};
const AMBIENTES = {
  papel: { img: '/media/catalogo/papel.webp?v=4' },
  bobinas: { img: '/media/catalogo/bobinas.webp?v=4' },
  bolsas: { img: '/media/catalogo/bolsas.webp?v=4' },
  lazos: { img: '/media/lazos/1.webp?v=4' },
  cajas: { img: '/media/cajas/1.webp?v=4' },
  sacos: { img: '/media/sacos/1.webp?v=4' },
  globos: { img: '/media/globos/1.webp?v=4' },
  decoracion: { img: '/media/decoracion/1.webp?v=4' },
  pegatinas: { img: '/media/pegatinas/1.webp?v=4' },
  fiesta: { img: '/media/fiesta/1.webp?v=4' },
  vajilla: { img: '/media/vajilla/1.webp?v=4' },
  calefaccion: { img: '/media/calefaccion/1.webp?v=4' }
};

const PER_PAGE = 6;
const FEATURE = 3;
const SEL_KEY = 'cc-catalogo-seleccion';
const DIM_ORDER = ['Medida', 'Color', 'Cantidad', 'Capas', 'Modelo', 'Composición'];
const DIM_LABEL = { Medida: 'Medida', Color: 'Color', Cantidad: 'Cantidad', Capas: 'Capas', Modelo: 'Modelo', 'Composición': 'Composición' };

const CAT = Object.fromEntries(CATALOG.map(p => [p.c, p]));
const FAM = Object.fromEntries(FAMILIES.map(f => [f.id, f]));
const STARS = new Set(STAR_CODES);
const MODEL = Object.fromEntries(MODELS.map(m => [m.id, m]));
const MODEL_OF = {};
MODELS.forEach(m => m.v.forEach(v => { MODEL_OF[v.c] = m.id; }));

const foto = e => `/productos/foto/${e}.webp`;
const mini = e => `/productos/mini/${e}.webp`;
const ficha = e => `/productos/ficha/${e}.webp`;
const famImg = id => `/img/familias/${id}.webp`;
const famCard = id => `/img/familias/${id}-card.webp`;

const $ = (s, el = document) => el.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const norm = s => String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
const plural = (n, a, b) => `${n} ${n === 1 ? a : b}`;

const I = {
  arrow: '<svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  star: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3Z"/></svg>',
  play: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5Z"/></svg>',
  swipe: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h12M12 4l4 4-4 4"/><path d="M20 16H8M12 12l-4 4 4 4"/></svg>',
  tap: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M12 10.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-.5a6 6 0 0 1-5.2-3L4.6 14.8a1.5 1.5 0 0 1 2.6-1.5L9 15"/></svg>',
  bag: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 7h12l-1 13H7L6 7Z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>',
  search: '<svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
  check: '<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>',
  chev: '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>',
};

/* Colores para las muestras */
const SWATCH = {
  blanco: '#FFFFFF', blanca: '#FFFFFF', blancas: '#FFFFFF', negro: '#1B1B1F', negra: '#1B1B1F', rojo: '#C8102E', roja: '#C8102E', rojos: '#C8102E',
  azul: '#1F4BB8', verde: '#1E7A3C', oro: 'linear-gradient(135deg,#F3DB8C,#B98A2E 55%,#E9C873)', dorado: 'linear-gradient(135deg,#F3DB8C,#B98A2E 55%,#E9C873)',
  plata: 'linear-gradient(135deg,#F2F3F5,#A7ABB3 55%,#E4E6EA)', plateado: 'linear-gradient(135deg,#F2F3F5,#A7ABB3 55%,#E4E6EA)',
  rosa: '#F2A3BE', fucsia: '#D6197A', lila: '#B79AD8', violeta: '#6E3FA8', morado: '#5B2A86', naranja: '#F07D1A', amarillo: '#F5C518',
  marron: '#7A4A26', beige: '#E3D2B4', crema: '#F3E8CF', gris: '#9A9DA5', turquesa: '#21B5B0', celeste: '#8CC8EE', burdeos: '#6D1A2A',
  magenta: '#C2187E', pistacho: '#A8C66C', granate: '#7A1F2B', cobre: 'linear-gradient(135deg,#F0B489,#A85A2A 55%,#E39C6B)', bronce: '#9C6B30',
  kraft: '#C49A6C', natural: '#D8C3A0', transparente: 'repeating-conic-gradient(#E6E8EE 0 25%, #fff 0 50%) 0 0/8px 8px', salmon: '#F29C84', champagne: '#EAD9B0',
};
function swatchFor(val) {
  const words = norm(val).split(/\s+/);
  for (const w of words) if (SWATCH[w]) return SWATCH[w];
  return null;
}
const swHTML = val => { const s = swatchFor(val); return s ? `<span class="sw" style="background:${s}" title="${esc(val)}"></span>` : ''; };

/* ═══ CONSTRUCCIÓN DEL LIBRO ═══ */
const famModels = {};
FAMILIES.forEach(f => {
  const list = MODELS.filter(m => m.f === f.id);
  famModels[f.id] = [...list.filter(m => m.s), ...list.filter(m => !m.s)];
});

const PAGES = [];          // { kind, html, family }
const MODEL_PAGE = {};     // id modelo → índice de página
const FAMILY_PAGE = {};    // id familia → página de apertura

function tileHTML(m, feature) {
  const lead = CAT[m.k];
  const n = m.v.length;
  const colors = m.d.includes('Color') ? [...new Set(m.v.map(v => v.a.Color))] : [];
  const sizes = m.d.includes('Medida') ? [...new Set(m.v.map(v => v.a.Medida))] : [];
  const hasVideo = m.v.some(v => VIDEOS[v.c]);
  const sw = colors.filter(swatchFor).slice(0, feature ? 10 : 6);
  const more = colors.length - sw.length;
  let meta;
  if (n === 1) meta = `<span>Ref. ${esc(lead.c)}</span>`;
  else {
    meta = `<span class="tile-var">${n} variantes</span>`;
    if (sw.length) meta += `<span class="swatches">${sw.map(swHTML).join('')}${more > 0 ? `<span class="sw-more">+${more}</span>` : ''}</span>`;
    else if (sizes.length > 1) meta += `<span>${plural(sizes.length, 'medida', 'medidas')}</span>`;
  }
  return `
    <div class="tile" role="button" tabindex="0" data-model="${m.id}" aria-label="${esc(m.t)}${n > 1 ? `, ${n} variantes` : ''}">
      <div class="tile-img"><img src="${foto(lead.e)}" alt="" loading="lazy" draggable="false"></div>
      <div class="tile-body">
        ${feature ? `<span class="tile-kicker">${m.s ? 'Producto destacado' : esc(FAM[m.f].name)}</span>` : ''}
        <span class="tile-name">${esc(m.t)}</span>
        <span class="tile-meta">${meta}</span>
        ${feature ? `<span class="tile-cta">Ver ficha ${I.arrow}</span>` : ''}
      </div>
      <div class="tile-badges">${hasVideo ? `<span class="tile-video" title="Con vídeo">${I.play}</span>` : ''}${m.s ? `<span class="tile-star" title="Producto destacado">${I.star}</span>` : ''}</div>
    </div>`;
}

/* Relleno de los huecos de la última página de cada familia */
function fillerHTML(f, free) {
  if (free <= 0) return '';
  let out = '';
  if (free % 2) out += `
    <div class="filler is-cell" role="button" tabindex="0" data-href="/familia/${f.id}">
      <span class="filler-kicker">${f.count} referencias</span>
      <span class="filler-title">Toda la familia en la web</span>
      <span class="filler-cta">Ver ${esc(f.name)} ${I.arrow}</span>
    </div>`;
  const rows = Math.floor(free / 2);
  if (rows) out += `
    <div class="filler is-row" style="grid-row: span ${rows}" role="button" tabindex="0" data-href="/#contacto">
      <span class="filler-body">
        <span class="filler-kicker">Venta a profesionales</span>
        <span class="filler-title">¿Te interesa ${esc(f.name)}?</span>
        <span class="filler-text">Pide precios y disponibilidad a tu comercial:<br><strong>(+34) 961 53 21 09</strong> · <strong>comercial@criscolor.com</strong></span>
        <span class="filler-cta">Solicitar precios ${I.arrow}</span>
      </span>
    </div>`;
  return out;
}

function head(f, label) {
  return `<div class="pg-head"><span><strong>${f.num}</strong> · ${esc(f.name)}</span><span>${label}</span></div>`;
}
function foot(i) {
  return `<div class="pg-foot"><span>Criscolor · Navidad 2026</span><span class="pg-folio">${i}</span></div>`;
}

function build() {
  // 0 · Portada
  PAGES.push({ kind: 'cover', html: () => `
    <div class="pg-bleed">
      <img src="/img/hero.webp" alt="" draggable="false">
      <div class="cover-logo"><img src="/img/logo.png" alt="Criscolor" draggable="false"></div>
      <div class="cover-season">Campaña<br>Navidad 2026</div>
      <div class="pg-bleed-content">
        <div class="cover-title">Catálogo<span>Navidad 2026</span></div>
        <p class="cover-sub">Papel de regalo, bolsas, lazos, cajas, globos, decoración, vajilla y calefacción para surtir tu tienda esta temporada.</p>
        <div class="cover-meta"><span><strong>${TOTAL_REFS}</strong> referencias</span><span><strong>${MODELS.length}</strong> modelos</span><span><strong>12</strong> familias</span></div>
        <div class="cover-hint">Desliza para abrir ${I.arrow}</div>
      </div>
    </div>` });

  // 1 · Índice  ·  2 · Cómo usar
  PAGES.push({ kind: 'toc', html: i => `
    <div class="pg">
      <div class="pg-head"><span><strong>Índice</strong></span><span>12 familias</span></div>
      <h2 class="pg-title">Índice</h2>
      <div class="toc">${FAMILIES.map(f => `
        <div class="toc-row" role="button" tabindex="0" data-goto="${FAMILY_PAGE[f.id]}">
          <span class="toc-num">${f.num}</span>
          <span class="toc-name">${esc(f.name)}<small>${plural(famModels[f.id].length, 'modelo', 'modelos')} · ${f.count} referencias</small></span>
          <span class="toc-page">${FAMILY_PAGE[f.id]}</span>
        </div>`).join('')}
      </div>
      ${foot(i)}
    </div>` });
  PAGES.push({ kind: 'howto', html: i => `
    <div class="pg">
      <div class="pg-head"><span><strong>Criscolor</strong> · Desde el año 2000</span><span>Cómo usar este catálogo</span></div>
      <h2 class="pg-title">Un catálogo para <em>tocar</em></h2>
      <div class="howto">
        <p class="howto-intro">Las ${TOTAL_REFS} referencias de la campaña de Navidad, agrupadas en ${MODELS.length} modelos: cada producto reúne sus colores, medidas y formatos en una sola ficha.</p>
        <div class="howto-steps">
          <div class="howto-step"><span class="howto-icon">${I.swipe}</span><div><strong>Pasa las páginas</strong><span>Desliza con el dedo, usa las flechas o salta a cualquier familia desde el índice.</span></div></div>
          <div class="howto-step"><span class="howto-icon">${I.tap}</span><div><strong>Toca un producto</strong><span>Se abre su ficha: elige color o medida y verás la referencia, el EAN y las unidades por caja.</span></div></div>
          <div class="howto-step"><span class="howto-icon">${I.bag}</span><div><strong>Guarda tu selección</strong><span>Añade referencias con sus cajas y descárgala en Excel o envíala a tu comercial.</span></div></div>
        </div>
        <div class="howto-stats">
          <div><strong>25+</strong>años de trayectoria</div>
          <div><strong>7.123</strong>clientes activos</div>
          <div><strong>13</strong>países</div>
        </div>
      </div>
      ${foot(i)}
    </div>` });

  // Familias: apertura (izquierda) + destacados (derecha) + rejillas, en bloques pares
  FAMILIES.forEach(f => {
    const list = famModels[f.id];
    const start = PAGES.length;
    FAMILY_PAGE[f.id] = start;
    PAGES.push({ kind: 'opener', family: f.id, html: () => `
      <div class="pg-bleed">
        <img src="${famImg(f.id)}" alt="" loading="lazy" draggable="false">
        <div class="pg-bleed-top"><span>Familia ${f.num} de 12</span><span>Navidad 2026</span></div>
        <div class="pg-bleed-content">
          <div class="opener-num">${f.num}</div>
          <h2 class="opener-name">${esc(f.name)}</h2>
          <p class="opener-desc">${esc(f.desc)}</p>
          <div class="opener-meta"><span><strong>${list.length}</strong> modelos</span><span><strong>${f.count}</strong> referencias</span><span><strong>${list.filter(m => m.s).length}</strong> destacados</span></div>
        </div>
      </div>` });
    const chunks = [list.slice(0, FEATURE)];
    for (let k = FEATURE; k < list.length; k += PER_PAGE) chunks.push(list.slice(k, k + PER_PAGE));
    chunks.forEach((chunk, ci) => {
      const idx = PAGES.length;
      chunk.forEach(m => { MODEL_PAGE[m.id] = idx; });
      const feature = ci === 0 && chunk.length === FEATURE;
      PAGES.push({ kind: 'grid', family: f.id, html: i => `
        <div class="pg">
          ${head(f, ci === 0 ? 'Selección destacada' : `${plural(chunk.length, 'modelo', 'modelos')}`)}
          <div class="pg-grid${feature ? ' is-feature' : ''}">${chunk.map((m, j) => tileHTML(m, feature && j === 0)).join('')}${feature ? '' : fillerHTML(f, PER_PAGE - chunk.length)}</div>
          ${foot(i)}
        </div>` });
    });
    if ((PAGES.length - start) % 2) {
      const amb = AMBIENTES[f.id] || {};
      PAGES.push({ kind: 'ambient', family: f.id, html: () => `
        <div class="pg-bleed">
          ${amb.video ? `<video src="${amb.video}" ${amb.poster ? `poster="${amb.poster}"` : ''} muted loop playsinline autoplay preload="none"></video>`
            : `<img src="${amb.img || famImg(f.id)}" alt="" loading="lazy" draggable="false" style="object-position:${amb.img ? 'center' : '78% 40%'};${amb.img ? '' : 'transform:scale(1.35)'}">`}
          <div class="pg-bleed-content"><div class="ambient-caption"><strong>${esc(f.name)}</strong>Colección Navidad 2026 · Criscolor</div></div>
        </div>` });
    }
  });

  // Contraportada
  PAGES.push({ kind: 'back', html: () => `
    <div class="pg">
      <div>
        <img class="back-logo" src="/img/logo.png" alt="Criscolor" draggable="false">
        <h2 class="back-title">Pide precios y<br><span>condiciones</span></h2>
        <p class="back-text">Venta exclusiva a profesionales. Nuestro equipo comercial te atiende en 24 h laborables con precios, disponibilidad y plazos de entrega.</p>
        <div class="back-contact">
          <div><strong>(+34) 961 53 21 09</strong>L-V de 8:00 a 13:30 y de 15:30 a 18:00</div>
          <div><strong>comercial@criscolor.com</strong>www.criscolor.com</div>
          <div><strong>Parc Empresarial Tàctica</strong>Carrer de l'Algepser, 125 · 46980 Paterna, Valencia</div>
        </div>
      </div>
      <div>
        <div class="back-eu"><img src="/img/banner-eu.png" alt="Generalitat Valenciana · IVACE · Finançat per la Unió Europea · Fons Europeus · Programa FEDER Comunitat Valenciana 2021-2027" draggable="false"></div>
        <p class="back-legal">© 2026 CRISCOLOR Distribuciones de Levante, S.L.U. · Imágenes orientativas.</p>
      </div>
    </div>` });
}
build();
const LAST = PAGES.length - 1;

/* ═══ LIBRO (StPageFlip) ═══ */
let flip = null;
let mode = null;
let current = 0;
const stage = $('#stage');
const host = $('#bookHost');

function pagesHTML() {
  return PAGES.map((p, i) => {
    const hard = p.kind === 'cover' || p.kind === 'back';
    const side = i === 0 ? '' : (i % 2 ? ' is-left' : ' is-right');
    return `<div class="page ${p.kind}${side}" ${hard ? 'data-density="hard"' : ''} data-index="${i}">${p.html(i)}</div>`;
  }).join('');
}

function layout() {
  const r = stage.getBoundingClientRect();
  const cs = getComputedStyle(stage);
  const availW = r.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  const availH = r.height - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  const ratio = 3 / 4;
  const spread = availW >= 700 && availW > availH * 1.05;
  const pageW = Math.floor(Math.min(spread ? availW / 2 : availW, availH * ratio));
  return { spread, pageW, pageH: Math.floor(pageW / ratio) };
}

function initBook(startAt) {
  const L = layout();
  mode = L.spread ? 'spread' : 'single';
  if (flip) { try { flip.destroy(); } catch (e) {} flip = null; }
  host.innerHTML = '';
  host.style.width = (L.spread ? L.pageW * 2 : L.pageW) + 'px';
  host.style.height = L.pageH + 'px';
  const book = document.createElement('div');
  book.className = 'book';
  book.innerHTML = pagesHTML();
  host.appendChild(book);
  flip = new St.PageFlip(book, {
    width: L.pageW, height: L.pageH, size: 'fixed',
    showCover: true, usePortrait: !L.spread, autoSize: false,
    maxShadowOpacity: 0.45, flippingTime: 760,
    mobileScrollSupport: false, disableFlipByClick: true, showPageCorners: true,
    startPage: Math.max(0, Math.min(LAST, startAt || 0)),
  });
  flip.loadFromHTML(book.querySelectorAll('.page'));
  flip.on('flip', e => { current = e.data; onPage(); });
  current = flip.getCurrentPageIndex();
  onPage();
}

let resizeT;
window.addEventListener('resize', () => {
  clearTimeout(resizeT);
  resizeT = setTimeout(() => {
    const L = layout();
    const m = L.spread ? 'spread' : 'single';
    const hostW = parseFloat(host.style.width);
    const want = L.spread ? L.pageW * 2 : L.pageW;
    if (m !== mode || Math.abs(hostW - want) > 8) initBook(current);
  }, 180);
});

/* Controles */
const range = $('#scrub');
const label = $('#scrubLabel');
const famLabel = $('#scrubFamily');
range.max = LAST;

function visiblePages() {
  if (mode === 'single' || current === 0 || current === LAST) return [current];
  const left = current % 2 ? current : current - 1;
  return [left, Math.min(left + 1, LAST)];
}
function onPage() {
  const vis = visiblePages();
  const first = vis[0];
  range.value = first;
  range.style.setProperty('--pct', `${(first / LAST) * 100}%`);
  const txt = first === 0 ? 'Portada' : first === LAST ? 'Contraportada' : vis.length > 1 && vis[1] !== LAST ? `Pág. <strong>${vis[0]}–${vis[1]}</strong>` : `Pág. <strong>${first}</strong>`;
  label.innerHTML = `${txt} <span aria-hidden="true">/ ${LAST}</span>`;
  const fam = PAGES[vis[vis.length - 1]].family || PAGES[first].family;
  famLabel.textContent = fam ? `${FAM[fam].num} · ${FAM[fam].name}` : '';
  $('#prevBtn').disabled = current <= 0;
  $('#nextBtn').disabled = current >= LAST || (vis.length > 1 && vis[1] >= LAST);
  try { history.replaceState(null, '', first ? `#p${first}` : location.pathname + location.search); } catch (e) {}
  vis.forEach(i => { const v = host.querySelector(`.page[data-index="${i}"] video`); if (v) v.play().catch(() => {}); });
}
function goTo(i) {
  if (!flip) return;
  i = Math.max(0, Math.min(LAST, i));
  if (i === current || visiblePages().includes(i)) return;
  const near = Math.abs(i - current) <= 2;
  if (near) flip.flip(i); else { flip.turnToPage(i); current = i; onPage(); }
}
$('#prevBtn').addEventListener('click', () => flip && flip.flipPrev());
$('#nextBtn').addEventListener('click', () => flip && flip.flipNext());
range.addEventListener('input', () => { range.style.setProperty('--pct', `${(range.value / LAST) * 100}%`); });
range.addEventListener('change', () => goTo(+range.value));

/* Toques en el libro: abrir ficha sin interferir con el deslizamiento */
let down = null;
host.addEventListener('pointerdown', e => {
  down = { x: e.clientX, y: e.clientY, t: Date.now() };
  const tile = e.target.closest('.tile');
  if (tile) { tile.classList.add('is-pressed'); setTimeout(() => tile.classList.remove('is-pressed'), 180); }
}, true);
host.addEventListener('click', e => {
  if (down && (Math.hypot(e.clientX - down.x, e.clientY - down.y) > 10 || Date.now() - down.t > 700)) return;
  const tile = e.target.closest('.tile');
  if (tile) { openModel(tile.dataset.model); return; }
  const go = e.target.closest('[data-goto]');
  if (go) { goTo(+go.dataset.goto); return; }
  const link = e.target.closest('[data-href]');
  if (link) window.open(link.dataset.href, '_blank', 'noopener');
});
host.addEventListener('keydown', e => {
  if (e.key !== 'Enter' && e.key !== ' ') return;
  const tile = e.target.closest('.tile');
  if (tile) { e.preventDefault(); openModel(tile.dataset.model); }
  const go = e.target.closest('[data-goto]');
  if (go) { e.preventDefault(); goTo(+go.dataset.goto); }
  const link = e.target.closest('[data-href]');
  if (link) { e.preventDefault(); window.open(link.dataset.href, '_blank', 'noopener'); }
});

/* ═══ HOJAS ═══ */
const scrim = $('#scrim');
let openSheet = null;
let lastFocus = null;
function showSheet(id) {
  if (openSheet && openSheet.id !== id) openSheet.classList.remove('is-open');
  lastFocus = document.activeElement;
  openSheet = $('#' + id);
  openSheet.classList.add('is-open');
  openSheet.setAttribute('aria-hidden', 'false');
  scrim.classList.add('is-on');
  setTimeout(() => (openSheet.querySelector('[data-autofocus]') || openSheet.querySelector('.sheet-close')).focus({ preventScroll: true }), 80);
}
function closeSheet() {
  if (!openSheet) return;
  openSheet.classList.remove('is-open');
  openSheet.setAttribute('aria-hidden', 'true');
  openSheet = null;
  scrim.classList.remove('is-on');
  if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
}
scrim.addEventListener('click', closeSheet);
document.querySelectorAll('[data-close]').forEach(b => b.addEventListener('click', closeSheet));

/* ── Ficha ── */
let fm = null;      // modelo abierto
let fsel = {};      // selección de dimensiones
function variantFor(m, sel) { return m.v.find(v => m.d.every(d => v.a[d] === sel[d])); }
function openModel(id, code) {
  const m = MODEL[id];
  if (!m) return;
  fm = m;
  const v0 = (code && m.v.find(v => v.c === code)) || m.v.find(v => v.c === m.k) || m.v[0];
  fsel = { ...v0.a };
  $('#fichaKicker').textContent = `${FAM[m.f].num} · ${FAM[m.f].name}${m.s ? ' · Destacado' : ''}`;
  $('#fichaTitle').textContent = m.t;
  renderFicha();
  showSheet('fichaSheet');
  $('#fichaBody').scrollTop = 0;
}
function renderFicha() {
  const m = fm;
  const v = variantFor(m, fsel) || m.v[0];
  const p = CAT[v.c];
  const img = $('#fichaImg');
  if (!img.src.endsWith(ficha(p.e))) {
    img.classList.add('is-loading');
    img.onload = () => img.classList.remove('is-loading');
    img.src = ficha(p.e);
  }
  img.alt = `Ficha de ${p.n}`;
  const vid = VIDEOS[v.c] || m.v.map(x => VIDEOS[x.c]).find(Boolean);
  $('#fichaVideo').innerHTML = vid ? `<div class="ficha-video"><video src="${vid.src}" ${vid.poster ? `poster="${vid.poster}"` : ''} controls playsinline preload="metadata"></video></div>` : '';

  const dims = DIM_ORDER.filter(d => m.d.includes(d));
  $('#fichaOpts').innerHTML = dims.map(d => {
    const vals = [...new Set(m.v.map(x => x.a[d]))];
    return `<div><div class="opt-label">${DIM_LABEL[d]}<b>${esc(fsel[d])}</b></div><div class="chips" role="group" aria-label="${DIM_LABEL[d]}">${vals.map(val => {
      const avail = !!variantFor(m, { ...fsel, [d]: val });
      return `<button type="button" class="chip${avail ? '' : ' is-unavail'}" aria-pressed="${fsel[d] === val}" data-dim="${esc(d)}" data-val="${esc(val)}">${d === 'Color' ? swHTML(val) : ''}${esc(val)}</button>`;
    }).join('')}</div></div>`;
  }).join('');

  $('#fichaFacts').innerHTML = `
    <div class="fact"><span>Referencia</span><strong>${esc(p.c)}</strong></div>
    <div class="fact"><span>Código EAN</span><strong>${esc(p.e)}</strong></div>
    <div class="fact"><span>Unidades por paquete</span><strong>${p.p || '—'}</strong></div>
    <div class="fact"><span>Unidades por caja</span><strong>${p.x || '—'}</strong></div>
    <div class="fact"><span>Familia</span><strong>${esc(FAM[m.f].name)}</strong></div>
    <div class="fact"><span>Descripción</span><strong>${esc(p.n)}</strong></div>`;

  const vl = $('#fichaVariants');
  if (m.v.length > 1) {
    vl.hidden = false;
    vl.querySelector('summary span').textContent = `Las ${m.v.length} referencias de este modelo`;
    vl.querySelector('.vlist').innerHTML = m.v.map(x => {
      const q = CAT[x.c];
      const lab = m.d.map(d => x.a[d]).join(' · ');
      return `<button type="button" class="vrow${x.c === v.c ? ' is-current' : ''}" data-code="${esc(x.c)}"><img src="${mini(q.e)}" alt="" loading="lazy"><span class="vrow-code">${esc(x.c)}</span><span>${esc(lab)}</span></button>`;
    }).join('');
  } else vl.hidden = true;

  const add = $('#fichaAdd');
  const inSel = SEL.some(s => s.c === v.c);
  add.classList.toggle('is-added', inSel);
  add.innerHTML = inSel ? `${I.check} En tu selección` : `Añadir a mi selección`;
  $('#fichaWeb').href = `/familia/${m.f}`;
}
$('#fichaOpts').addEventListener('click', e => {
  const b = e.target.closest('.chip');
  if (!b) return;
  const d = b.dataset.dim, val = b.dataset.val;
  let next = { ...fsel, [d]: val };
  if (!variantFor(fm, next)) {
    const alt = fm.v.find(x => x.a[d] === val);
    if (alt) next = { ...alt.a };
  }
  fsel = next;
  renderFicha();
});
$('#fichaVariants').addEventListener('click', e => {
  const b = e.target.closest('.vrow');
  if (!b) return;
  const x = fm.v.find(v => v.c === b.dataset.code);
  if (x) { fsel = { ...x.a }; renderFicha(); }
});
$('#fichaAdd').addEventListener('click', () => {
  const v = variantFor(fm, fsel) || fm.v[0];
  if (SEL.some(s => s.c === v.c)) { openSelection(); return; }
  SEL.push({ c: v.c, q: 1 });
  saveSel();
  renderFicha();
  toast(`Añadida la ref. ${v.c} a tu selección`);
});
$('#fichaImgBtn').addEventListener('click', () => {
  const v = variantFor(fm, fsel) || fm.v[0];
  openZoom(CAT[v.c]);
});
$('#fichaDownload').addEventListener('click', () => {
  const v = variantFor(fm, fsel) || fm.v[0];
  downloadFicha(CAT[v.c]);
});

/* Descarga de la ficha como JPG (convertida en el navegador) */
function downloadFicha(p) {
  const img = new Image();
  img.onload = () => {
    const c = document.createElement('canvas');
    c.width = img.naturalWidth; c.height = img.naturalHeight;
    const ctx = c.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, c.width, c.height);
    ctx.drawImage(img, 0, 0);
    c.toBlob(b => saveBlob(b, `Criscolor-${p.c.replace(/\W+/g, '-')}.jpg`), 'image/jpeg', 0.92);
  };
  img.onerror = () => window.open(ficha(p.e), '_blank');
  img.src = ficha(p.e);
}
function saveBlob(blob, name) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = name; document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(url); a.remove(); }, 1500);
}

/* ── Visor de ampliación ── */
const zoom = $('#zoom');
function openZoom(p) {
  const img = $('#zoomImg');
  img.src = ficha(p.e);
  img.alt = `Ficha de ${p.n}`;
  $('#zoomTitle').textContent = `Ref. ${p.c} · ${p.n}`;
  zoom.classList.remove('is-zoomed');
  img.style.width = '';
  zoom.classList.add('is-open');
  zoom.setAttribute('aria-hidden', 'false');
  $('#zoomClose').focus();
}
function closeZoom() { zoom.classList.remove('is-open'); zoom.setAttribute('aria-hidden', 'true'); }
$('#zoomClose').addEventListener('click', closeZoom);
$('#zoomImg').addEventListener('click', e => {
  const img = e.currentTarget, box = $('#zoomScroll');
  if (zoom.classList.contains('is-zoomed')) { zoom.classList.remove('is-zoomed'); img.style.width = ''; return; }
  const r = img.getBoundingClientRect();
  const fx = (e.clientX - r.left) / r.width, fy = (e.clientY - r.top) / r.height;
  const w = Math.max(r.width * 2.4, 1100);
  zoom.classList.add('is-zoomed');
  img.style.width = w + 'px';
  requestAnimationFrame(() => {
    box.scrollLeft = fx * img.offsetWidth - box.clientWidth / 2;
    box.scrollTop = fy * img.offsetHeight - box.clientHeight / 2;
  });
});
$('#zoomDownload').addEventListener('click', () => {
  const v = variantFor(fm, fsel) || fm.v[0];
  downloadFicha(CAT[v.c]);
});

/* ── Búsqueda ── */
const sInput = $('#searchInput');
function renderSearch() {
  const q = norm(sInput.value.trim());
  const out = $('#searchResults');
  if (q.length < 2) {
    $('#searchInfo').textContent = `Busca entre ${TOTAL_REFS} referencias por nombre, código o EAN.`;
    out.innerHTML = `<div class="empty"><div class="empty-icon">${I.search}</div>Prueba con <strong>lazo</strong>, <strong>Stitch</strong>, <strong>43030</strong> o un código de barras.</div>`;
    return;
  }
  const words = q.split(/\s+/);
  const hits = CATALOG.filter(p => {
    const hay = norm(`${p.n} ${p.c} ${p.e} ${FAM[p.f].name}`);
    return words.every(w => hay.includes(w));
  });
  // Agrupar por modelo para no repetir
  const byModel = new Map();
  hits.forEach(p => { const id = MODEL_OF[p.c]; if (!byModel.has(id)) byModel.set(id, []); byModel.get(id).push(p); });
  const exact = hits.find(p => norm(p.c) === q || p.e === q);
  $('#searchInfo').textContent = hits.length ? `${plural(hits.length, 'referencia', 'referencias')} en ${plural(byModel.size, 'modelo', 'modelos')}` : '';
  if (!hits.length) {
    out.innerHTML = `<div class="empty"><div class="empty-icon">${I.search}</div>No hay resultados para «<strong>${esc(sInput.value)}</strong>».<br>Revisa la palabra o busca por código o EAN.</div>`;
    return;
  }
  const rows = [...byModel.entries()].slice(0, 60).map(([id, ps]) => {
    const m = MODEL[id];
    const p = (exact && ps.includes(exact)) ? exact : ps[0];
    const sub = ps.length === 1 ? `Ref. ${p.c} · EAN ${p.e}` : `${ps.length} de ${m.v.length} referencias · ${FAM[m.f].name}`;
    return `<button type="button" class="result" data-model="${m.id}" data-code="${esc(p.c)}">
      <img src="${mini(p.e)}" alt="" loading="lazy">
      <span><span class="result-name">${esc(ps.length === 1 ? p.n : m.t)}</span><span class="result-sub">${esc(sub)}</span></span>
      <span class="result-page">Pág. ${MODEL_PAGE[m.id]}</span>
    </button>`;
  });
  out.innerHTML = rows.join('') + (byModel.size > 60 ? `<p class="search-info">Mostrando 60 de ${byModel.size} modelos · afina la búsqueda</p>` : '');
}
sInput.addEventListener('input', renderSearch);
sInput.addEventListener('keydown', e => { if (e.key === 'Enter') { const r = $('#searchResults .result'); if (r) r.click(); } });
$('#searchResults').addEventListener('click', e => {
  const r = e.target.closest('.result');
  if (!r) return;
  const id = r.dataset.model, code = r.dataset.code;
  closeSheet();
  goTo(MODEL_PAGE[id]);
  setTimeout(() => openModel(id, code), 520);
});
$('#searchBtn').addEventListener('click', () => { renderSearch(); showSheet('searchSheet'); });

/* ── Índice ── */
function renderIndex() {
  const vis = visiblePages();
  const curFam = PAGES[vis[vis.length - 1]].family;
  $('#indexList').innerHTML = `
    <button type="button" class="idx-row" data-goto="0"><img src="/img/hero-m.webp" alt=""><span><span class="idx-name">Portada</span><span class="idx-sub">Índice y cómo usar el catálogo</span></span><span class="idx-page">Pág. 1</span></button>
    <div class="idx-sep">Familias</div>
    ${FAMILIES.map(f => `
      <button type="button" class="idx-row${curFam === f.id ? ' is-current' : ''}" data-goto="${FAMILY_PAGE[f.id]}">
        <img src="${famCard(f.id)}" alt="" loading="lazy">
        <span><span class="idx-name">${f.num} · ${esc(f.name)}</span><span class="idx-sub">${plural(famModels[f.id].length, 'modelo', 'modelos')} · ${f.count} referencias</span></span>
        <span class="idx-page">Pág. ${FAMILY_PAGE[f.id]}</span>
      </button>`).join('')}
    <div class="idx-sep">Final</div>
    <button type="button" class="idx-row" data-goto="${LAST}"><img src="/img/og.jpg" alt=""><span><span class="idx-name">Contacto comercial</span><span class="idx-sub">Teléfono, email y dirección</span></span><span class="idx-page">Contra.</span></button>`;
}
$('#indexList').addEventListener('click', e => {
  const b = e.target.closest('[data-goto]');
  if (!b) return;
  closeSheet();
  setTimeout(() => goTo(+b.dataset.goto), 250);
});
$('#indexBtn').addEventListener('click', () => { renderIndex(); showSheet('indexSheet'); });

/* ── Mi selección ── */
let SEL = [];
try { SEL = JSON.parse(localStorage.getItem(SEL_KEY) || '[]').filter(s => CAT[s.c]); } catch (e) { SEL = []; }
function saveSel() {
  try { localStorage.setItem(SEL_KEY, JSON.stringify(SEL)); } catch (e) {}
  const c = $('#selCount');
  c.textContent = SEL.length;
  c.hidden = !SEL.length;
  c.classList.remove('bump'); void c.offsetWidth; c.classList.add('bump');
  setTimeout(() => c.classList.remove('bump'), 400);
  if ($('#selSheet').classList.contains('is-open')) renderSelection();
}
function renderSelection() {
  const body = $('#selList');
  const has = SEL.length > 0;
  $('#selFoot').hidden = !has;
  if (!has) {
    body.innerHTML = `<div class="empty"><div class="empty-icon">${I.bag}</div><strong>Tu selección está vacía</strong><br>Abre la ficha de un producto y pulsa «Añadir a mi selección». Después podrás descargarla en Excel o enviarla a tu comercial.</div>`;
    return;
  }
  body.innerHTML = SEL.map((s, i) => {
    const p = CAT[s.c];
    const m = MODEL[MODEL_OF[s.c]];
    const v = m.v.find(x => x.c === s.c);
    const lab = m.d.map(d => v.a[d]).join(' · ');
    return `<div class="sel-item" data-i="${i}">
      <img src="${mini(p.e)}" alt="" data-open="${esc(s.c)}">
      <div>
        <div class="sel-name" data-open="${esc(s.c)}">${esc(m.v.length > 1 ? m.t : p.n)}</div>
        <div class="sel-sub">Ref. ${esc(p.c)}${lab ? ` · ${esc(lab)}` : ''} · ${p.x || '—'} uds/caja</div>
        <div class="sel-ctrl">
          <span style="display:inline-flex;align-items:center"><span class="stepper"><button type="button" data-step="-1" aria-label="Una caja menos">−</button><input type="number" min="1" inputmode="numeric" value="${s.q}" aria-label="Cajas de la ref. ${esc(p.c)}"><button type="button" data-step="1" aria-label="Una caja más">+</button></span><span class="stepper-unit">${s.q === 1 ? 'caja' : 'cajas'}</span></span>
          <button type="button" class="sel-remove" data-remove>Quitar</button>
        </div>
      </div>
    </div>`;
  }).join('');
  const boxes = SEL.reduce((a, s) => a + s.q, 0);
  $('#selSummary').innerHTML = `<span><strong>${SEL.length}</strong> ${SEL.length === 1 ? 'referencia' : 'referencias'}</span><span><strong>${boxes}</strong> ${boxes === 1 ? 'caja' : 'cajas'}</span>`;
}
function openSelection() { renderSelection(); showSheet('selSheet'); }
$('#selBtn').addEventListener('click', openSelection);
$('#selList').addEventListener('click', e => {
  const item = e.target.closest('.sel-item');
  if (!item) return;
  const i = +item.dataset.i;
  const st = e.target.closest('[data-step]');
  if (st) { SEL[i].q = Math.max(1, SEL[i].q + +st.dataset.step); saveSel(); return; }
  if (e.target.closest('[data-remove]')) { SEL.splice(i, 1); saveSel(); return; }
  const o = e.target.closest('[data-open]');
  if (o) { const code = o.dataset.open; closeSheet(); setTimeout(() => openModel(MODEL_OF[code], code), 300); }
});
$('#selList').addEventListener('change', e => {
  if (e.target.matches('.stepper input')) {
    const i = +e.target.closest('.sel-item').dataset.i;
    SEL[i].q = Math.max(1, parseInt(e.target.value, 10) || 1);
    saveSel();
  }
});
function selRows() {
  return SEL.map(s => {
    const p = CAT[s.c];
    return { ref: p.c, ean: p.e, nombre: p.n, familia: FAM[p.f].name, paq: p.p || '', caja: p.x || '', cajas: s.q, uds: p.x ? p.x * s.q : '' };
  });
}
$('#selCsv').addEventListener('click', () => {
  const head = ['Referencia', 'EAN', 'Descripción', 'Familia', 'Uds/paquete', 'Uds/caja', 'Cajas', 'Unidades totales'];
  const q = v => `"${String(v).replace(/"/g, '""')}"`;
  const lines = [head.map(q).join(';'), ...selRows().map(r => [r.ref, `="${r.ean}"`, r.nombre, r.familia, r.paq, r.caja, r.cajas, r.uds].map((v, i) => i === 1 ? v : q(v)).join(';'))];
  const blob = new Blob(['﻿' + lines.join('\r\n')], { type: 'text/csv;charset=utf-8' });
  saveBlob(blob, `Seleccion-Criscolor-Navidad-2026.csv`);
});
$('#selMail').addEventListener('click', () => {
  const rows = selRows();
  let body = 'Hola,\n\nMe interesan estas referencias del catálogo Navidad 2026:\n\n';
  body += rows.map(r => `· Ref. ${r.ref} — ${r.nombre} — ${r.cajas} ${r.cajas === 1 ? 'caja' : 'cajas'}`).join('\n');
  body += '\n\n¿Me podéis pasar precios y disponibilidad?\n\nGracias.\n';
  const href = `mailto:comercial@criscolor.com?subject=${encodeURIComponent('Selección catálogo Navidad 2026')}&body=${encodeURIComponent(body)}`;
  if (href.length > 1900) toast('Tu selección es larga: descárgala en Excel y adjúntala al email');
  window.location.href = href.length > 1900 ? `mailto:comercial@criscolor.com?subject=${encodeURIComponent('Selección catálogo Navidad 2026')}&body=${encodeURIComponent('Hola,\n\nAdjunto mi selección del catálogo Navidad 2026 (' + rows.length + ' referencias). ¿Me podéis pasar precios y disponibilidad?\n\nGracias.\n')}` : href;
});
$('#selPrint').addEventListener('click', () => {
  const rows = selRows();
  $('#printSheet').innerHTML = `
    <h1>Mi selección · Catálogo Navidad 2026</h1>
    <p>Criscolor Distribuciones de Levante · comercial@criscolor.com · (+34) 961 53 21 09 · ${new Date().toLocaleDateString('es-ES')}</p>
    <table><thead><tr><th></th><th>Ref.</th><th>Descripción</th><th>EAN</th><th class="num">Uds/caja</th><th class="num">Cajas</th><th class="num">Unidades</th></tr></thead>
    <tbody>${rows.map(r => `<tr><td><img src="${mini(r.ean)}" alt=""></td><td>${esc(r.ref)}</td><td>${esc(r.nombre)}</td><td>${esc(r.ean)}</td><td class="num">${r.caja}</td><td class="num">${r.cajas}</td><td class="num">${r.uds}</td></tr>`).join('')}</tbody></table>`;
  setTimeout(() => window.print(), 150);
});
$('#selClear').addEventListener('click', () => {
  if (!$('#selClear').dataset.confirm) {
    $('#selClear').dataset.confirm = '1';
    $('#selClear').textContent = 'Pulsa otra vez para vaciar';
    setTimeout(() => { delete $('#selClear').dataset.confirm; $('#selClear').textContent = 'Vaciar selección'; }, 3000);
    return;
  }
  SEL = []; saveSel();
  delete $('#selClear').dataset.confirm; $('#selClear').textContent = 'Vaciar selección';
});

/* ── Pantalla completa ── */
const fsBtn = $('#fsBtn');
const fsEl = document.documentElement;
const canFs = !!(fsEl.requestFullscreen || fsEl.webkitRequestFullscreen);
fsBtn.hidden = !canFs;
fsBtn.addEventListener('click', () => {
  const on = document.fullscreenElement || document.webkitFullscreenElement;
  if (on) (document.exitFullscreen || document.webkitExitFullscreen).call(document);
  else (fsEl.requestFullscreen || fsEl.webkitRequestFullscreen).call(fsEl);
});

/* ── Avisos ── */
let toastT;
function toast(msg) {
  const t = $('#toast');
  t.querySelector('span').textContent = msg;
  t.classList.add('is-on');
  clearTimeout(toastT);
  toastT = setTimeout(() => t.classList.remove('is-on'), 2600);
}
const coach = $('#coach');
let seen = false;
try { seen = localStorage.getItem('cc-catalogo-coach') === '1'; } catch (e) {}
if (!seen) setTimeout(() => coach.classList.add('is-on'), 700);
$('#coachOk').addEventListener('click', () => {
  coach.classList.remove('is-on');
  try { localStorage.setItem('cc-catalogo-coach', '1'); } catch (e) {}
});

/* ── Teclado ── */
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    if (zoom.classList.contains('is-open')) return closeZoom();
    if (coach.classList.contains('is-on')) return $('#coachOk').click();
    return closeSheet();
  }
  if (openSheet || zoom.classList.contains('is-open') || /input|textarea/i.test(document.activeElement.tagName)) return;
  if (e.key === 'ArrowRight') flip && flip.flipNext();
  if (e.key === 'ArrowLeft') flip && flip.flipPrev();
  if (e.key === '/' || (e.key === 'f' && (e.metaKey || e.ctrlKey))) { e.preventDefault(); $('#searchBtn').click(); }
});

/* ── Arranque ── */
function startFromHash() {
  const h = location.hash;
  const pm = h.match(/^#p(\d+)$/);
  const rm = h.match(/^#ref=(.+)$/);
  if (rm) {
    const code = decodeURIComponent(rm[1]);
    const id = MODEL_OF[code];
    if (id) { setTimeout(() => openModel(id, code), 600); return MODEL_PAGE[id]; }
  }
  return pm ? +pm[1] : 0;
}
window.addEventListener('hashchange', () => {
  const h = location.hash;
  const rm = h.match(/^#ref=(.+)$/);
  if (rm) { const code = decodeURIComponent(rm[1]); const id = MODEL_OF[code]; if (id) { goTo(MODEL_PAGE[id]); setTimeout(() => openModel(id, code), 520); } return; }
  const pm = h.match(/^#p(\d+)$/);
  if (pm && !visiblePages().includes(+pm[1])) goTo(+pm[1]);
});
saveSel();
$('#selCount').classList.remove('bump');
initBook(startFromHash());
$('#loading').remove();
})();
