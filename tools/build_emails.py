#!/usr/bin/env python3
"""Genera las campañas de email de Navidad 2026 (HTML compatible con Klaviyo).

Salida en /email:
  navidad-a-imprescindibles.html      → correo A, para pegar en Klaviyo (con etiquetas de Klaviyo)
  navidad-b-calendario.html           → correo B, idem
  preview/…                           → mismas piezas con las etiquetas resueltas, para verlas en el navegador

Cambiar BASE cuando la web se publique en su dominio definitivo y volver a ejecutar.
"""
import os

BASE = os.environ.get('EMAIL_BASE', 'https://buenocriscolor-navidad.vercel.app')
IMG = BASE + '/email/img/'
CAT = BASE + '/catalogo/'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'email')

# Paleta de la web
NAVY = '#00063F'
INK = '#00109E'
GOLD = '#E2BE76'
GOLD_DARK = '#9C7426'
GOLD_SOFT = '#F4E7C8'
PAPER = '#F6F7FB'
TEXT = '#10122E'
TEXT2 = '#4A4D68'
LINE = '#E1E4EE'
SERIF = "'Libre Caslon Display', Georgia, 'Times New Roman', serif"
SANS = "'Hanken Grotesk', Helvetica, Arial, sans-serif"

FAMS = [
    ('papel', 'Papel de Regalo', 67), ('bobinas', 'Bobinas de Regalo', 60), ('bolsas', 'Bolsas', 158),
    ('lazos', 'Lazos y Cintas', 100), ('cajas', 'Cajas Cartón', 49), ('sacos', 'Sacos Navideños', 11),
    ('globos', 'Globos', 42), ('decoracion', 'Decoración Navidad', 77), ('pegatinas', 'Pegatinas y Tarjetas', 17),
    ('fiesta', 'Fiesta y Novedades', 26), ('vajilla', 'Vajilla Desechable', 161), ('calefaccion', 'Calefacción', 26),
]


def fam_url(f):
    return f'{BASE}/familia/{f}'


def ref_url(c):
    return f'{CAT}#ref={c}'


# ── Piezas ───────────────────────────────────────────────────

def head(title, preheader):
    return f'''<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{title}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;600;700&family=Libre+Caslon+Display&display=swap" rel="stylesheet">
<style>
  body, table, td, a {{ -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
  table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; }}
  img {{ -ms-interpolation-mode: bicubic; border: 0; outline: none; text-decoration: none; display: block; height: auto; }}
  body {{ margin: 0 !important; padding: 0 !important; width: 100% !important; background: #E9EBF3; }}
  a {{ color: {INK}; }}
  a[x-apple-data-detectors] {{ color: inherit !important; text-decoration: none !important; }}
  .btn a:hover {{ opacity: .9; }}
  @media screen and (max-width: 620px) {{
    .container {{ width: 100% !important; }}
    .px {{ padding-left: 22px !important; padding-right: 22px !important; }}
    .stack {{ display: block !important; width: 100% !important; max-width: 100% !important; }}
    .stack {{ padding-left: 0 !important; padding-right: 0 !important; }}
    .stack-pad {{ padding: 0 0 18px 0 !important; }}
    .col3 {{ max-width: 50% !important; }}
    .keep3 {{ max-width: 33.33% !important; }}
    .col2 {{ max-width: 50% !important; }}
    .col2 p {{ font-size: 15px !important; line-height: 20px !important; }}
    .keep3 p {{ font-size: 12px !important; line-height: 16px !important; }}
    .h1 {{ font-size: 34px !important; line-height: 38px !important; }}
    .h2 {{ font-size: 27px !important; line-height: 32px !important; }}
    .fluid {{ width: 100% !important; max-width: 100% !important; }}
    .hide-m {{ display: none !important; }}
    .btn-full {{ width: 100% !important; }}
    .btn-full a {{ display: block !important; }}
    .stat {{ font-size: 26px !important; line-height: 30px !important; }}
    .stat-l {{ font-size: 10px !important; letter-spacing: 0.8px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:#E9EBF3;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{preheader}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#E9EBF3;">
<tr><td align="center" style="padding:24px 10px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#FFFFFF;border-radius:18px;overflow:hidden;">
'''


def foot():
    return f'''
<!-- Pie -->
<tr><td class="px" style="padding:34px 40px 30px;background:{PAPER};border-top:1px solid {LINE};" align="center">
  <a href="{BASE}/"><img src="{IMG}logo.png" width="150" alt="Criscolor" style="width:150px;margin:0 auto 16px;"></a>
  <p style="margin:0 0 6px;font-family:{SANS};font-size:13px;line-height:20px;color:{TEXT2};">
    <a href="tel:+34961532109" style="color:{TEXT};font-weight:700;text-decoration:none;">(+34) 961 53 21 09</a> &nbsp;·&nbsp;
    <a href="mailto:comercial@criscolor.com" style="color:{TEXT};font-weight:700;text-decoration:none;">comercial@criscolor.com</a>
  </p>
  <p style="margin:0 0 6px;font-family:{SANS};font-size:12px;line-height:19px;color:{TEXT2};">L-V de 8:00 a 13:30 y de 15:30 a 18:00</p>
  <p style="margin:0 0 18px;font-family:{SANS};font-size:12px;line-height:19px;color:{TEXT2};">CRISCOLOR Distribuciones de Levante, S.L.U. · Parc Empresarial Tàctica, C/ de l'Algepser, 125 · 46980 Paterna (Valencia)</p>
  <p style="margin:0;font-family:{SANS};font-size:11px;line-height:18px;color:#8A8DA6;">
    Recibes este correo como cliente profesional de Criscolor. Venta exclusiva a profesionales. Imágenes orientativas.<br>
    <a href="{{% unsubscribe_link %}}" style="color:#8A8DA6;text-decoration:underline;">Darse de baja</a> &nbsp;·&nbsp;
    <a href="{{% manage_preferences_link %}}" style="color:#8A8DA6;text-decoration:underline;">Preferencias</a>
  </p>
</td></tr>
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
'''


