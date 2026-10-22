#!/usr/bin/env python3
"""Genera las campañas de email de Navidad 2026 (HTML compatible con Klaviyo).

Salida en /email:
  navidad-1-lanzamiento.html          → para pegar en Klaviyo (con etiquetas de Klaviyo)
  navidad-2-mas-pedidos.html          → idem
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


# ── Campaña 1 · Lanzamiento ─────────────────────────────────

def email_lanzamiento():
    h = head('Ya está aquí el Catálogo Navidad 2026 · Criscolor',
             '790 referencias en 12 familias. Ábrelo, elige y prepara tu pedido antes de que empiece la campaña.')
    h += topbar('Campaña Navidad 2026')
    h += f'''
<!-- Hero -->
<tr><td><a href="{CAT}"><img src="{IMG}hero.jpg" width="600" alt="Escaparate navideño de Criscolor" class="fluid" style="width:600px;max-width:100%;"></a></td></tr>
<tr><td class="px" style="padding:40px 40px 42px;background:{NAVY};">
  {kicker('Nueva campaña · Navidad 2026', GOLD)}
  <h1 class="h1" style="margin:0 0 16px;font-family:{SERIF};font-weight:400;font-size:44px;line-height:48px;color:#FFFFFF;">La Navidad ya ha llegado a <span style="color:{GOLD};">Criscolor</span></h1>
  {p('Hola{% if first_name %} {{ first_name }}{% endif %}, ya tienes disponible el catálogo completo de la campaña: papel de regalo, bolsas, lazos, cajas, globos, decoración, vajilla y calefacción. Todo lo que tu tienda necesita para la temporada, en un solo sitio y listo para pedir.', color='#C9CCE6', mb=28)}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td class="stack stack-pad" valign="top" style="padding:0 8px 0 0;">{button('Abrir el catálogo interactivo', CAT)}</td>
    <td class="stack" valign="top" style="padding:0 0 0 8px;">{button('Ver la web de la campaña', BASE + '/', bg=NAVY, fg='#FFFFFF', border='#FFFFFF')}</td>
  </tr></table>
</td></tr>'''
    h += stats([('790', 'referencias'), ('12', 'familias'), ('24 h', 'respuesta')])
    h += media_block('bobinas.gif', fam_url('bobinas'), 'Bobina de papel de regalo de elfos desenrollándose',
                     'Míralo en movimiento', 'Bobinas de 62 cm con diseños exclusivos',
                     'Elfos, liso oro, plata y metalizados en formato profesional para envolver en mostrador. Tus clientes se llevan el regalo listo.',
                     'Ver las bobinas de regalo')
    h += f'''
<tr><td class="px" style="padding:40px 40px 18px;border-top:1px solid {LINE};">
  {kicker('Lo más destacado')}{h2('Los productos estrella de la temporada')}{p('Una selección de lo que más pedirán tus clientes. Toca cualquier producto para ver su ficha completa en el catálogo.', mb=6)}
</td></tr>'''
    h += product_pair([
        ('p-papel-2.jpg', 'Papel Regalo Stars 70 cm × 2 m', '45045', '60 rollos en 5 diseños surtidos.', ref_url('45045')),
        ('p-globos-1.jpg', 'Globos Reyes Magos 110 cm', '44011', 'Melchor, Gaspar y Baltasar en foil metalizado.', ref_url('44011')),
    ])
    h += product_pair([
        ('p-lazos-2.jpg', 'Lazos Estrella adhesivos', '43030', 'Metalizados, en bandejas de 36 a 100 unidades.', ref_url('43030')),
        ('p-cajas-1.jpg', 'Cajas Navidad Metal Oro', '44090', 'Set de 3 tamaños surtidos.', ref_url('44090')),
    ])
    h += f'<tr><td class="px" style="padding:4px 40px 40px;">{button("Ver todos los destacados", BASE + "/#destacados", bg="#FFFFFF", fg=INK, border=INK)}</td></tr>'
    h += families_grid()
    h += media_block('decoracion.gif', ref_url('44981'), 'Papá Noel en escalera colgado en una ventana',
                     'Decoración que vende', 'Papá Noel en escalera',
                     'El clásico que no falta en ningún escaparate. Disponible en 40, 70 y 100 cm.',
                     'Ver Papá Noel en escalera')
    h += urgency('No esperes a diciembre',
                 'Las referencias más pedidas se agotan pronto. Reserva ahora tu stock de campaña y asegúrate el surtido completo para tu tienda.')
    h += steps()
    return h + foot()


# ── Campaña 2 · Lo más pedido ───────────────────────────────

def alt_row(img, href, kick, title, text, meta, flip=False, is_gif=False):
    """Fila imagen + texto (alterna lados en ordenador, apila en móvil)."""
    img_td = f'''<td class="stack stack-pad" width="50%" valign="middle" style="padding:{'0 0 0 12px' if flip else '0 12px 0 0'};">
      <a href="{href}"><img src="{IMG}{img}" width="254" alt="{title}" class="fluid" style="width:100%;max-width:100%;border-radius:14px;"></a>
    </td>'''
    txt_td = f'''<td class="stack" width="50%" valign="middle" style="padding:{'0 12px 0 0' if flip else '0 0 0 12px'};">
      {kicker(kick)}
      <h3 style="margin:0 0 8px;font-family:{SERIF};font-weight:400;font-size:25px;line-height:29px;color:{TEXT};">{title}</h3>
      {p(text, size=15, mb=10)}
      <p style="margin:0 0 14px;font-family:{SANS};font-size:13px;line-height:19px;color:{GOLD_DARK};font-weight:700;">{meta}</p>
      <a href="{href}" style="font-family:{SANS};font-size:15px;font-weight:700;color:{INK};text-decoration:none;">Ver ficha en el catálogo &rarr;</a>
    </td>'''
    # En móvil la imagen debe ir siempre primero: con dir=rtl se invierte el orden visual solo en ordenador
    if flip:
        row = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl"><tr>{img_td.replace("<td ", "<td dir=\"ltr\" ", 1)}{txt_td.replace("<td ", "<td dir=\"ltr\" ", 1)}</tr></table>'
    else:
        row = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{img_td}{txt_td}</tr></table>'
    return f'<tr><td class="px" style="padding:0 40px 34px;">{row}</td></tr>'


def email_mas_pedidos():
    h = head('Lo que más se va a vender esta Navidad · Criscolor',
             'Novedades 2026, los productos más pedidos y cómo tenerlo todo en tu tienda a tiempo.')
    h += topbar('Novedades · Navidad 2026')
    h += f'''
<tr><td class="px" style="padding:40px 40px 30px;background:{NAVY};">
  {kicker('Novedades 2026', GOLD)}
  <h1 class="h1" style="margin:0 0 16px;font-family:{SERIF};font-weight:400;font-size:44px;line-height:48px;color:#FFFFFF;">Lo que más se va a vender <span style="color:{GOLD};">esta Navidad</span></h1>
  {p('Hola{% if first_name %} {{ first_name }}{% endif %}, hemos reunido las referencias que más rotan en campaña y las novedades de este año. Prepara tu tienda con tiempo y que no te falte nada cuando lleguen las prisas.', color='#C9CCE6', mb=0)}
</td></tr>
<tr><td style="background:{NAVY};padding:0 40px;" class="px">
  <a href="{ref_url('44251')}"><img src="{IMG}fiesta.gif" width="520" alt="Cañón de confeti dorado disparándose" class="fluid" style="width:520px;max-width:100%;border-radius:14px;"></a>
</td></tr>
<tr><td class="px" style="padding:22px 40px 42px;background:{NAVY};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td class="stack stack-pad" valign="middle" style="padding:0 12px 0 0;">
      <p style="margin:0;font-family:{SANS};font-size:15px;line-height:22px;color:#FFFFFF;font-weight:700;">Cañón Fiesta Gold 40 cm</p>
      <p style="margin:2px 0 0;font-family:{SANS};font-size:13px;line-height:19px;color:#B9BCD6;">Ref. 44251 · Para Nochevieja y celebraciones</p>
    </td>
    <td class="stack" valign="middle" width="220" style="padding:0;">{button('Ver novedades', fam_url('fiesta'))}</td>
  </tr></table>
</td></tr>
<tr><td class="px" style="padding:44px 40px 26px;">
  {kicker('Los imprescindibles')}{h2('Las referencias que no pueden faltar')}{p('Cinco productos que tus clientes buscarán esta campaña. Toca cualquiera para ver su ficha, medidas y unidades por caja.', mb=0)}
</td></tr>'''
    h += alt_row('p-papel-2.jpg', ref_url('45045'), 'Papel de regalo', 'Papel Regalo Stars',
                 'Estrellas doradas sobre cinco colores, en expositor listo para colocar en tienda.',
                 '60 rollos de 70 cm × 2 m · 5 diseños surtidos')
    h += alt_row('sacos.gif', ref_url('45033'), 'Sacos navideños', 'Sacos para regalos grandes',
                 'La solución rápida para juguetes y regalos voluminosos: se mete, se cierra y listo.',
                 'Paquetes de 12 uds surtidas · Cinta incluida', flip=True)
    h += alt_row('globos.gif', ref_url('44011'), 'Globos', 'Globos Reyes Magos 110 cm',
                 'Melchor, Gaspar y Baltasar en foil metalizado. El reclamo perfecto para la semana de Reyes.',
                 'Pack de 3 globos · 110 cm de alto')
    h += alt_row('p-vajilla-1.jpg', ref_url('44611'), 'Vajilla desechable', 'Vasos metalizados oro',
                 'Para las mesas de Nochebuena y Nochevieja. También en plata, rojo y verde, y con platos a juego.',
                 'Vaso de cartón 270 cc · 6 uds por paquete', flip=True)
    h += alt_row('p-calefaccion-1.jpg', ref_url('44884'), 'Calefacción', 'Calefactor Atlas 2000 W',
                 'El invierno también se vende: calefactores cerámicos y estufas en varios modelos y acabados.',
                 'Blanco y negro · 26,5 cm · 2000 W')
    h += f'''
<tr><td class="px" style="padding:6px 40px 44px;">{button('Ver el catálogo completo', CAT, bg=INK, fg='#FFFFFF')}</td></tr>
<tr><td class="px" style="padding:40px;background:{PAPER};">
  {kicker('Para tu escaparate')}{h2('Envolver, decorar y regalar')}{p('Completa la venta con lazos, pegatinas y cajas a juego con el papel. Pequeños complementos que suben el ticket de cada cliente.', mb=22)}
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td width="33%" valign="top" style="padding:0 6px 0 0;"><a href="{fam_url('lazos')}" style="text-decoration:none;"><img src="{IMG}p-lazos-2.jpg" width="168" alt="Lazos estrella" class="fluid" style="width:100%;border-radius:10px;"><p style="margin:8px 0 0;font-family:{SANS};font-size:14px;font-weight:700;color:{TEXT};">Lazos y cintas</p></a></td>
    <td width="33%" valign="top" style="padding:0 3px;"><a href="{fam_url('pegatinas')}" style="text-decoration:none;"><img src="{IMG}p-pegatinas-2.jpg" width="168" alt="Pegatinas de ventana" class="fluid" style="width:100%;border-radius:10px;"><p style="margin:8px 0 0;font-family:{SANS};font-size:14px;font-weight:700;color:{TEXT};">Pegatinas</p></a></td>
    <td width="33%" valign="top" style="padding:0 0 0 6px;"><a href="{fam_url('cajas')}" style="text-decoration:none;"><img src="{IMG}p-cajas-1.jpg" width="168" alt="Cajas metalizadas" class="fluid" style="width:100%;border-radius:10px;"><p style="margin:8px 0 0;font-family:{SANS};font-size:14px;font-weight:700;color:{TEXT};">Cajas</p></a></td>
  </tr></table>
  <div style="height:24px;line-height:24px;font-size:0;">&nbsp;</div>
  {button('Ver todas las familias', BASE + '/#familias', bg='#FFFFFF', fg=INK, border=INK)}
</td></tr>'''
    h += urgency('Cuanto antes pidas, mejor surtido',
                 'En campaña de Navidad las referencias más vendidas se agotan rápido. Pide ahora tus precios y deja tu pedido preparado con tu comercial.')
    h += steps()
    return h + foot()


def preview(html):
    """Resuelve las etiquetas de Klaviyo para ver el correo en el navegador."""
    return (html.replace('{% if first_name %} {{ first_name }}{% endif %}', '')
                .replace('{% web_view_link %}', '#').replace('{% unsubscribe_link %}', '#')
                .replace('{% manage_preferences_link %}', '#'))


if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'preview'), exist_ok=True)
    for name, fn in [('navidad-1-lanzamiento', email_lanzamiento), ('navidad-2-mas-pedidos', email_mas_pedidos)]:
        html = fn()
        open(os.path.join(ROOT, name + '.html'), 'w', encoding='utf-8').write(html)
        open(os.path.join(ROOT, 'preview', name + '.html'), 'w', encoding='utf-8').write(preview(html))
        print(name, len(html.encode()) // 1024, 'KB')
