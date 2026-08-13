#!/usr/bin/env python3
"""Erzeugt die animierte katzen-analyzer-Karte fuer das Profil-README.

Links das Foto als Eingangssignal, rechts ein laufendes FFT-Spektrum.
Das Foto wird als data:-URI eingebettet, damit die Datei fuer sich steht —
ein per <img> geladenes SVG darf keine externen Ressourcen nachladen.

    python3 generate_footer.py path/to/cats.jpg

Schreibt assets/katzen-analyzer.svg.
"""

import base64
import pathlib
import random
import sys

W, H = 1200, 400

# Bewusst durchgehend dunkel: die Karte soll wie ein Geraetedisplay wirken
# und funktioniert so in beiden GitHub-Themes ohne zweite Fassung.
BG = "#0D1117"
BORDER = "#30363D"
FG = "#E6EDF3"
MUTED = "#8B949E"
GOLD = "#C8973A"
A1, A2, A3 = "#7EE787", "#58A6FF", "#D2A8FF"

PHOTO_X, PHOTO_Y, PHOTO_W, PHOTO_H = 40, 44, 520, 312

SPEC_X0, SPEC_X1 = 620, 1160
BAR_W, BAR_GAP = 8, 5
BASE_Y = 316
MAX_BAR = 150

MONO = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
        "'Liberation Mono', monospace")


def bars(rnd):
    """Balken mit pseudo-zufaelligen Keyframes — sieht aus wie Live-Audio.

    Fester Seed, damit ein erneuter Lauf dieselbe Datei erzeugt und der
    Commit-Diff nicht bei jedem Aufruf rauscht.
    """
    out = []
    count = (SPEC_X1 - SPEC_X0 + BAR_GAP) // (BAR_W + BAR_GAP)
    for i in range(count):
        x = SPEC_X0 + i * (BAR_W + BAR_GAP)
        # Tiefe Frequenzen links tragen mehr Energie als hohe rechts
        tilt = 1.0 - 0.55 * (i / (count - 1))
        keys = [rnd.uniform(0.10, 1.0) * tilt * MAX_BAR for _ in range(5)]
        keys.append(keys[0])  # Schleife schliessen, sonst ruckelt der Umbruch
        hs = ";".join(f"{k:.1f}" for k in keys)
        ys = ";".join(f"{BASE_Y - k:.1f}" for k in keys)
        dur = rnd.uniform(1.6, 2.6)
        out.append(
            f'<rect x="{x}" y="{BASE_Y - keys[0]:.1f}" width="{BAR_W}" '
            f'height="{keys[0]:.1f}" rx="2" fill="url(#spec)">'
            f'<animate attributeName="height" values="{hs}" dur="{dur:.2f}s" '
            f'repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{ys}" dur="{dur:.2f}s" '
            f'repeatCount="indefinite"/></rect>')
    return "".join(out)


def deco_frame():
    """Dieselben gestuften Eckwinkel wie im Header — haelt die Karten als Serie zusammen."""
    out = ['<g opacity="0.8">']
    arm_outer, arm_inner = 30, 18
    inset0, step = 20, 7

    def bracket(x0, y0, sx, sy):
        segs = []
        for i, arm in enumerate((arm_outer, arm_inner)):
            o = inset0 + i * step
            ax, ay = x0 + sx * o, y0 + sy * o
            segs.append(
                f'<path d="M{ax:.1f},{ay + sy * arm:.1f} L{ax:.1f},{ay:.1f} '
                f'L{ax + sx * arm:.1f},{ay:.1f}" fill="none" stroke="{GOLD}" '
                f'stroke-width="1.3" opacity="{0.9 if i == 0 else 0.5}"/>')
        return "".join(segs)

    out.append(bracket(0, 0, 1, 1))
    out.append(bracket(W, 0, -1, 1))
    out.append(bracket(0, H, 1, -1))
    out.append(bracket(W, H, -1, -1))
    out.append('</g>')
    return "".join(out)