def topbar(label):
    return f'''
<!-- Barra superior -->
<tr><td style="background:{NAVY};padding:10px 24px;" class="px">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td style="font-family:{SANS};font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:{GOLD};font-weight:700;">{label}</td>
    <td align="right" class="hide-m" style="font-family:{SANS};font-size:11px;color:#B9BCD6;"><a href="{{% web_view_link %}}" style="color:#B9BCD6;text-decoration:underline;">Ver en el navegador</a></td>
  </tr></table>
</td></tr>
<!-- Logo -->
<tr><td align="center" style="padding:22px 24px 18px;background:#FFFFFF;">
  <a href="{BASE}/"><img src="{IMG}logo.png" width="170" alt="Criscolor" style="width:170px;margin:0 auto;"></a>
</td></tr>'''


def button(text, href, bg=GOLD, fg=NAVY, border=None, width=None, full=True):
    b = border or bg
    w = f'width:{width}px;' if width else ''
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" class="btn{' btn-full' if full else ''}" style="border-collapse:separate;{w}"><tr>
  <td align="center" bgcolor="{bg}" style="border-radius:12px;background:{bg};">
    <a href="{href}" style="display:inline-block;padding:13px 26px;font-family:{SANS};font-size:15px;line-height:20px;font-weight:700;color:{fg};text-decoration:none;border-radius:12px;border:2px solid {b};background:{bg};">{text}</a>
  </td></tr></table>'''


def kicker(t, color=GOLD_DARK):
    return f'<p style="margin:0 0 10px;font-family:{SANS};font-size:11px;letter-spacing:1.8px;text-transform:uppercase;font-weight:700;color:{color};">{t}</p>'


def h2(t, color=TEXT, align='left'):
    return f'<h2 class="h2" style="margin:0 0 12px;font-family:{SERIF};font-weight:400;font-size:32px;line-height:36px;color:{color};text-align:{align};">{t}</h2>'


def p(t, color=TEXT2, size=16, align='left', mb=20):
    return f'<p style="margin:0 0 {mb}px;font-family:{SANS};font-size:{size}px;line-height:{round(size * 1.6)}px;color:{color};text-align:{align};">{t}</p>'


def spacer(h, bg='#FFFFFF'):
    return f'<tr><td style="height:{h}px;line-height:{h}px;font-size:0;background:{bg};">&nbsp;</td></tr>'


def stats(items):
    cells = ''.join(
        f'''<td width="{100 // len(items)}%" align="center" valign="top" style="padding:0 4px;">
          <p class="stat" style="margin:0;font-family:{SERIF};font-size:34px;line-height:38px;color:{INK};">{n}</p>
          <p class="stat-l" style="margin:4px 0 0;font-family:{SANS};font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:{TEXT2};font-weight:700;">{l}</p>
        </td>''' for n, l in items)
    return f'''
<tr><td class="px" style="padding:30px 40px;border-bottom:1px solid {LINE};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table>
</td></tr>'''


def media_block(gif, href, alt, kick, title, text, btn, bg='#FFFFFF'):
    """Vídeo (GIF animado) a todo el ancho con su texto y botón."""
    return f'''
<tr><td class="px" style="padding:40px 40px 8px;background:{bg};">
  {kicker(kick)}{h2(title)}{p(text, mb=22)}
</td></tr>
<tr><td class="px" style="padding:0 40px;background:{bg};">
  <a href="{href}"><img src="{IMG}{gif}" width="520" alt="{alt}" class="fluid" style="width:520px;max-width:100%;border-radius:14px;"></a>
  <p style="margin:10px 0 0;font-family:{SANS};font-size:12px;color:#8A8DA6;">&#9654; Vídeo del producto · toca para verlo en la web</p>
