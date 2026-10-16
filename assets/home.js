/* Portada: familias y destacados */

function renderFamilies() {
  const grid = document.getElementById('familiesGrid');
  grid.innerHTML = FAMILIES.map((f, i) => `
    <a href="${familyUrl(f.id)}" class="family-card reveal" style="--d:${(i % 3) * 0.08}s" aria-label="${f.name}: ${refsLabel(f.count)}">
      <img src="${famCardImg(f.id)}" alt="" loading="lazy">
      <span class="family-card-overlay">
        <span class="family-card-num">${f.num}</span>
        <span class="family-card-name">${f.name}</span>
        <span class="family-card-foot">
          <span class="family-card-refs">${refsLabel(f.count)}</span>
          <span class="family-card-btn">Ver familia <span class="btn-icon">${ICON.arrow}</span></span>
        </span>
      </span>
    </a>`).join('');
}

function renderProducts(prods) {
  const grid = document.getElementById('featuredGrid');
  grid.innerHTML = prods.map(productCardHTML).join('');
  revealChildren(grid, '.product-card');
}

function renderFilters() {
  const bar = document.getElementById('filtersBar');
  const opts = [{ id: 'all', label: 'Todos' }, ...FAMILIES.map(f => ({ id: f.id, label: f.name.split(' ')[0] }))];
  bar.innerHTML = opts.map((o, i) => `
    <button type="button" class="filter-chip ${i === 0 ? 'active' : ''}" aria-pressed="${i === 0}" onclick="filterBy('${o.id}', this)">${o.label}</button>`).join('');
}

function filterBy(id, btn) {
  document.querySelectorAll('.filter-chip').forEach(c => { c.classList.remove('active'); c.setAttribute('aria-pressed', 'false'); });
  btn.classList.add('active');
  btn.setAttribute('aria-pressed', 'true');
  renderProducts(id === 'all' ? PRODUCTS : PRODUCTS.filter(p => p.family === id));
}

renderFamilies();
renderFilters();
renderProducts(PRODUCTS);
