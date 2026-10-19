#!/usr/bin/env python3
"""Genera familia/<id>.html (12 páginas) a partir de las piezas comunes de index.html.

Uso:  python3 tools/build_familias.py
Ejecutar después de cambiar en index.html el menú, el footer o la ficha
(bloques <!-- @nav -->, <!-- @footer -->, <!-- @modal -->, <!-- @head -->, <!-- @scripts -->)
o los datos de assets/catalog.js.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://buenocriscolor-navidad.vercel.app'
index = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
catjs = open(os.path.join(ROOT, 'assets', 'catalog.js'), encoding='utf-8').read()

def block(name):
    m = re.search(rf'<!-- @{name} -->\n(.*?)\n<!-- /@{name} -->', index, re.S)
    assert m, name
    return m.group(1)

FAMS = [dict(id=m[0], num=m[1], name=m[2], desc=json.loads(m[3]), count=int(m[4])) for m in
        re.findall(r"\{ id: '(\w+)', num: '(\d+)', name: '([^']+)', desc: (\".*?\"), count: (\d+) \}", catjs)]
assert len(FAMS) == 12, len(FAMS)
STARS = json.loads(re.search(r'const STAR_CODES = (\[.*?\]);', catjs).group(1))
CATALOG = [json.loads(l.rstrip(',')) for l in catjs.split('\n') if l.startswith('{"c":')]
fam_of = {p['c']: p['f'] for p in CATALOG}

head = '\n'.join(l for l in block('head').split('\n') if 'property="og:' not in l)
nav, footer, modal, scripts = block('nav'), block('footer'), block('modal'), block('scripts')

ARROW16 = '<svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg width="12" height="12" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
LIST = '<svg width="15" height="15" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg>'
GRID = '<svg width="15" height="15" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg>'

os.makedirs(os.path.join(ROOT, 'familia'), exist_ok=True)
for f in FAMS:
    e = {k: html.escape(str(v)) for k, v in f.items()}
    stars = sum(1 for c in STARS if fam_of.get(c) == f['id'])
    page_nav = nav.replace(f'<a href="/familia/{f["id"]}" class="nav-familias-item">',
                           f'<a href="/familia/{f["id"]}" class="nav-familias-item" aria-current="page">')
    page = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{e['name']} — Catálogo Navidad 2026 · Criscolor</title>
<meta name="description" content="{e['count']} referencias de {e['name']} en el catálogo mayorista Navidad 2026 de Criscolor. {e['desc']}">
<link rel="canonical" href="{SITE}/familia/{f['id']}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e['name']} — Catálogo Navidad 2026 · Criscolor">
<meta property="og:description" content="{e['count']} referencias de {e['name']}. Venta mayorista desde Paterna, Valencia.">
<meta property="og:image" content="{SITE}/img/og/{f['id']}.jpg">
<meta property="og:url" content="{SITE}/familia/{f['id']}">
{head}
<link rel="preload" href="/img/familias/{f['id']}.webp" as="image">
</head>
<body data-family="{f['id']}">
<a href="#referencias" class="skip-link">Saltar a las referencias</a>

{page_nav}

<main>
<header class="fam-hero">
  <div class="fam-hero-bg"><img src="/img/familias/{f['id']}.webp" alt="" fetchpriority="high"></div>
  <div class="fam-hero-overlay"></div>
  <div class="fam-hero-content">
    <nav class="breadcrumb" aria-label="Estás en">
      <a href="/">Catálogo Navidad 2026</a> {CHEV} <a href="/#familias">Familias</a> {CHEV} <span aria-current="page">{e['name']}</span>
    </nav>
    <h1>{e['name']}</h1>
    <p class="fam-hero-desc">{e['desc']}</p>
    <div class="hero-ctas">
      <a href="#referencias" class="btn-hero-primary">Ver referencias <span class="btn-icon">{ARROW16}</span></a>
      <a href="/#contacto" class="btn-hero-outline">Solicitar precios</a>
    </div>
    <div class="hero-meta">
      <span>Familia <strong>{e['num']}</strong> de 12</span>
      <span><strong>{e['count']}</strong> referencias</span>
      <span><strong>{stars}</strong> destacados</span>
      <span>Temporada <strong>2026</strong></span>
    </div>
  </div>
</header>

<section class="fam-section is-white" aria-labelledby="mediaTitle">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="section-title" id="mediaTitle">{e['name']} <em>en imágenes</em></h2>
      <p class="section-subtitle">El producto de cerca: acabados, estampados y detalles de la colección.</p>
    </div>
    <div class="media-grid" id="mediaGrid"></div>
  </div>
</section>

<section class="fam-section is-paper" id="famStars" aria-labelledby="starsTitle">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="section-title" id="starsTitle">Productos <em>destacados</em></h2>
      <p class="section-subtitle">Las referencias estrella de {e['name']} en esta campaña, con su ficha completa.</p>
    </div>
    <div class="fam-stars-grid" id="famStarsGrid"></div>
  </div>
</section>

<section class="fam-section is-white" id="referencias" aria-labelledby="refsTitle">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="section-title" id="refsTitle">Todas las <em>referencias</em></h2>
      <p class="section-subtitle">Pulsa cualquier referencia para abrir su ficha con foto, código, EAN y unidades por caja.</p>
    </div>
    <div class="refs-toolbar">
      <input type="search" class="ref-search" placeholder="Buscar por nombre, código o EAN…" aria-label="Buscar en {e['name']}" oninput="onRefSearch(this.value)">
      <div class="refs-tools-right">
        <span class="refs-count" id="refsCount" aria-live="polite"></span>
        <div class="view-toggle" role="group" aria-label="Vista de referencias">
          <button type="button" data-view="lista" aria-pressed="true" onclick="setRefView('lista')">{LIST} Lista</button>
          <button type="button" data-view="fotos" aria-pressed="false" onclick="setRefView('fotos')">{GRID} Fotos</button>
        </div>
      </div>
    </div>
    <div id="refsBox" class="ref-list"></div>
    <div class="refs-more" id="refsMore" hidden><button type="button" class="btn btn-outline" onclick="showMoreRefs()">Ver más referencias</button></div>
  </div>
</section>

<section class="fam-section is-paper" aria-label="Otras familias">
  <div class="container">
    <div class="fam-nav" id="famNav"></div>
    <div class="fam-all-link"><a href="/#familias" class="btn btn-outline">Ver las 12 familias</a></div>
  </div>
</section>

<section class="fam-cta">
  <div class="container fam-cta-inner reveal">
    <div>
      <h2 class="section-title">¿Te interesa la familia <em>{e['name']}</em>?</h2>
      <p>Pide precios, condiciones y disponibilidad a nuestro equipo comercial. Venta exclusiva a profesionales.</p>
    </div>
    <div class="fam-cta-actions">
      <a href="/#contacto" class="btn-hero-primary">Solicitar precios <span class="btn-icon">{ARROW16}</span></a>
      <span class="fam-cta-phone">o llama al <a href="tel:+34961532109">(+34) 961 53 21 09</a></span>
    </div>
  </div>
</section>
</main>

{footer}

{modal}

{scripts}
<script src="/assets/familia.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, 'familia', f"{f['id']}.html"), 'w', encoding='utf-8').write(page)
print(f'{len(FAMS)} páginas generadas en familia/')
