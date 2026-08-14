#!/usr/bin/env python3
"""Erzeugt je ein Deco-Emblem pro Projekt.

Zwischen den grossen Karten stand bisher nur Fliesstext — die Seite wirkte
abschnittsweise leer. Diese Embleme geben jedem Projekt ein eigenes Zeichen,
gezeichnet im selben Vokabular wie der Maeanderring: reine Goldlinien, keine
Flaechen, gestufter Ring als Fassung.

Auch humanism bekommt eine Linienfassung: das echte Logo
(assets/humanism-icon.png) bleibt fuer den Repo-Kopf, ist auf Emblemgroesse
aber zu fein gezeichnet und faellt neben den uebrigen Zeichen auseinander.

    python3 generate_icons.py

Schreibt assets/icon-<name>-<theme>.svg.
"""

import math
import pathlib

from theme import THEMES

SIZE = 120
CX = CY = SIZE / 2


def ring(c):
    """Gefasster Kreis als gemeinsame Klammer aller Embleme."""
    return (f'<circle cx="{CX}" cy="{CY}" r="57" fill="none" '
            f'stroke="{c["gold"]}" stroke-width="2" opacity="0.55"/>'
            f'<circle cx="{CX}" cy="{CY}" r="52" fill="none" '
            f'stroke="{c["gold"]}" stroke-width="1" opacity="0.35"/>')


def shield():
    """dns-blocklist-builder — Schild ueber durchgestrichenem Funksignal.

    Bewusst nur ein Bogenpaar statt zwei: mit vier Boegen lief das Innere
    bei 44px zu einem Fleck zusammen.
    """
    p = ['<path d="M60,20 L92,33 V57 C92,77 78,90 60,96 '
         'C42,90 28,77 28,57 V33 Z"/>']
    p.append('<circle cx="60" cy="58" r="5"/>')
    p.append('<path d="M44,44 A21,21 0 0,0 44,72"/>')
    p.append('<path d="M76,44 A21,21 0 0,1 76,72"/>')
    p.append('<path d="M38,84 L84,34" stroke-width="3.6"/>')
    return "".join(p)


def humanitas():
    """humanism — Bogen, Sonne, aufgeschlagenes Buch.

    Reduziert auf die drei tragenden Motive des echten Logos. Dessen
    Vollfassung (assets/humanism-icon.png) ist fein gezeichnet und wird
    auf Emblemgroesse unleserlich; hier zaehlt Lesbarkeit bei 64px.
    """
    p = ['<path d="M32,100 V56 A28,28 0 0,1 88,56 V100"/>']
    # Sonne mit Strahlen
    p.append('<circle cx="60" cy="50" r="9"/>')
    for i in range(8):
        a = math.radians(i * 45)
        p.append(f'<path d="M{60 + 13 * math.cos(a):.1f},'
                 f'{50 + 13 * math.sin(a):.1f} '
                 f'L{60 + 18 * math.cos(a):.1f},'
                 f'{50 + 18 * math.sin(a):.1f}" stroke-width="1.6"/>')
    # Aufgeschlagenes Buch
    p.append('<path d="M60,88 C52,81 42,80 33,82 V96 C42,94 52,95 60,100 Z"/>')
    p.append('<path d="M60,88 C68,81 78,80 87,82 V96 C78,94 68,95 60,100 Z"/>')
    return "".join(p)


