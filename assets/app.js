/* ═══════════════════════════════════════════════════════════
   CRISCOLOR · Catálogo Navidad 2026 — lógica compartida
   (portada y páginas de familia). Requiere assets/catalog.js
═══════════════════════════════════════════════════════════ */

const FAM_BY_ID = Object.fromEntries(FAMILIES.map(f => [f.id, f]));
const CAT_BY_CODE = Object.fromEntries(CATALOG.map(p => [p.c, p]));
const STAR_SET = new Set(STAR_CODES);

/* Rutas */
const familyUrl = id => `/familia/${id}`;
const famImg = id => `/img/familias/${id}.webp`;
const famCardImg = id => `/img/familias/${id}-card.webp`;
const photoFoto = ean => `/productos/foto/${ean}.webp`;
const photoMini = ean => `/productos/mini/${ean}.webp`;
const photoFicha = ean => `/productos/ficha/${ean}.webp`;

function escHTML(s) { return String(s).replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch])); }
function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
function refsLabel(n) { return `${n} ${n === 1 ? 'referencia' : 'referencias'}`; }

const ICON = {
  arrow: '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  box: '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8 12 3 3 8v8l9 5 9-5V8Z"/><path d="M3 8l9 5 9-5M12 13v8"/></svg>',
  pack: '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 12h16M12 4v16"/></svg>',
  star: '<svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3Z"/></svg>',
};

function toProduct(p) {
  const f = FAM_BY_ID[p.f];
  return {
    id: p.c, ref: p.c, family: p.f, familyName: f.name, name: p.n, ean: p.e || '—',
    uds: p.x || null, pack: p.p || null,
    img: p.e ? photoFoto(p.e) : famCardImg(p.f),
    ficha: p.e ? photoFicha(p.e) : famCardImg(p.f),
  };
}
const PRODUCTS = STAR_CODES.map(c => CAT_BY_CODE[c]).filter(Boolean).map(toProduct);

function productCardHTML(p) {
  return `
    <div class="product-card" role="button" tabindex="0" onclick="openProduct('${p.id}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();openProduct('${p.id}')}">
      <div class="product-card-img">
        <img src="${p.img}" alt="${escHTML(p.name)}" loading="lazy">
        <div class="product-card-family-tag">${p.familyName}</div>
        ${STAR_SET.has(p.ref) ? `<div class="product-card-star" title="Producto destacado">${ICON.star}</div>` : ''}
      </div>
      <div class="product-card-body">
        <div class="product-card-ref">Ref. ${p.ref}</div>
        <div class="product-card-name">${escHTML(p.name)}</div>
        <div class="product-card-specs">
          ${p.uds ? `<span class="spec-chip">${ICON.box} ${p.uds} uds/caja</span>` : ''}
          ${p.pack ? `<span class="spec-chip">${ICON.pack} ${p.pack} uds/paquete</span>` : ''}
        </div>
        <div class="product-card-footer">
          <div class="product-card-ean">EAN ${p.ean}</div>
          <div class="product-card-view">Ver ficha ${ICON.arrow}</div>
        </div>
      </div>
    </div>`;
}

/* ── Revelado al hacer scroll ── */
const revealObserver = 'IntersectionObserver' in window
  ? new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); revealObserver.unobserve(e.target); }
    }), { rootMargin: '0px 0px -8% 0px', threshold: 0.06 })
  : null;
function observeReveal(el) { if (revealObserver) revealObserver.observe(el); else el.classList.add('is-in'); }
function revealChildren(container, selector, step = 0.07, cols = 3) {
  container.querySelectorAll(selector).forEach((el, i) => {
    el.classList.add('reveal');
    el.style.setProperty('--d', `${(i % cols) * step}s`);
    observeReveal(el);
  });
}

