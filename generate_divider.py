#!/usr/bin/env python3
"""Deco-Trenner zwischen den README-Abschnitten, statt einer nackten "---".

Transparenter Hintergrund, daher wie beim Header eine helle und eine dunkle
Fassung — auf Weiss braucht das Gold mehr Tiefe, sonst verschwindet es.

    python3 generate_divider.py

Schreibt assets/divider-dark.svg und assets/divider-light.svg.
"""

import pathlib

W, H = 1200, 32
GOLD = {"dark": "#C8973A", "light": "#8A6A1F"}


def build(gold):
    cx = W / 2
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
      f'width="{W}" height="{H}" role="presentation">')
    a(f'<g stroke="{gold}" fill="{gold}">')
    # Aussenlinien
    a(f'<line x1="0" y1="{H / 2}" x2="{cx - 30}" y2="{H / 2}" stroke-width="1" opacity="0.6"/>')
    a(f'<line x1="{cx + 30}" y1="{H / 2}" x2="{W}" y2="{H / 2}" stroke-width="1" opacity="0.6"/>')
    # Rautenkette in der Mitte: klein - gross - klein
    for dx, r in ((-18, 3), (0, 6), (18, 3)):
        a(f'<rect x="{cx + dx - r / 1.4:.1f}" y="{H / 2 - r / 1.4:.1f}" '
          f'width="{r * 1.42:.1f}" height="{r * 1.42:.1f}" '
          f'transform="rotate(45 {cx + dx:.1f} {H / 2})" opacity="0.9"/>')
    a('</g></svg>')
    return "".join(o)


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name, gold in GOLD.items():
        path = assets / f"divider-{name}.svg"
        path.write_text(build(gold), encoding="utf-8")
        print(f"{path}  ({path.stat().st_size} B)")


if __name__ == "__main__":
    main()
