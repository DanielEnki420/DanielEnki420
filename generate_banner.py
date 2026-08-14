#!/usr/bin/env python3
"""Erzeugt den Profil-Header als SVG (dark + light).

Bewusst ohne externe Dienste: die fertigen SVGs liegen im Repo und werden
direkt von GitHub ausgeliefert. Kein Drittanbieter sieht Profilbesucher.

    python3 generate_banner.py

Schreibt assets/banner-dark.svg und assets/banner-light.svg.
"""

import math
import pathlib

W, H = 1200, 350

# Titelleiste im Stil eines Terminalfensters. Der Inhalt darunter ist um
# CONTENT_TOP nach unten gerueckt.
TITLE_DOT_Y = 46
TITLE_RULE_Y = 76
WINDOW_PATH = "~/danielenki — zsh"
# Leicht entsaettigte Ampelfarben; das Bernstein liegt bewusst nah am Gold.
DOT_COLORS = ("#E06C60", "#DEA123", "#61C554")

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "grid": "#161B22",
        "fg": "#E6EDF3",
        "muted": "#8B949E",
        "a1": "#7EE787",
        "a2": "#58A6FF",
        "a3": "#D2A8FF",
        "gold": "#C8973A",
    },
    "light": {
        "bg": "#FFFFFF",
        "grid": "#F0F3F6",
        "fg": "#1F2328",
        "muted": "#59636E",
        "a1": "#1A7F37",
        "a2": "#0969DA",
        "a3": "#8250DF",
        # Auf Weiss braucht das Gold mehr Tiefe, sonst verschwindet der Ring.
        "gold": "#8A6A1F",
    },
}

# --- Logo: Meander-Ring mit dem Wahlspruch -------------------------------
# Nach der letzten Verkleinerung blieb rechts vom Ring ein grosser leerer
# Streifen bis zur Eckenrahmung — der Ring wirkte verloren in der Karte.
# Wieder groesser UND nach rechts geschoben: der rechte Rand hat vertikal
# in der Bandmitte keine Eckwinkel im Weg (die sitzen nur oben/unten in den
# Ecken), da ist also mehr Platz als es auf den ersten Blick aussieht.
LOGO_CX, LOGO_CY = 1032, 208
R_RIM = 124          # aeussere Haarlinie
R_BAND_OUT = 116     # Maeanderband aussen
R_BAND_IN = 91       # Maeanderband innen
R_INNER = 84         # innere Haarlinie
MEANDER_UNITS = 28   # Wiederholungen des Schluesselmotivs
MOTTO = "ESSE QUAM VIDERI"

# Das Spektrum laeuft als Fussleiste unter dem Textblock und endet vor dem
# Logo-Ring, damit sich beide nicht ins Gehege kommen.
MARGIN = 64
SPEC_X1 = 878
BAR_W = 10
BAR_GAP = 6
BARS = (SPEC_X1 - MARGIN + BAR_GAP) // (BAR_W + BAR_GAP)
BASE_Y = 330
MAX_BAR = 50


def spectrum(t):
    """Zwei ueberlagerte Wellen + Abfall zu den Raendern.

    Sieht aus wie ein FFT-Frame — der rote Faden zum katzen-analyzer.
    """
    x = t / (BARS - 1)
    envelope = math.sin(math.pi * x) ** 0.65
    detail = 0.55 + 0.45 * math.sin(x * 17.0) * math.cos(x * 9.0 + 0.6)
    return max(0.12, envelope * detail)


def double_border(c):
    """Doppelte Zierlinie entlang des Kartenrands — klassisches Deco-Passepartout."""
    out = []
    for inset in (9, 19):
        r = max(14 - inset, 2)
        out.append(f'<rect x="{inset}" y="{inset}" width="{W - 2 * inset}" '
                    f'height="{H - 2 * inset}" rx="{r}" fill="none" '
                    f'stroke="{c["gold"]}" stroke-width="1.2" opacity="0.55"/>')
    return "".join(out)