</td></tr>
<tr><td class="px" style="padding:20px 40px 40px;background:{bg};">{button(btn, href, bg=INK, fg='#FFFFFF', full=True)}</td></tr>'''


def product_pair(items):
    """Dos fichas de producto en paralelo (apiladas en móvil)."""
    cells = []
    for i, (img, name, ref, meta, href) in enumerate(items):
        pad = 'padding:0 10px 0 0;' if i == 0 else 'padding:0 0 0 10px;'
        cells.append(f'''<td class="stack stack-pad" width="50%" valign="top" style="{pad}">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};border-radius:14px;overflow:hidden;">
        <tr><td><a href="{href}"><img src="{IMG}{img}" width="249" alt="{name}" class="fluid" style="width:100%;max-width:100%;"></a></td></tr>
        <tr><td style="padding:16px 16px 18px;">
          <p style="margin:0 0 4px;font-family:{SANS};font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:{GOLD_DARK};font-weight:700;">Ref. {ref}</p>
          <p style="margin:0 0 6px;font-family:{SANS};font-size:16px;line-height:22px;font-weight:700;color:{TEXT};">{name}</p>
          <p style="margin:0 0 12px;font-family:{SANS};font-size:13px;line-height:20px;color:{TEXT2};">{meta}</p>
          <a href="{href}" style="font-family:{SANS};font-size:14px;font-weight:700;color:{INK};text-decoration:none;">Ver ficha &rarr;</a>
        </td></tr>
      </table>
    </td>''')
    return f'''
<tr><td class="px" style="padding:0 40px 20px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{''.join(cells)}</tr></table>
</td></tr>'''


def families_grid():
    """Rejilla fluida: 3 columnas en ordenador, 2 en móvil (tablas MSO para Outlook)."""
    cards = []
    for i, (fid, name, n) in enumerate(FAMS):
        pre = '<!--[if mso]><tr><![endif]-->' if i % 3 == 0 else ''
        post = '<!--[if mso]></tr><![endif]-->' if i % 3 == 2 else ''
        cards.append(f'''{pre}<!--[if mso]><td width="177" valign="top" style="padding:0 0 16px;"><![endif]--><div class="col3" style="display:inline-block;width:100%;max-width:177px;vertical-align:top;font-size:14px;">
        <div style="padding:0 6px 16px;"><a href="{fam_url(fid)}" style="text-decoration:none;">
          <img src="{IMG}fam-{fid}.jpg" width="161" alt="{name}" class="fluid" style="width:100%;max-width:100%;border-radius:10px;">
          <p style="margin:8px 0 0;font-family:{SANS};font-size:14px;line-height:18px;font-weight:700;color:{TEXT};">{name}</p>
          <p style="margin:2px 0 0;font-family:{SANS};font-size:12px;line-height:16px;color:{TEXT2};">{n} referencias</p>
        </a></div>
      </div><!--[if mso]></td><![endif]-->{post}''')
    return f'''
<tr><td class="px" style="padding:40px 40px 6px;background:{PAPER};">
  {kicker('12 familias')}{h2('Todo para la Navidad, en un solo catálogo')}{p('Elige una familia y entra directamente a todas sus referencias, con ficha, medidas y unidades por caja.', mb=18)}
</td></tr>
<tr><td class="px" style="padding:0 34px 0;background:{PAPER};font-size:0;line-height:0;">
  <!--[if mso]><table role="presentation" width="531" cellpadding="0" cellspacing="0" border="0"><![endif]-->{''.join(cards)}<!--[if mso]></table><![endif]-->
</td></tr>
<tr><td class="px" style="padding:8px 40px 40px;background:{PAPER};">{button('Ver todas las familias en la web', BASE + '/#familias', bg='#FFFFFF', fg=INK, border=INK)}</td></tr>'''


def steps():
    st = [('1', 'Abre el catálogo', 'Pasa las páginas o busca por nombre, referencia o EAN.'),
          ('2', 'Guarda tu selección', 'Añade las referencias que te interesan con sus cantidades.'),
          ('3', 'Envíala a tu comercial', 'Descárgala en Excel o mándala y te respondemos con precios.')]
    cells = ''.join(f'''<td class="stack stack-pad" width="33%" valign="top" style="padding:0 16px 0 0;">
      <p style="margin:0 0 10px;width:38px;height:38px;line-height:38px;border-radius:19px;background:{INK};color:#FFFFFF;font-family:{SANS};font-size:16px;font-weight:700;text-align:center;">{n}</p>
      <p style="margin:0 0 4px;font-family:{SANS};font-size:15px;font-weight:700;color:{TEXT};">{t}</p>
      <p style="margin:0;font-family:{SANS};font-size:13px;line-height:20px;color:{TEXT2};">{d}</p>
    </td>''' for n, t, d in st)
    return f'''
<tr><td class="px" style="padding:40px 40px 14px;">
  {kicker('Así de fácil')}{h2('Haz tu pedido en tres pasos')}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:12px;"><tr>{cells}</tr></table>
</td></tr>
<tr><td class="px" style="padding:14px 40px 40px;">{button('Abrir el catálogo interactivo', CAT, bg=INK, fg='#FFFFFF')}</td></tr>'''


def urgency(title, text):
    return f'''
<tr><td class="px" style="padding:40px;background:{GOLD_SOFT};">
  {kicker('Venta a profesionales', GOLD_DARK)}{h2(title)}{p(text, color='#4B3B17', mb=24)}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td class="stack stack-pad" valign="top" style="padding:0 8px 0 0;">{button('Solicitar precios', BASE + '/#contacto', bg=NAVY, fg='#FFFFFF')}</td>
    <td class="stack" valign="top" style="padding:0 0 0 8px;">{button('Llamar al (+34) 961 53 21 09', 'tel:+34961532109', bg='#FFFFFF', fg=NAVY, border=NAVY)}</td>
  </tr></table>
  {p('O escríbenos a <a href="mailto:comercial@criscolor.com" style="color:' + NAVY + ';font-weight:700;">comercial@criscolor.com</a>. Te respondemos en 24 h laborables.', color='#4B3B17', size=14, mb=0).replace('margin:0 0 0px', 'margin:18px 0 0')}
