#!/usr/bin/env python3
"""Deco-Linienzeichnung: zwei sitzende Katzen flankieren einen Raspberry Pi 5.

Bewusst neu gezeichnet statt irgendwo abgeschaut — Linienstaerke, Gold und
Strahlenfaecher folgen demselben Vokabular wie der Maeanderring im Header.
Sitzende Katzen im Profil sind ein Deco-Motiv mit Geschichte: nach der
Tutanchamun-Grabung 1922 war Aegyptisierendes in den Zwanzigern ueberall.

    python3 generate_illustration.py

Schreibt assets/the-stack.svg.
"""

import math
import pathlib

W, H = 1200, 420

BG = "#0D1117"
BORDER = "#30363D"
GOLD = "#C8973A"
MUTED = "#8B949E"

MONO = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
        "'Liberation Mono', monospace")

GROUND_Y = 322


def cat():
    """Sitzende Katze, lokal 120 breit und 170 hoch, Standlinie bei y=170.

    Reine Linienzeichnung: alles offen gestrichelt, nichts gefuellt, damit
    sie neben dem Maeanderring nicht als Klecks wirkt.
    """
    p = []
    # Kopf mit angesetzten Ohren
    p.append('<path d="M30,60 L26,10 L50,34 L70,34 L94,10 L90,60 '
             'C90,86 76,98 60,98 C44,98 30,86 30,60 Z"/>')
    # Ohrinnenflaechen
    p.append('<path d="M36,54 L33,22 L52,38 Z"/>')
    p.append('<path d="M84,54 L87,22 L68,38 Z"/>')
    # Augen: gestreckte Deco-Mandeln mit senkrechter Pupille
    for ex in (46, 74):
        p.append(f'<ellipse cx="{ex}" cy="58" rx="7.5" ry="4.5"/>')
        p.append(f'<ellipse cx="{ex}" cy="58" rx="1.6" ry="4"/>')
    # Nase und Schnauze
    p.append('<path d="M55,70 L65,70 L60,77 Z"/>')
    p.append('<path d="M60,77 C60,83 54,85 50,81"/>')
    p.append('<path d="M60,77 C60,83 66,85 70,81"/>')
    # Schnurrhaare
    for wy, dy in ((72, -4), (77, 0), (82, 4)):
        p.append(f'<path d="M48,{wy} L12,{wy + dy}"/>')
        p.append(f'<path d="M72,{wy} L108,{wy + dy}"/>')
    # Koerper
    p.append('<path d="M34,88 C20,110 14,140 16,170 L104,170 '
             'C106,140 100,110 86,88"/>')
    # Halsband mit Anhaenger — kleiner Deco-Akzent
    p.append('<path d="M37,95 C49,107 71,107 83,95"/>')
    p.append('<path d="M60,104 L64,110 L60,116 L56,110 Z"/>')
    # Vorderlaeufe und Pfoten
    p.append('<path d="M46,142 L46,170"/>')
    p.append('<path d="M74,142 L74,170"/>')
    p.append('<ellipse cx="34" cy="166" rx="14" ry="6"/>')
    p.append('<ellipse cx="86" cy="166" rx="14" ry="6"/>')
    # Schwanz, um die Standlinie gelegt
    p.append('<path d="M104,168 C124,164 130,142 118,130 '
             'C112,124 103,127 104,136"/>')
    return "".join(p)


def raspberry_pi():
    """Platine von oben, lokal 300 x 210. Geometrisch, kein Fotorealismus."""
    p = []
    # Platine mit abgeschraegten Ecken
    p.append('<path d="M14,0 L286,0 L300,14 L300,196 L286,210 L14,210 '
             'L0,196 L0,14 Z"/>')
    # 40-poliger GPIO-Header, zwei Reihen
    for row, y in ((0, 12), (1, 24)):
        for i in range(20):
            p.append(f'<rect x="{28 + i * 12}" y="{y}" width="7" height="7"/>')
    # SoC mit Diagonalkreuz
    p.append('<rect x="112" y="84" width="66" height="66"/>')
    p.append('<rect x="126" y="98" width="38" height="38"/>')
    p.append('<path d="M126,98 L164,136 M164,98 L126,136"/>')
    # Speicherbaustein
    p.append('<rect x="196" y="92" width="40" height="26"/>')
    # Anschluesse an der rechten Kante
    for y in (48, 104, 160):
        p.append(f'<rect x="252" y="{y}" width="48" height="42"/>')
        p.append(f'<rect x="260" y="{y + 8}" width="32" height="26"/>')
    # Micro-HDMI und Stromanschluss an der Unterkante
    for x in (26, 78, 128):
        p.append(f'<rect x="{x}" y="196" width="30" height="14"/>')
    # Befestigungsloecher
    for hx, hy in ((20, 20), (280, 20), (20, 190), (280, 190)):
        p.append(f'<circle cx="{hx}" cy="{hy}" r="5"/>')
    # Ein paar Leiterbahnen als Zierde
    p.append('<path d="M40,60 L100,60 L112,72"/>')
    p.append('<path d="M40,72 L94,72 L106,84"/>')
    p.append('<path d="M178,116 L196,116"/>')
    return "".join(p)


