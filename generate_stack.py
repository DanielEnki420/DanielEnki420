#!/usr/bin/env python3
"""Erzeugt die Stack-Leiste als SVG — Ersatz fuer die shields.io-Badges.

Die bunten Fremd-Badges (Signalrot, Giftgruen, Knallgelb) waren der einzige
Abschnitt des Profils, der nicht aus einer Hand kam und sich neben Gold auf
Anthrazit gebissen hat. Diese Fassung nutzt dieselbe Palette und dieselben
Eckwinkel wie die uebrigen Karten — und laedt nichts von fremden Servern.

    python3 generate_stack.py

Schreibt assets/stack-dark.svg und assets/stack-light.svg.
"""

import pathlib

from theme import MONO, THEMES, card, corner_brackets

W = 1200
PAD_X = 64          # linker Textrand, wie auf der Kennzahlen-Karte
CHAR_W = 8.4        # Vorschub der Monospace bei 14px
FONT = 14
PILL_H = 32
PILL_PAD = 14       # Innenabstand je Seite
PILL_GAP = 10
ROW_GAP = 46

ROWS = [
    ("INFRASTRUCTURE", ["Raspberry Pi 5", "Linux", "Docker", "Pi-hole",
                        "Unbound", "Grafana", "Prometheus", "ioBroker",
                        "Tailscale", "restic"]),
    ("DEVELOPMENT", ["TypeScript", "JavaScript", "Node.js", "Python",
                     "Bash"]),
]


def pill_width(label):
    return round(len(label) * CHAR_W + 2 * PILL_PAD)


def layout(items, max_w):
    """Bricht die Schlagworte in Zeilen um, die in die Karte passen."""
    lines, cur, cur_w = [], [], 0
    for it in items:
        w = pill_width(it)
        if cur and cur_w + PILL_GAP + w > max_w:
            lines.append(cur)
            cur, cur_w = [it], w
        else:
            cur_w += (PILL_GAP + w) if cur else w
            cur.append(it)
    if cur:
        lines.append(cur)
    return lines


def measure():
    """Kartenhoehe aus dem tatsaechlichen Umbruch bestimmen, nicht raten."""
    y = 84
    for _, items in ROWS:
        y += 26                                    # Zeile der Rubrik
        for _ in layout(items, W - 2 * PAD_X):
            y += PILL_H + 10
        y += ROW_GAP - 10
    return round(y - ROW_GAP + 44)


H = measure()


def build(theme_name):
    c = THEMES[theme_name]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" aria-label="Stack: '
         + "; ".join(f"{t.lower()} — " + ", ".join(i) for t, i in ROWS)
         + '">']
    o.append(card(c, W, H))
    o.append(f'<text x="{PAD_X}" y="50" font-family="{MONO}" font-size="20" '
             f'font-weight="700" fill="{c["fg"]}">$ stack</text>')

    y = 84
    for title, items in ROWS:
        o.append(f'<text x="{PAD_X}" y="{y}" font-family="{MONO}" '
                 f'font-size="15" fill="{c["gold"]}">// {title}</text>')
        y += 26
        for line in layout(items, W - 2 * PAD_X):
            x = PAD_X
            for label in line:
                w = pill_width(label)
                # Rechteckig, nicht abgerundet: Deco setzt auf Kanten.
                o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{PILL_H}" '
                         f'fill="none" stroke="{c["gold"]}" stroke-width="1" '
                         f'opacity="0.75"/>')
                o.append(f'<text x="{x + w / 2:.0f}" y="{y + 21}" '
                         f'text-anchor="middle" font-family="{MONO}" '
                         f'font-size="{FONT}" fill="{c["fg"]}">{label}</text>')
                x += w + PILL_GAP
            y += PILL_H + 10
        y += ROW_GAP - 10

    o.append(corner_brackets(c, W, H))
    o.append('</svg>')
    return "".join(o)


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name in THEMES:
        out = assets / f"stack-{name}.svg"
        out.write_text(build(name), encoding="utf-8")
        print(f"{out}  ({out.stat().st_size} B, {W}x{H})")


if __name__ == "__main__":
    main()
