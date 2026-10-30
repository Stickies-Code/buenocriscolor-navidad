/* Portada: familias y los 10 más vendidos */

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

renderFamilies();
renderProducts(BESTSELLERS.map(c => CAT_BY_CODE[c]).filter(Boolean).map(toProduct));
