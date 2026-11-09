#!/usr/bin/env python3
"""Erzeugt den Profil-Header als SVG (dark + light).

Bewusst ohne externe Dienste: die fertigen SVGs liegen im Repo und werden
direkt von GitHub ausgeliefert. Kein Drittanbieter sieht Profilbesucher.

    python3 generate_banner.py

Schreibt assets/banner-dark.svg und assets/banner-light.svg.
"""

import math
import pathlib

from theme import SERIF, THEMES

W, H = 1200, 304

# --- Logo: Meander-Ring mit dem Wahlspruch -------------------------------
# Nach der letzten Verkleinerung blieb rechts vom Ring ein grosser leerer
# Streifen bis zur Eckenrahmung — der Ring wirkte verloren in der Karte.
# Wieder groesser UND nach rechts geschoben: der rechte Rand hat vertikal
# in der Bandmitte keine Eckwinkel im Weg (die sitzen nur oben/unten in den
# Ecken), da ist also mehr Platz als es auf den ersten Blick aussieht.
LOGO_CX, LOGO_CY = 1032, 152
R_RIM = 124          # aeussere Haarlinie
R_BAND_OUT = 116     # Maeanderband aussen
R_BAND_IN = 91       # Maeanderband innen
R_INNER = 84         # innere Haarlinie
MEANDER_UNITS = 28   # Wiederholungen des Schluesselmotivs

MARGIN = 64
BASE_Y = 280


def frieze(c, x1, x2, base):
    """Zikkurat-Fries: Strichhoehe steigt in Stufen zur Mitte und faellt wieder."""
    step, tiers, tier_h = 12, 6, 6
    n = int((x2 - x1) // step) + 1
    out = [f'<g stroke="{c["gold"]}" stroke-width="2" stroke-linecap="butt">']
    for i in range(n):
        x = x1 + i * step
        d = abs(i - (n - 1) / 2) / ((n - 1) / 2)      # 0 Mitte .. 1 Rand
        tier = tiers - min(tiers - 1, int(d * tiers))  # 1..tiers
        h = 6 + tier * tier_h
        op = 0.35 + 0.1 * tier
        # Welle von der Mitte nach aussen: Verzoegerung waechst mit dem Abstand.
        out.append(f'<line class="fr" style="animation-delay:{d * 1.6:.2f}s" '
                   f'x1="{x}" y1="{base}" x2="{x}" y2="{base - h}" '
                   f'opacity="{op:.2f}"/>')
    out.append(f'<line x1="{x1 - 2}" y1="{base + 0.5}" x2="{x2 + 2}" '
               f'y2="{base + 0.5}" stroke-width="1.4"/>')
    out.append('</g>')
    return "".join(out)


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
    out = [f'<g class="ccw" opacity="0.22" stroke="{c["gold"]}" '
           f'stroke-width="1">']
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
    add(f'<g class="cw" fill="none" stroke="{c["gold"]}" stroke-width="1.2" '
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
    # Zweizeilig und groesser: einzeilig in 16px war der Spruch auf der
    # Profilseite (Banner ~830px breit) nur noch ~11px hoch und unlesbar.
    for line, y, w in (("ESSE QUAM", LOGO_CY - 4, 2 * R_INNER - 40),
                       ("VIDERI", LOGO_CY + 26, 2 * R_INNER - 76)):
        add(f'<text x="{LOGO_CX}" y="{y}" text-anchor="middle" '
            f'font-family="{SERIF}" font-size="24" '
            f'textLength="{w}" lengthAdjust="spacingAndGlyphs" '
            f'fill="{c["gold"]}">{line}</text>')

    assert band_h < (R_BAND_OUT - R_BAND_IN) + 2, "Band laeuft ueber"
    return "".join(out)


def build(theme_name):
    c = THEMES[theme_name]
    out = []
    add = out.append

    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" '
        f'aria-label="Daniel Enki — self-hosting, tools that prove they work">')

    # Bewegung per CSS statt SMIL: so greift prefers-reduced-motion, und wer
    # "Bewegung reduzieren" eingestellt hat, sieht den Banner still.
    # Mäanderband dreht langsam, Strahlenkranz noch langsamer gegenlaeufig,
    # das Motto in der Mitte bleibt stehen.
    add('<style>'
        f'.cw,.ccw{{transform-origin:{LOGO_CX}px {LOGO_CY}px}}'
        '.cw{animation:spin 30s linear infinite}'
        '.ccw{animation:spin 60s linear infinite reverse}'
        '.fr{transform-box:fill-box;transform-origin:50% 100%;'
        'animation:breathe 3.2s ease-in-out infinite}'
        '@keyframes spin{to{transform:rotate(360deg)}}'
        '@keyframes breathe{0%,100%{transform:scaleY(1)}'
        '50%{transform:scaleY(.55)}}'
        '@media (prefers-reduced-motion:reduce){.cw,.ccw,.fr{animation:none}}'
        '</style>')
    add(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}"/>')

    add(sunburst(c))

    # Name: gesperrte Serifen-Versalien wie auf Deco-Plakaten. Ersetzt das
    # Terminal-Motiv ($ whoami + Cursor), das nicht zum Deco-Rahmen passte.
    add(f'<text x="{MARGIN}" y="148" font-family="{SERIF}" font-size="80" '
        f'textLength="736" lengthAdjust="spacing" '
        f'fill="{c["fg"]}">DANIEL ENKI</text>')

    # Goldlinie mit Raute in der Mitte
    rule_y, rule_x2 = 178, 800
    mid = (MARGIN + rule_x2) / 2
    add(f'<path d="M{MARGIN},{rule_y} H{mid - 14} M{mid + 14},{rule_y} '
        f'H{rule_x2}" stroke="{c["gold"]}" stroke-width="1.4"/>')
    add(f'<path d="M{mid},{rule_y - 7} L{mid + 7},{rule_y} L{mid},'
        f'{rule_y + 7} L{mid - 7},{rule_y} Z" fill="{c["gold"]}"/>')

    # Unterzeile in gesperrten Versalien
    add(f'<text x="{MARGIN}" y="214" font-family="{SERIF}" font-size="19" '
        f'textLength="{rule_x2 - MARGIN}" lengthAdjust="spacing" '
        f'fill="{c["muted"]}">SELF-HOSTING &#183; TOOLS THAT PROVE THEY WORK'
        f'</text>')

    # Gestufter Fries statt Spektrum: senkrechte Goldstriche, symmetrisch in
    # Terrassen ansteigend wie eine Deco-Fassade (Zikkurat).
    add(frieze(c, MARGIN + 40, rule_x2 - 40, BASE_Y))

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