/* ── Ficha de producto ── */
let lastFocus = null;
function openProduct(code) {
  const raw = CAT_BY_CODE[code];
  if (!raw) return;
  const p = toProduct(raw);
  lastFocus = document.activeElement;
  document.getElementById('modalFamily').textContent = p.familyName + (STAR_SET.has(p.ref) ? ' · Producto destacado' : '');
  document.getElementById('modalName').textContent = p.name;
  const img = document.getElementById('modalImg');
  img.src = p.ficha;
  img.alt = `Ficha de ${p.name}`;
  document.getElementById('modalDesc').textContent = `Referencia de la familia ${p.familyName} del catálogo Navidad 2026. Venta exclusiva a profesionales: consulta precios y disponibilidad con nuestro equipo comercial.`;
  document.getElementById('modalRef').textContent = p.ref;
  document.getElementById('modalEan').textContent = p.ean;
  document.getElementById('modalUds').textContent = p.uds ? `${p.uds} unidades` : '—';
  document.getElementById('modalMedida').textContent = p.pack ? `${p.pack} unidades` : '—';
  document.getElementById('modalMat').textContent = p.familyName;
  const link = document.getElementById('modalFamilyLink');
  if (link) {
    const here = document.body.dataset.family === p.family;
    link.hidden = here;
    link.href = familyUrl(p.family);
    link.querySelector('span').textContent = `Ver toda la familia ${p.familyName}`;
  }
  document.getElementById('productModal').classList.add('active');
  document.body.style.overflow = 'hidden';
  setTimeout(() => document.querySelector('#productModal .modal-close')?.focus(), 60);
}
function closeModal(e) {
  const modal = document.getElementById('productModal');
  if (!modal.classList.contains('active')) return;
  if (!e || e.target === modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
}

/* ── Búsqueda global ── */
function doSearch(q) {
  const panel = document.getElementById('searchResults');
  const inner = document.getElementById('searchResultsInner');
  if (!q || q.trim().length < 2) { panel.classList.remove('active'); return; }
  const nq = norm(q.trim());
  const results = CATALOG.filter(p =>
    norm(p.n).includes(nq) || p.c.toLowerCase().includes(nq) || (p.e || '').includes(nq) || norm(FAM_BY_ID[p.f].name).includes(nq));
  if (!results.length) {
    inner.innerHTML = `<div class="search-no-results">No hay productos para «<strong>${escHTML(q)}</strong>». Prueba con otra palabra, el código o el EAN.</div>`;
  } else {
    const shown = results.slice(0, 40);
    inner.innerHTML = shown.map(p => `
      <div class="search-result-item" role="button" tabindex="0" onclick="openProduct('${p.c}'); hideSearchResults();" onkeydown="if(event.key==='Enter'){openProduct('${p.c}'); hideSearchResults();}">
        <div class="search-result-img"><img src="${photoMini(p.e)}" alt="" loading="lazy"></div>
        <div>
          <div class="search-result-name">${escHTML(p.n)}</div>
          <div class="search-result-ref">Ref. ${p.c} · ${FAM_BY_ID[p.f].name}</div>
        </div>
      </div>`).join('') + (results.length > shown.length
      ? `<div class="search-no-results">Mostrando 40 de ${results.length} resultados · afina la búsqueda</div>` : '');
  }
  panel.classList.add('active');
}
function showSearchResults() {
  if (document.getElementById('globalSearch').value.trim().length >= 2) document.getElementById('searchResults').classList.add('active');
}
function hideSearchResults() { document.getElementById('searchResults').classList.remove('active'); }

/* ── Menú de familias ── */
function toggleFamiliasMenu() {
  const dd = document.getElementById('navFamiliasDropdown');
  const isOpen = dd.classList.toggle('open');
  dd.querySelector('.nav-familias-btn').setAttribute('aria-expanded', String(isOpen));
}
function closeFamiliasMenu() {
  const dd = document.getElementById('navFamiliasDropdown');
  if (dd) { dd.classList.remove('open'); dd.querySelector('.nav-familias-btn').setAttribute('aria-expanded', 'false'); }
}
document.addEventListener('click', e => {
  const dd = document.getElementById('navFamiliasDropdown');
  if (dd && !dd.contains(e.target)) closeFamiliasMenu();
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') { closeModal(); closeFamiliasMenu(); hideSearchResults(); }
});

/* ── Formulario de contacto (pendiente de conectar a un servicio de envío) ── */
function submitForm(e) {
  if (e) e.preventDefault();
  const form = document.getElementById('contactForm');
  const nombre = form.querySelector('#f-nombre');
  const tel = form.querySelector('#f-tel');
  const email = form.querySelector('#f-email');
  const checks = [
    [nombre, nombre.value.trim().length >= 2],
    [tel, tel.value.replace(/\D/g, '').length >= 9],
    [email, !email.value.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())],
  ];
  let firstBad = null;
  checks.forEach(([input, ok]) => {
    input.closest('.form-group').classList.toggle('has-error', !ok);
    input.setAttribute('aria-invalid', String(!ok));
    if (!ok && !firstBad) firstBad = input;
  });
  if (firstBad) { firstBad.focus(); return; }
  const btn = document.getElementById('formSubmit');
  btn.innerHTML = 'Solicitud enviada · te contactaremos en 24 h';
  btn.classList.add('is-sent');
  btn.disabled = true;
}
document.addEventListener('input', e => {
  const g = e.target.closest && e.target.closest('.form-group.has-error');
  if (g) { g.classList.remove('has-error'); e.target.removeAttribute('aria-invalid'); }
});

/* ── Arranque común ── */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.reveal').forEach(observeReveal);
  requestAnimationFrame(() => requestAnimationFrame(() => document.documentElement.classList.add('is-loaded')));
  const nav = document.querySelector('.nav');
  const sentinel = document.querySelector('.hero, .fam-hero');
  if (nav && sentinel && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => nav.classList.toggle('is-scrolled', !e.isIntersecting), { rootMargin: '-80px 0px 0px 0px' }).observe(sentinel);
  }
});