</td></tr>'''


# ── Productos «imprescindibles» (datos del catálogo) ───────────

P = {
    '44981': dict(name='Papá Noel en escalera', img='decoracion.gif', gif=True,
                  pack='40, 70 y 100 cm · paquete de 6',
                  why='Se ve desde la calle. Colgado en tu escaparate se vende solo, y el cliente lo quiere para su ventana o balcón.'),
    '44011': dict(name='Globos Reyes Magos 110 cm', img='globos.gif', gif=True,
                  pack='Pack de 3 globos · paquete de 12',
                  why='Melchor, Gaspar y Baltasar a tamaño gigante. Es el reclamo de la semana de Reyes y alarga tu campaña hasta el 6 de enero.'),
    '45045': dict(name='Papel Regalo Stars', img='p-papel-2.jpg',
                  pack='Expositor de 60 rollos · 5 diseños surtidos',
                  why='Llega en expositor listo para el mostrador. Cinco colores con estrellas doradas que combinan con cualquier regalo.'),
    '45049': dict(name='Papel Regalo Reyes Magos', img='p-papel-1.jpg',
                  pack='Expositor de 60 rollos · 5 diseños surtidos',
                  why='El papel que se pide para los regalos del 6 de enero. Con él alargas tus ventas hasta el 6 de enero.'),
    '45033': dict(name='Sacos navideños', img='p-sacos-2.jpg',
                  pack='12 uds surtidas · cinta incluida',
                  why='Para juguetes y regalos grandes que no se pueden envolver. Venta segura en diciembre y cero trabajo en el mostrador.'),
    '44251': dict(name='Cañón de confeti Gold 40 cm', img='p-fiesta-1.jpg',
                  pack='Paquete de 12 · también 30 y 60 cm',
                  why='Nochevieja, cumpleaños y celebraciones. Compra de impulso que se vende por unidades y se repite todo el año.'),
    '44988': dict(name='Gafas Fin de Año 2027', img='pf-44988.jpg',
                  pack='4 modelos surtidos · paquete de 12',
                  why='Junto a la caja, imprescindibles para la foto de Nochevieja. Fáciles de vender por unidad.'),
    '42650': dict(name='Bolsa de papel kraft con asa', img='p-bolsas-1.jpg',
                  pack='6 medidas · paquete de 25',
                  why='La bolsa que se vende todo el año y se dispara en diciembre. En kraft, blanco y colores.'),
    '43030': dict(name='Lazos estrella adhesivos', img='p-lazos-2.jpg',
                  pack='Bandeja de 100 uds · metalizados',
                  why='El remate de cada regalo. Una venta añadida en el mostrador que casi nadie rechaza.'),
    '44611': dict(name='Vasos y platos metalizados oro', img='p-vajilla-1.jpg',
                  pack='6 uds por paquete · oro, plata y rojo',
                  why='La mesa de Nochebuena y Nochevieja. Se venden juntos, vasos y platos a juego.'),
}


def rank_row(n, code, big=False):
    """Una posición del ranking: número, imagen y por qué se vende."""
    d = P[code]
    href = ref_url(code)
    num = f'<p style="margin:0;font-family:{SERIF};font-size:46px;line-height:46px;color:{GOLD_DARK};">{n:02d}</p>'
    info = f"""<p style="margin:0 0 4px;font-family:{SANS};font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:{TEXT2};font-weight:700;">Ref. {code}</p>
      <h3 style="margin:0 0 8px;font-family:{SERIF};font-weight:400;font-size:{26 if big else 22}px;line-height:{30 if big else 26}px;color:{TEXT};">{d['name']}</h3>
      <p style="margin:0 0 10px;font-family:{SANS};font-size:14px;line-height:22px;color:{TEXT2};"><strong style="color:{TEXT};">Por qué se vende:</strong> {d['why']}</p>
      <p style="margin:0 0 12px;font-family:{SANS};font-size:13px;line-height:19px;color:{GOLD_DARK};font-weight:700;">{d['pack']}</p>
      <a href="{href}" style="font-family:{SANS};font-size:14px;font-weight:700;color:{INK};text-decoration:none;">Ver ficha en el catálogo &rarr;</a>"""
    if big:
        return f"""
<tr><td class="px" style="padding:0 40px 36px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr><td style="padding:0 0 14px;">{num}</td></tr>
    <tr><td><a href="{href}"><img src="{IMG}{d['img']}" width="520" alt="{d['name']}" class="fluid" style="width:520px;max-width:100%;border-radius:14px;"></a></td></tr>
    <tr><td style="padding:18px 0 0;">{info}</td></tr>
  </table>
</td></tr>"""
    return f"""
<tr><td class="px" style="padding:0 40px 30px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};"><tr>
    <td class="stack" width="64" valign="top" style="padding:22px 0 0;">{num}</td>
    <td class="stack stack-pad" width="190" valign="top" style="padding:24px 18px 0 0;"><a href="{href}"><img src="{IMG}{d['img']}" width="190" alt="{d['name']}" class="fluid" style="width:190px;max-width:100%;border-radius:12px;"></a></td>
    <td class="stack" valign="top" style="padding:24px 0 0;">{info}</td>
  </tr></table>
</td></tr>"""


def order_steps(title='Así se pide'):
    st = [('1', 'Haz tu selección', 'Abre el catálogo interactivo y añade las referencias que quieras con sus cantidades.'),
          ('2', 'Descárgala en Excel', 'Con un toque tienes tu pedido con referencias, EAN y unidades por caja.'),
          ('3', 'Envíala o llámanos', 'Mándala a tu comercial o llama al (+34) 961 53 21 09 y te damos precio.')]
    cells = ''.join(f"""<td class="stack stack-pad" width="33%" valign="top" style="padding:0 16px 0 0;">
      <p style="margin:0 0 10px;width:38px;height:38px;line-height:38px;border-radius:19px;background:{GOLD};color:{NAVY};font-family:{SANS};font-size:16px;font-weight:700;text-align:center;">{n}</p>
      <p style="margin:0 0 4px;font-family:{SANS};font-size:15px;font-weight:700;color:#FFFFFF;">{t}</p>
      <p style="margin:0;font-family:{SANS};font-size:13px;line-height:20px;color:#B9BCD6;">{d}</p>
    </td>""" for n, t, d in st)
    return f"""
<tr><td class="px" style="padding:44px 40px 10px;background:{NAVY};">
  {kicker(title, GOLD)}{h2('Tu pedido, en tres pasos', color='#FFFFFF')}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:14px;"><tr>{cells}</tr></table>
</td></tr>
<tr><td class="px" style="padding:22px 40px 44px;background:{NAVY};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td class="stack stack-pad" valign="top" style="padding:0 8px 0 0;">{button('Hacer mi selección', CAT)}</td>
    <td class="stack" valign="top" style="padding:0 0 0 8px;">{button('Llamar a mi comercial', 'tel:+34961532109', bg=NAVY, fg='#FFFFFF', border='#FFFFFF')}</td>
  </tr></table>
</td></tr>"""


# ── Correo A · Los 10 imprescindibles ───────────────────────

def email_imprescindibles():
    h = head('Los 10 imprescindibles de tu tienda esta Navidad · Criscolor',
             'Nuestra selección de lo que más rota en bazares y tiendas de regalo. Que no te falte ninguno.')
    h += topbar('Selección Navidad 2026')
    h += f"""
<tr><td class="px" style="padding:44px 40px 36px;background:{PAPER};border-top:1px solid {LINE};">
  {kicker('Top 10 · Navidad 2026')}
  <h1 class="h1" style="margin:0 0 18px;font-family:{SERIF};font-weight:400;font-size:46px;line-height:50px;color:{TEXT};">Los 10 imprescindibles de tu tienda esta&nbsp;Navidad</h1>
  {p('Hola{% if first_name %} {{ first_name }}{% endif %}, de las 790 referencias de nuestro catálogo de Navidad, estas son las diez que no deberían faltar en tu tienda. Son productos de rotación alta, fáciles de vender y que tus clientes van a buscar. Te contamos por qué funciona cada uno.', mb=26)}
  {button('Ver el catálogo completo', CAT, bg=INK, fg='#FFFFFF', full=False)}
</td></tr>
<tr><td class="px" style="padding:40px 40px 22px;">
  {kicker('Los dos que más llaman la atención')}{h2('Empieza por el escaparate')}
</td></tr>"""
    h += rank_row(1, '44981', big=True)
    h += rank_row(2, '44011', big=True)
    h += f"""
<tr><td class="px" style="padding:8px 40px 6px;">
  {kicker('Envolver y regalar')}{h2('Lo que se vende cada día de diciembre')}
</td></tr>"""
    for n, c in [(3, '45045'), (4, '45049'), (5, '45033'), (6, '42650'), (7, '43030')]:
        h += rank_row(n, c)
    h += f"""
<tr><td class="px" style="padding:8px 40px 6px;">
  {kicker('Nochebuena y Nochevieja')}{h2('La fiesta también se compra en tu tienda')}
</td></tr>"""
    for n, c in [(8, '44251'), (9, '44988'), (10, '44611')]:
        h += rank_row(n, c)
    h += f"""
<tr><td class="px" style="padding:6px 40px 40px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{GOLD_SOFT};border-radius:14px;"><tr>
    <td class="stack stack-pad" width="150" valign="middle" style="padding:20px 0 20px 20px;"><a href="{ref_url('44884')}"><img src="{IMG}p-calefaccion-1.jpg" width="130" alt="Calefactor Atlas" style="width:130px;border-radius:10px;"></a></td>
    <td class="stack" valign="middle" style="padding:20px 22px;">
      <p style="margin:0 0 4px;font-family:{SANS};font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:{GOLD_DARK};font-weight:700;">Y además, el frío</p>
      <p style="margin:0 0 6px;font-family:{SERIF};font-size:22px;line-height:26px;color:{TEXT};">Calefactores y estufas</p>
      <p style="margin:0 0 10px;font-family:{SANS};font-size:14px;line-height:21px;color:#4B3B17;">La compra de invierno que llega con el primer frío. Calefactor Atlas de 2000 W, en blanco y negro.</p>
      <a href="{fam_url('calefaccion')}" style="font-family:{SANS};font-size:14px;font-weight:700;color:{INK};text-decoration:none;">Ver calefacción &rarr;</a>
    </td>
  </tr></table>
</td></tr>"""
    h += order_steps('¿Te lo preparamos?')
    return h + foot()


# ── Correo B · Calendario de ventas ─────────────────────────

def mini_card(code, img, name, pack, cls='col3'):
    return f"""<!--[if mso]><td width="177" valign="top"><![endif]--><div class="{cls}" style="display:inline-block;width:100%;max-width:177px;vertical-align:top;font-size:14px;">
      <div style="padding:0 6px 18px;"><a href="{ref_url(code)}" style="text-decoration:none;">
        <img src="{IMG}{img}" width="165" alt="{name}" class="fluid" style="width:100%;max-width:100%;border-radius:10px;background:#FFFFFF;">
        <p style="margin:10px 0 0;font-family:{SANS};font-size:14px;line-height:18px;font-weight:700;color:#FFFFFF;">{name}</p>
        <p style="margin:3px 0 0;font-family:{SANS};font-size:12px;line-height:17px;color:#B9BCD6;">{pack}</p>
      </a></div>
    </div><!--[if mso]></td><![endif]-->"""


def phase(n, when, title, text, cards, gif=None, gif_href=None, gif_alt=''):
    g = ''
    if gif:
        g = f"""<tr><td class="px" style="padding:0 40px 22px;background:{NAVY};"><a href="{gif_href}"><img src="{IMG}{gif}" width="520" alt="{gif_alt}" class="fluid" style="width:520px;max-width:100%;border-radius:14px;"></a></td></tr>"""
    return f"""
<tr><td class="px" style="padding:40px 40px 18px;background:{NAVY};border-top:1px solid #1B2160;">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>
    <td style="background:{GOLD};border-radius:20px;padding:6px 14px;font-family:{SANS};font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:{NAVY};">Fase {n} · {when}</td>
  </tr></table>
  <h2 class="h2" style="margin:16px 0 10px;font-family:{SERIF};font-weight:400;font-size:32px;line-height:36px;color:#FFFFFF;">{title}</h2>
  {p(text, color='#C9CCE6', mb=6)}
</td></tr>
{g}
<tr><td class="px" style="padding:4px 34px 18px;background:{NAVY};font-size:0;line-height:0;">
  <!--[if mso]><table role="presentation" width="531" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->{'<!--[if mso]></tr><tr><![endif]-->'.join(''.join(mini_card(*c, cls='col3' if len(cards) > 3 else 'col3 keep3') for c in cards[i:i + 3]) for i in range(0, len(cards), 3))}<!--[if mso]></tr></table><![endif]-->
</td></tr>"""


def email_calendario():
    h = head('Tu calendario de ventas de Navidad · Criscolor',
             'Qué vender en cada momento, de noviembre a Reyes, y cuándo pedirlo para no quedarte sin stock.')
    h += topbar('Planifica tu campaña')
    h += f"""
<tr><td><a href="{CAT}"><img src="{IMG}hero.jpg" width="600" alt="Escaparate navideño de Criscolor" class="fluid" style="width:600px;max-width:100%;"></a></td></tr>
<tr><td class="px" style="padding:40px 40px 36px;background:{NAVY};">
  {kicker('De noviembre a Reyes', GOLD)}
  <h1 class="h1" style="margin:0 0 16px;font-family:{SERIF};font-weight:400;font-size:44px;line-height:48px;color:#FFFFFF;">Tu calendario de ventas de <span style="color:{GOLD};">Navidad</span></h1>
  {p('Hola{% if first_name %} {{ first_name }}{% endif %}, la campaña de Navidad no es un solo momento: son cuatro, y en cada uno tu cliente busca cosas distintas. Te lo hemos ordenado para que tengas en tienda lo que toca, justo cuando toca.', color='#C9CCE6', mb=22)}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;background:#0B1257;border-radius:14px;"><tr>
    <td style="padding:16px 18px;font-family:{SANS};font-size:14px;line-height:22px;color:#FFFFFF;"><strong style="color:{GOLD};">Consejo:</strong> pide cada fase con 3 o 4 semanas de antelación. Lo más vendido es lo primero que se agota.</td>
  </tr></table>
</td></tr>"""
    h += phase(1, 'Noviembre', 'Viste el escaparate',
               'Lo primero que ve tu cliente es tu escaparate. Decoración que se vende sola y anuncia que en tu tienda ya es Navidad.',
               [('44981', 'p-decoracion-1.jpg', 'Papá Noel en escalera', '40, 70 y 100 cm'),
                ('44984', 'pf-44984.jpg', 'Figura Papá Noel 40 cm', 'Con caja expositora'),
                ('44117', 'pf-44117.jpg', 'Globos «Feliz Navidad»', 'Letras de 33 cm'),
                ('44814', 'p-pegatinas-2.jpg', 'Pegatinas de ventana', 'Metalizadas, surtidas'),
                ('44816', 'p-pegatinas-1.jpg', 'Pegatinas 3D', 'Diseños surtidos'),
                ('44018', 'pf-44018.jpg', 'Plantillas huellas', 'Pack de 3')])
    h += phase(2, '1 – 24 de diciembre', 'Temporada de regalos',
               'El pico de ventas. Todo lo necesario para envolver y llevar: papel, bobinas, bolsas, lazos, cajas y sacos.',
               [('45045', 'p-papel-2.jpg', 'Papel Regalo Stars', 'Expositor de 60 rollos'),
                ('42650', 'p-bolsas-1.jpg', 'Bolsa kraft con asa', '6 medidas'),
                ('06375', 'p-lazos-1.jpg', 'Lazo automático rojo', 'Paquete de 12'),
                ('44090', 'p-cajas-1.jpg', 'Cajas metal oro', '3 tamaños surtidos'),
                ('45033', 'p-sacos-2.jpg', 'Sacos navideños', 'Cinta incluida'),
                ('43030', 'p-lazos-2.jpg', 'Lazos estrella', 'Bandeja de 100 uds')],
               gif='bobinas.gif', gif_href=ref_url('44950'), gif_alt='Bobina de papel de regalo de elfos desenrollándose')
    h += phase(3, '24 – 31 de diciembre', 'La mesa y la fiesta',
               'Nochebuena y Nochevieja se compran a última hora. Vajilla a juego, confeti, gafas y las bolsas para las uvas.',
               [('44611', 'p-vajilla-1.jpg', 'Vasos metalizados', 'Oro, plata y rojo'),
                ('44782', 'p-vajilla-2.jpg', 'Platos metalizados', 'A juego con los vasos'),
                ('44988', 'pf-44988.jpg', 'Gafas Fin de Año 2027', '4 modelos surtidos'),
                ('43424', 'pf-43424.jpg', 'Bolsas uvas de la suerte', '12 uds por paquete'),
                ('44251', 'p-fiesta-1.jpg', 'Cañón de confeti Gold', '30, 40 y 60 cm'),
                ('44115', 'pf-44115.jpg', 'Globos «Happy New Year»', 'Letras oro de 30 cm')],
               gif='fiesta.gif', gif_href=ref_url('44251'), gif_alt='Cañón de confeti dorado disparándose')
    h += phase(4, '1 – 6 de enero', 'Llegan los Reyes',
               'La campaña no acaba en Nochevieja. Los regalos de Reyes te dan una semana más de ventas: papel, bolsas y cajas con Melchor, Gaspar y Baltasar.',
               [('44011', 'p-globos-1.jpg', 'Globos Reyes Magos', '110 cm · pack de 3'),
                ('45049', 'p-papel-1.jpg', 'Papel Reyes Magos', 'Expositor de 60 rollos'),
                ('44979', 'pf-44979.jpg', 'Bandera Reyes Magos', '2 × 1,5 m · 2 modelos'),
                ('44985', 'pf-44985.jpg', 'Figuras Reyes Magos', '44 cm · los tres Reyes'),
                ('43967', 'pf-43967.jpg', 'Bolsas Reyes Magos', '12 uds surtidas'),
                ('44968', 'pf-44968.jpg', 'Cajas Reyes Magos', '10 tamaños surtidos')])
    h += f"""
<tr><td class="px" style="padding:40px;background:{GOLD_SOFT};">
  {kicker('Venta a profesionales', GOLD_DARK)}{h2('¿Quieres que te ayudemos a planificarlo?')}
  {p('Tu comercial te prepara el pedido de cada fase según el tamaño de tu tienda y lo que más te funcionó el año pasado. Llámanos o escríbenos y lo vemos juntos.', color='#4B3B17', mb=22)}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td class="stack stack-pad" valign="top" style="padding:0 8px 0 0;">{button('Llamar al (+34) 961 53 21 09', 'tel:+34961532109', bg=NAVY, fg='#FFFFFF')}</td>
    <td class="stack" valign="top" style="padding:0 0 0 8px;">{button('Escribir a comercial', 'mailto:comercial@criscolor.com?subject=Pedido%20campa%C3%B1a%20Navidad%202026', bg='#FFFFFF', fg=NAVY, border=NAVY)}</td>
  </tr></table>
</td></tr>"""
    h += order_steps('O hazlo tú en dos minutos')
    return h + foot()


# ── Correo B · Sencillo: «Ya tenemos la Navidad» ─────────────

def big_button(text, href, bg, fg, border=None):
    b = border or bg
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>
  <td align="center" bgcolor="{bg}" style="border-radius:14px;background:{bg};">
    <a href="{href}" style="display:block;padding:18px 20px;font-family:{SANS};font-size:19px;line-height:24px;font-weight:700;color:{fg};text-decoration:none;border-radius:14px;border:2px solid {b};background:{bg};">{text}</a>
  </td></tr></table>"""


def simple_card(code, img, name, line):
    href = ref_url(code)
    return f"""<!--[if mso]><td width="265" valign="top"><![endif]--><div class="col2" style="display:inline-block;width:100%;max-width:265px;vertical-align:top;font-size:16px;">
      <div style="padding:0 8px 22px;"><a href="{href}" style="text-decoration:none;">
        <img src="{IMG}{img}" width="249" alt="{name}" class="fluid" style="width:100%;max-width:100%;border-radius:12px;border:1px solid {LINE};">
        <p style="margin:12px 0 2px;font-family:{SANS};font-size:18px;line-height:23px;font-weight:700;color:{TEXT};">{name}</p>
        <p style="margin:0 0 10px;font-family:{SANS};font-size:15px;line-height:21px;color:{TEXT2};">{line}</p>
        <span style="font-family:{SANS};font-size:16px;font-weight:700;color:{INK};">Ver producto &rarr;</span>
      </a></div>
    </div><!--[if mso]></td><![endif]-->"""


def email_sencillo():
    h = head('Ya ha llegado la Navidad a Criscolor',
             'Papá Noel en escalera, globos de Reyes, papel de regalo y mucho más. Míralo en un minuto.')
    h += topbar('Campaña Navidad 2026')
    h += f"""
<tr><td><a href="{CAT}"><img src="{IMG}hero.jpg" width="600" alt="Escaparate de Navidad de Criscolor" class="fluid" style="width:600px;max-width:100%;"></a></td></tr>
<tr><td class="px" align="center" style="padding:40px 40px 36px;background:{NAVY};">
  <h1 class="h1" style="margin:0 0 16px;font-family:{SERIF};font-weight:400;font-size:44px;line-height:50px;color:#FFFFFF;text-align:center;">Ya ha llegado la <span style="color:{GOLD};">Navidad</span> a Criscolor</h1>
  <p style="margin:0 0 28px;font-family:{SANS};font-size:19px;line-height:29px;color:#DADCF0;text-align:center;">Hola{{% if first_name %}} {{{{ first_name }}}}{{% endif %}}, ya tienes disponibles los productos que más se venden estas fiestas. Échales un vistazo y haz tu pedido antes de que se agoten.</p>
  {big_button('Ver catálogo', CAT, GOLD, NAVY)}
  <div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>
  {big_button('Contacta con nosotros', BASE + '/#contacto', NAVY, '#FFFFFF', border='#FFFFFF')}
</td></tr>
<tr><td class="px" align="center" style="padding:40px 40px 22px;">
  <h2 class="h2" style="margin:0 0 8px;font-family:{SERIF};font-weight:400;font-size:32px;line-height:37px;color:{TEXT};text-align:center;">Lo que más vas a vender</h2>
  <p style="margin:0;font-family:{SANS};font-size:17px;line-height:26px;color:{TEXT2};text-align:center;">Toca cualquier producto para verlo.</p>
</td></tr>
<tr><td class="px" style="padding:0 32px 10px;font-size:0;line-height:0;">
  <!--[if mso]><table role="presentation" width="536" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->"""
    cards = [
        ('44981', 'p-decoracion-1.jpg', 'Papá Noel en escalera', 'Para el escaparate y la ventana'),
        ('44011', 'p-globos-1.jpg', 'Globos Reyes Magos', 'Gigantes, de 110 cm'),
        ('45045', 'p-papel-2.jpg', 'Papel de regalo', 'Rollos de 2 y 5 metros'),
        ('42650', 'p-bolsas-1.jpg', 'Bolsas de regalo', 'Kraft, blancas y de colores'),
        ('45033', 'p-sacos-2.jpg', 'Sacos de regalo', 'Para los regalos grandes'),
        ('44251', 'p-fiesta-1.jpg', 'Cañón de confeti', 'Para Nochevieja'),
    ]
    rows = []
    for i in range(0, len(cards), 2):
        rows.append(''.join(simple_card(*c) for c in cards[i:i + 2]))
    h += '<!--[if mso]></tr><tr><![endif]-->'.join(rows)
    h += f"""<!--[if mso]></tr></table><![endif]-->
</td></tr>
<tr><td class="px" style="padding:0 40px 44px;">{big_button('Ver catálogo completo', CAT, INK, '#FFFFFF')}</td></tr>
<tr><td class="px" align="center" style="padding:40px;background:{GOLD_SOFT};">
  <h2 class="h2" style="margin:0 0 10px;font-family:{SERIF};font-weight:400;font-size:32px;line-height:37px;color:{TEXT};text-align:center;">Solicita tu catálogo y precios</h2>
  <p style="margin:0 0 24px;font-family:{SANS};font-size:18px;line-height:27px;color:#4B3B17;text-align:center;">Déjanos tus datos y te contestamos en menos de 24 horas.</p>
  {big_button('Contacta con nosotros', BASE + '/#contacto', NAVY, '#FFFFFF')}
  <div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>
  {big_button('Ver catálogo', CAT, '#FFFFFF', NAVY, border=NAVY)}
</td></tr>"""
    return h + foot()


def preview(html):
    """Resuelve las etiquetas de Klaviyo para ver el correo en el navegador."""
    return (html.replace('{% if first_name %} {{ first_name }}{% endif %}', '')
                .replace('{% web_view_link %}', '#').replace('{% unsubscribe_link %}', '#')
                .replace('{% manage_preferences_link %}', '#'))


if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'preview'), exist_ok=True)
    for name, fn in [('navidad-a-imprescindibles', email_imprescindibles), ('navidad-b-sencillo', email_sencillo)]:
        html = fn()
        open(os.path.join(ROOT, name + '.html'), 'w', encoding='utf-8').write(html)
        open(os.path.join(ROOT, 'preview', name + '.html'), 'w', encoding='utf-8').write(preview(html))
        print(name, len(html.encode()) // 1024, 'KB')
