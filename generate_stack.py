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

from theme import (MONO, PILL_GAP, PILL_H, THEMES, card, corner_brackets,
                   pill, pill_width, wrap)

W = 1200
PAD_X = 64          # linker Textrand, wie auf der Kennzahlen-Karte
ROW_GAP = 46

# Bewusst nur die Plattformebene: die einzelnen Dienste stehen auf der
# Homelab-Karte. Als beide Karten nebeneinander standen, wiederholten sich
# sieben von zehn Eintraegen — hier Unterbau, dort was darauf laeuft.
ROWS = [
    ("PLATFORM", ["Raspberry Pi 5", "Linux", "Docker", "NVMe", "Samba"]),
    ("DEVELOPMENT", ["TypeScript", "JavaScript", "Node.js", "Python",
                     "Bash"]),
]


def measure():
    """Kartenhoehe aus dem tatsaechlichen Umbruch bestimmen, nicht raten."""
    y = 84
    for _, items in ROWS:
        y += 26                                    # Zeile der Rubrik
        for _ in wrap(items, W - 2 * PAD_X):
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
        for line in wrap(items, W - 2 * PAD_X):
            x = PAD_X
            for label in line:
                o.append(pill(c, x, y, label))
                x += pill_width(label) + PILL_GAP
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