def sun_fan():
    """Halbrunder Strahlenfaecher ueber der Szene — Deco-Sonnentor."""
    cx, cy = W / 2, GROUND_Y
    # Deutlich weiter aussen als im ersten Entwurf: dort lag der Faecher so
    # dicht an der Platine, dass er als Gekritzel gelesen wurde statt als
    # eigenes Motiv. r_in liegt jetzt sicher jenseits der Platinenecken.
    r_in, r_out = 236, 268
    out = [f'<g opacity="0.32" stroke="{GOLD}" stroke-width="1.4">']
    n = 23
    for i in range(n):
        # 202 bis 338 Grad: oberer Bogen, laesst die Katzen frei
        ang = math.radians(202 + i * (136 / (n - 1)))
        out.append(
            f'<line x1="{cx + r_in * math.cos(ang):.1f}" '
            f'y1="{cy + r_in * math.sin(ang):.1f}" '
            f'x2="{cx + r_out * math.cos(ang):.1f}" '
            f'y2="{cy + r_out * math.sin(ang):.1f}"/>')
    out.append('</g>')
    return "".join(out)


def deco_frame():
    out = ['<g opacity="0.8">']
    for x0, y0, sx, sy in ((0, 0, 1, 1), (W, 0, -1, 1),
                           (0, H, 1, -1), (W, H, -1, -1)):
        for i, arm in enumerate((30, 18)):
            o = 20 + i * 7
            ax, ay = x0 + sx * o, y0 + sy * o
            out.append(f'<path d="M{ax:.1f},{ay + sy * arm:.1f} '
                       f'L{ax:.1f},{ay:.1f} L{ax + sx * arm:.1f},{ay:.1f}" '
                       f'fill="none" stroke="{GOLD}" stroke-width="1.3" '
                       f'opacity="{0.9 if i == 0 else 0.5}"/>')
    out.append('</g>')
    return "".join(out)


def build():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" '
         f'aria-label="Linienzeichnung im Art-Deco-Stil: zwei sitzende Katzen '
         f'flankieren einen Raspberry Pi 5, darueber ein Strahlenfaecher">']
    o.append(f'<rect width="{W}" height="{H}" rx="14" fill="{BG}" '
             f'stroke="{BORDER}" stroke-width="1"/>')

    o.append(sun_fan())

    # Standlinie mit Rautenabschluss an beiden Enden
    o.append(f'<line x1="150" y1="{GROUND_Y}" x2="1050" y2="{GROUND_Y}" '
             f'stroke="{GOLD}" stroke-width="1.2" opacity="0.55"/>')
    for dx in (150, 1050):
        o.append(f'<rect x="{dx - 4}" y="{GROUND_Y - 4}" width="8" height="8" '
                 f'transform="rotate(45 {dx} {GROUND_Y})" fill="{GOLD}" '
                 f'opacity="0.7"/>')

    # Platine, mittig auf der Standlinie
    o.append(f'<g fill="none" stroke="{GOLD}" stroke-width="1.5" '
             f'stroke-linejoin="round" opacity="0.95" '
             f'transform="translate(450 {GROUND_Y - 210}) scale(1)">'
             f'{raspberry_pi()}</g>')

    # Die beiden Aufseher, gespiegelt
    scale = 1.12
    cat_h = 170 * scale
    ty = GROUND_Y - cat_h
    o.append(f'<g fill="none" stroke="{GOLD}" stroke-width="1.6" '
             f'stroke-linejoin="round" stroke-linecap="round" '
             f'transform="translate(196 {ty:.1f}) scale({scale})">'
             f'{cat()}</g>')
    o.append(f'<g fill="none" stroke="{GOLD}" stroke-width="1.6" '
             f'stroke-linejoin="round" stroke-linecap="round" '
             f'transform="translate(1004 {ty:.1f}) scale({-scale} {scale})">'
             f'{cat()}</g>')

    o.append(f'<text x="{W / 2}" y="372" text-anchor="middle" '
             f'font-family="{MONO}" font-size="15" fill="{MUTED}">'
             f'~30 containers &#183; one Raspberry Pi 5 &#183; '
             f'two supervisors</text>')

    o.append(deco_frame())
    o.append('</svg>')
    return "".join(o)


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    out = assets / "the-stack.svg"
    out.write_text(build(), encoding="utf-8")
    print(f"{out}  ({out.stat().st_size} B)")


if __name__ == "__main__":
    main()