def magnifier():
    """faktenchecker — Lupe mit Haken."""
    p = ['<circle cx="55" cy="52" r="25"/>']
    p.append('<path d="M73,70 L92,89" stroke-width="4" '
             'stroke-linecap="round"/>')
    p.append('<path d="M43,52 L52,62 L68,40" stroke-width="3.4" '
             'stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(p)


def leaves(x, y, up=34):
    """Zwei gespiegelte Blaetter an einem Stiel — fuer beide Grower-Apps."""
    return (f'<path d="M{x},{y} V{y - up}"/>'
            f'<path d="M{x},{y - up + 14} C{x - 16},{y - up + 14} '
            f'{x - 21},{y - up + 3} {x - 19},{y - up - 6} '
            f'C{x - 8},{y - up - 8} {x - 2},{y - up + 4} {x},{y - up + 14} Z"/>'
            f'<path d="M{x},{y - up + 22} C{x + 16},{y - up + 22} '
            f'{x + 21},{y - up + 11} {x + 19},{y - up + 2} '
            f'C{x + 8},{y - up} {x + 2},{y - up + 12} {x},{y - up + 22} Z"/>')


def dwc():
    """dwc-grower-edition — Naehrloesung mit Luftblasen."""
    p = ['<path d="M30,56 L90,56 L83,100 L37,100 Z"/>']
    # Wasserlinie
    p.append('<path d="M34,70 C44,64 52,76 62,70 C71,65 78,73 85,69"/>')
    p.append(leaves(60, 56))
    for bx, by, r in ((46, 88, 4), (58, 94, 3), (70, 85, 3.5), (52, 79, 2.5)):
        p.append(f'<circle cx="{bx}" cy="{by}" r="{r}"/>')
    return "".join(p)


def soil():
    """soil-coco-grower-edition — Topf mit Erdschicht."""
    p = ['<rect x="30" y="50" width="60" height="12"/>']
    p.append('<path d="M36,62 L84,62 L78,100 L42,100 Z"/>')
    # Erde als kurze Striche statt Flaeche
    for i in range(5):
        x = 44 + i * 8
        p.append(f'<path d="M{x},72 h5"/>')
    p.append(leaves(60, 50, up=30))
    return "".join(p)


def cat_wave():
    """katzen-analyzer — Katzenkopf mit Schallbogen, wie in der Illustration."""
    head = ('M30,60 L26,10 L50,34 L70,34 L94,10 L90,60 '
            'C90,86 76,98 60,98 C44,98 30,86 30,60 Z')
    p = [f'<g transform="translate(8 22) scale(0.62)">'
         f'<path d="{head}"/>'
         f'<path d="M36,54 L33,22 L52,38 Z"/>'
         f'<path d="M84,54 L87,22 L68,38 Z"/>'
         f'<ellipse cx="46" cy="58" rx="7" ry="4.5"/>'
         f'<ellipse cx="74" cy="58" rx="7" ry="4.5"/>'
         f'<path d="M55,70 L65,70 L60,77 Z"/>'
         f'</g>']
    for r, w in ((16, 2), (26, 1.6), (36, 1.2)):
        p.append(f'<path d="M78,{CY - r} A{r},{r} 0 0,1 78,{CY + r}" '
                 f'stroke-width="{w}" opacity="0.85"/>')
    return "".join(p)


def olive():
    """olivera — Olivenzweig mit Fruechten.

    Kein Wappen und kein Siegel: das Projekt ist nicht in Betrieb, das
    Zeichen soll nichts Amtliches suggerieren.
    """
    p = ['<path d="M60,100 C60,74 62,54 72,36"/>']          # Zweig
    # Blattpaare entlang des Zweigs, abwechselnd links und rechts
    for (bx, by), (ex, ey) in (((62, 82), (40, 74)), ((64, 70), (86, 62)),
                               ((68, 56), (46, 46)), ((72, 44), (92, 36))):
        p.append(f'<path d="M{bx},{by} C{(bx + ex) / 2 - 4},{by - 12} '
                 f'{ex + 4},{ey - 6} {ex},{ey} '
                 f'C{ex + 6},{ey + 8} {bx + 4},{by + 6} {bx},{by} Z"/>')
    for cx_, cy_, r in ((52, 62, 5.5), (76, 78, 5.5), (58, 40, 4.5)):
        p.append(f'<circle cx="{cx_}" cy="{cy_}" r="{r}"/>')  # Oliven
    return "".join(p)


ICONS = {
    "dns-blocklist": shield,
    "faktenchecker": magnifier,
    "humanism": humanitas,
    "olivera": olive,
    "dwc": dwc,
    "soil-coco": soil,
    "katzen": cat_wave,
}


def build(draw, theme_name):
    c = THEMES[theme_name]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {SIZE} {SIZE}" width="{SIZE}" height="{SIZE}" '
            f'role="presentation">'
            f'{ring(c)}'
            f'<g fill="none" stroke="{c["gold"]}" stroke-width="2.4" '
            f'stroke-linejoin="round">{draw()}</g>'
            f'</svg>')


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name, draw in ICONS.items():
        for theme in THEMES:
            out = assets / f"icon-{name}-{theme}.svg"
            out.write_text(build(draw, theme), encoding="utf-8")
    print(f"{len(ICONS) * len(THEMES)} Embleme in {assets}")


if __name__ == "__main__":
    main()