def corner_brackets(c):
    """Gestufte Eckwinkel, wie an Deco-Kinoplakaten der 1920er/30er.

    Zwei ineinander verschachtelte L-Winkel je Ecke — der aeussere kraeftig,
    der innere zurueckhaltender, dazwischen eine kleine Stufe.
    """
    out = []
    arm_outer, arm_inner = 42, 25
    inset0, step = 25, 9

    def bracket(x0, y0, sx, sy):
        segs = []
        for i, arm in enumerate((arm_outer, arm_inner)):
            o = inset0 + i * step
            ax, ay = x0 + sx * o, y0 + sy * o
            segs.append(
                f'<path d="M{ax:.1f},{ay + sy * arm:.1f} L{ax:.1f},{ay:.1f} '
                f'L{ax + sx * arm:.1f},{ay:.1f}" fill="none" '
                f'stroke="{c["gold"]}" stroke-width="1.6" '
                f'opacity="{0.9 if i == 0 else 0.5}"/>')
        return "".join(segs)

    out.append(bracket(0, 0, 1, 1))
    out.append(bracket(W, 0, -1, 1))
    out.append(bracket(0, H, 1, -1))
    out.append(bracket(W, H, -1, -1))
    return "".join(out)


def sunburst(c):
    """Strahlenkranz hinter dem Maeanderring — Deco-Sonnentor-Motiv.

    Gleichlange Strahlen statt abwechselnd lang/kurz: die erste Fassung
    wirkte durch die Laengenvariation zackig statt wie ein ruhiger Kranz.
    Der Aussenradius bleibt klar innerhalb der rechten Eckwinkel, damit
    sich beide Zierelemente nicht schneiden.
    """
    r_in = R_RIM + 7
    r_out = R_RIM + 15
    out = [f'<g opacity="0.22" stroke="{c["gold"]}" stroke-width="1">']
    n = 20
    for i in range(n):
        ang = math.radians(i * 360.0 / n)
        x1 = LOGO_CX + r_in * math.cos(ang)
        y1 = LOGO_CY + r_in * math.sin(ang)
        x2 = LOGO_CX + r_out * math.cos(ang)
        y2 = LOGO_CY + r_out * math.sin(ang)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" '
                    f'y2="{y2:.1f}"/>')
    out.append('</g>')
    return "".join(out)


def meander_ring(c):
    """Der goldene Maeanderring mit dem Wahlspruch in der Mitte.

    Das Schluesselmotiv wird einmal in lokalen Koordinaten (8 breit, 6 hoch)
    definiert und dann MEANDER_UNITS mal um den Mittelpunkt rotiert. Jede
    Einheit ist eine gerade Sehne — bei 26 Stueck ist die Facettierung so
    fein, dass sie als Kreis liest (der gedruckte Ring macht es genauso).
    """
    out = []
    add = out.append

    mid_r = (R_BAND_OUT + R_BAND_IN) / 2
    arc = 2 * math.pi * mid_r / MEANDER_UNITS   # Bogenlaenge je Einheit
    s = arc / 8.0                               # lokale Breite 8 -> Bogen
    band_h = 6 * s

    # Haarlinien aussen und innen
    for r in (R_RIM, R_INNER):
        add(f'<circle cx="{LOGO_CX}" cy="{LOGO_CY}" r="{r}" fill="none" '
            f'stroke="{c["gold"]}" stroke-width="2.4"/>')

    # Das Motiv: Grundlinie + eingerollter Haken (klassischer Maeander).
    # stroke-width 1.2 statt 0.95 im Erstentwurf — auf dem breiteren Band
    # wirkte die duennere Linie ausgefranst statt kraeftig.
    unit = "M0,6 H8 M0,6 V0 H6 V4 H2 V2 H4"
    add(f'<g fill="none" stroke="{c["gold"]}" stroke-width="1.2" '
        f'stroke-linecap="square">')
    for i in range(MEANDER_UNITS):
        angle = i * 360.0 / MEANDER_UNITS
        tx = LOGO_CX - arc / 2
        ty = LOGO_CY - R_BAND_OUT
        add(f'<path d="{unit}" transform="rotate({angle:.2f} {LOGO_CX} '
            f'{LOGO_CY}) translate({tx:.2f} {ty:.2f}) scale({s:.4f})"/>')
    add('</g>')

    # Wahlspruch — Versalien, gesperrt, wie auf dem Original.
    # textLength/lengthAdjust nagelt die Breite fest: der Spruch bleibt im
    # Innenkreis, auch wenn beim Betrachter eine andere Serife einspringt.
    serif = "Georgia, 'Times New Roman', 'Iowan Old Style', serif"
    text_w = 2 * R_INNER - 32
    add(f'<text x="{LOGO_CX}" y="{LOGO_CY + 6}" text-anchor="middle" '
        f'font-family="{serif}" font-size="16" '
        f'textLength="{text_w}" lengthAdjust="spacingAndGlyphs" '
        f'fill="{c["gold"]}">{MOTTO}</text>')

    assert band_h < (R_BAND_OUT - R_BAND_IN) + 2, "Band laeuft ueber"
    return "".join(out)