def build(photo_b64):
    rnd = random.Random(4921)
    o = []
    a = o.append

    a(f'<svg xmlns="http://www.w3.org/2000/svg" '
      f'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" '
      f'width="{W}" height="{H}" role="img" '
      f'aria-label="katzen-analyzer: zwei Katzen als Eingangssignal, '
      f'daneben ein laufendes Frequenzspektrum">')

    a('<defs>')
    a(f'<linearGradient id="spec" gradientUnits="userSpaceOnUse" '
      f'x1="{SPEC_X0}" y1="0" x2="{SPEC_X1}" y2="0">'
      f'<stop offset="0%" stop-color="{A1}"/>'
      f'<stop offset="50%" stop-color="{A2}"/>'
      f'<stop offset="100%" stop-color="{A3}"/></linearGradient>')
    a(f'<clipPath id="photoClip"><rect x="{PHOTO_X}" y="{PHOTO_Y}" '
      f'width="{PHOTO_W}" height="{PHOTO_H}" rx="10"/></clipPath>')
    a('</defs>')

    a(f'<rect width="{W}" height="{H}" rx="14" fill="{BG}" '
      f'stroke="{BORDER}" stroke-width="1"/>')

    # Eingangssignal
    a(f'<image xlink:href="data:image/jpeg;base64,{photo_b64}" '
      f'x="{PHOTO_X}" y="{PHOTO_Y}" width="{PHOTO_W}" height="{PHOTO_H}" '
      f'clip-path="url(#photoClip)" preserveAspectRatio="xMidYMid slice"/>')
    a(f'<rect x="{PHOTO_X}" y="{PHOTO_Y}" width="{PHOTO_W}" height="{PHOTO_H}" '
      f'rx="10" fill="none" stroke="{BORDER}" stroke-width="1"/>')

    # Pulsierender Aufnahmepunkt auf dem Foto
    a(f'<g><circle cx="{PHOTO_X + 22}" cy="{PHOTO_Y + 22}" r="5" fill="#F85149">'
      f'<animate attributeName="opacity" values="1;0.25;1" dur="1.6s" '
      f'repeatCount="indefinite"/></circle>'
      f'<text x="{PHOTO_X + 36}" y="{PHOTO_Y + 27}" font-family="{MONO}" '
      f'font-size="14" fill="{FG}">REC</text></g>')

    a(f'<text x="{PHOTO_X}" y="{PHOTO_Y + PHOTO_H + 26}" font-family="{MONO}" '
      f'font-size="14" fill="{MUTED}">input &#183; 2 subjects, '
      f'unimpressed</text>')

    # Analysepanel
    a(f'<text x="{SPEC_X0}" y="{PHOTO_Y + 30}" font-family="{MONO}" '
      f'font-size="26" font-weight="700" fill="{FG}">katzen-analyzer</text>')
    a(f'<text x="{SPEC_X0}" y="{PHOTO_Y + 58}" font-family="{MONO}" '
      f'font-size="15" fill="{MUTED}">real-time FFT &#183; browser-side &#183; '
      f'no upload</text>')

    a(bars(rnd))

    # Grundlinie und Frequenzachse
    a(f'<line x1="{SPEC_X0}" y1="{BASE_Y + 4}" x2="{SPEC_X1}" y2="{BASE_Y + 4}" '
      f'stroke="{BORDER}" stroke-width="1"/>')
    span = SPEC_X1 - SPEC_X0
    for frac, label in ((0.0, "20 Hz"), (0.33, "200"), (0.66, "2k"),
                        (1.0, "20 kHz")):
        x = SPEC_X0 + frac * span
        anchor = "start" if frac == 0.0 else ("end" if frac == 1.0 else "middle")
        a(f'<text x="{x:.0f}" y="{BASE_Y + 26}" text-anchor="{anchor}" '
          f'font-family="{MONO}" font-size="13" fill="{MUTED}">{label}</text>')

    a(deco_frame())

    a('</svg>')
    return "".join(o)


def main():
    src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "cats.jpg")
    photo_b64 = base64.b64encode(src.read_bytes()).decode("ascii")

    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    out = assets / "katzen-analyzer.svg"
    out.write_text(build(photo_b64), encoding="utf-8")
    print(f"{out}  ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