def build(theme_name):
    c = THEMES[theme_name]
    out = []
    add = out.append

    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" '
        f'aria-label="Daniel — self-hosting, home automation, network privacy">')

    # Verlauf fuer die Spektrumsbalken.
    # userSpaceOnUse ist hier zwingend: mit dem Default (objectBoundingBox)
    # bekaeme JEDER Balken den kompletten Farbverlauf auf seinen 10 Pixeln —
    # alle saehen dann gleich aus. So laeuft er ueber die gesamte Reihe.
    add('<defs>')
    add(f'<linearGradient id="g" gradientUnits="userSpaceOnUse" '
        f'x1="{MARGIN}" y1="0" x2="{SPEC_X1}" y2="0">')
    add(f'<stop offset="0%" stop-color="{c["a1"]}"/>')
    add(f'<stop offset="50%" stop-color="{c["a2"]}"/>')
    add(f'<stop offset="100%" stop-color="{c["a3"]}"/>')
    add('</linearGradient>')
    add('</defs>')

    add(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}"/>')

    # Feines Raster im Hintergrund
    for gx in range(0, W, 40):
        add(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" '
            f'stroke="{c["grid"]}" stroke-width="1"/>')
    for gy in range(0, H, 40):
        add(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" '
            f'stroke="{c["grid"]}" stroke-width="1"/>')

    add(sunburst(c))

    mono = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
            "'Liberation Mono', monospace")

    # Titelleiste: drei Ampelpunkte + Pfad, wie in einem Terminalfenster
    for i, col in enumerate(DOT_COLORS):
        add(f'<circle cx="{64 + i * 22}" cy="{TITLE_DOT_Y}" r="6.5" '
            f'fill="{col}"/>')
    add(f'<text x="{W / 2}" y="{TITLE_DOT_Y + 5}" text-anchor="middle" '
        f'font-family="{mono}" font-size="15" fill="{c["muted"]}">'
        f'{WINDOW_PATH}</text>')
    add(f'<line x1="30" y1="{TITLE_RULE_Y}" x2="{W - 30}" y2="{TITLE_RULE_Y}" '
        f'stroke="{c["gold"]}" stroke-width="1" opacity="0.35"/>')

    # Prompt
    add(f'<text x="64" y="136" font-family="{mono}" font-size="25" '
        f'fill="{c["a1"]}">$ whoami</text>')

    # Name + blinkender Cursor.
    # Monospace-Vorschub ist 0.6em, "Daniel" = 6 Zeichen -> Cursor sitzt buendig.
    name, size = "Daniel", 86
    cursor_x = 64 + len(name) * size * 0.6 + 9
    add(f'<text x="64" y="224" font-family="{mono}" font-size="{size}" '
        f'font-weight="700" fill="{c["fg"]}">{name}</text>')
    add(f'<rect x="{cursor_x:.0f}" y="172" width="26" height="58" '
        f'fill="{c["a2"]}">'
        f'<animate attributeName="opacity" values="1;1;0;0" dur="1.2s" '
        f'repeatCount="indefinite"/></rect>')

    # Tagline
    add(f'<text x="64" y="270" font-family="{mono}" font-size="23" '
        f'fill="{c["muted"]}">self-hosting &#183; home automation &#183; '
        f'network privacy</text>')

    # Spektrum
    start_x = MARGIN
    for i in range(BARS):
        h = spectrum(i) * MAX_BAR
        x = start_x + i * (BAR_W + BAR_GAP)
        y = BASE_Y - h
        lo, hi = h * 0.45, h
        add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{BAR_W}" height="{h:.1f}" '
            f'rx="3" fill="url(#g)" opacity="0.9">'
            f'<animate attributeName="height" '
            f'values="{h:.1f};{lo:.1f};{hi:.1f};{h:.1f}" dur="2.8s" '
            f'begin="{i * 0.045:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y" '
            f'values="{y:.1f};{BASE_Y - lo:.1f};{BASE_Y - hi:.1f};{y:.1f}" '
            f'dur="2.8s" begin="{i * 0.045:.2f}s" repeatCount="indefinite"/>'
            f'</rect>')

    add(meander_ring(c))

    add(double_border(c))
    add(corner_brackets(c))

    add('</svg>')
    return "".join(out)


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name in THEMES:
        path = assets / f"banner-{name}.svg"
        path.write_text(build(name), encoding="utf-8")
        print(f"{path}  ({path.stat().st_size} B)")


if __name__ == "__main__":
    main()
