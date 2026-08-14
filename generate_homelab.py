#!/usr/bin/env python3
"""Erzeugt die Homelab-Karte: Deco-Szene oben, Dienste darunter.

Vorher waren das zwei getrennte Karten direkt untereinander — zusammen
ueber 830 Pixel fuer einen einzigen Abschnitt, mit einer Rahmenkante
mittendrin, die nichts trennte. Jetzt eine Karte: die Zeichnung als Kopf,
die Rubriken als Inhalt.

Die Zeichnung stammt aus dem frueheren generate_illustration.py, das
dadurch entfaellt. Sitzende Katzen im Profil sind ein Deco-Motiv mit
Geschichte: nach der Tutanchamun-Grabung 1922 war Aegyptisierendes in den
Zwanzigern ueberall.

    python3 generate_homelab.py

Schreibt assets/homelab-dark.svg und assets/homelab-light.svg.
"""

import math
import pathlib

from theme import (MONO, PILL_GAP, PILL_H, THEMES, card, corner_brackets,
                   pill, pill_width, wrap)

W = 1200
PAD_X = 64
LABEL_W = 236       # Spalte der Rubriken
ROW_STEP = 46

# --- Szene -------------------------------------------------------------
# Die Zeichnung entstand fuer eine 1200 breite Karte; statt alle Koordinaten
# neu zu rechnen, wird die fertige Gruppe als Ganzes verkleinert.
SCENE_GROUND = 322          # Standlinie in lokalen Koordinaten
SCENE_TOP = 54              # oberster Punkt des Strahlenfaechers
SCENE_BOTTOM = 372          # Grundlinie der Bildunterschrift
SCENE_SCALE = 0.8
SCENE_Y = 76                # wo die Szene auf der Karte beginnt

RULE_Y = round(SCENE_Y + (SCENE_BOTTOM - SCENE_TOP) * SCENE_SCALE + 22)
TOP = RULE_Y + 32           # erste Pillenzeile

ROWS = [
    ("NETWORK &amp; PRIVACY", ["Pi-hole", "Unbound", "Tailscale", "CrowdSec",
                               "Fail2ban", "Vaultwarden"]),
    ("HOME AUTOMATION", ["ioBroker (Tuya, Zigbee, Shelly)",
                         "Telegram alerting"]),
    ("OBSERVABILITY", ["Grafana", "Prometheus", "Uptime Kuma", "Portainer",
                       "OLED display"]),
    ("MEDIA &amp; KNOWLEDGE", ["Immich", "Calibre-Web", "Kiwix"]),
    ("LOCAL AI", ["Ollama", "Open WebUI", "LiteLLM"]),
    ("BACKUP", ["restic &#8594; off-site, nightly"]),
]

CAPTION = ("~30 containers &#183; one Raspberry Pi 5 &#183; two supervisors")
NOTE = ("storage NVMe over Samba &#183; fan curve, watchdog and backup "
        "verification are scripted &#183; ~30 containers, self-reported")


def cat():
    """Sitzende Katze, lokal 120 breit und 170 hoch, Standlinie bei y=170."""
    p = ['<path d="M30,60 L26,10 L50,34 L70,34 L94,10 L90,60 '
         'C90,86 76,98 60,98 C44,98 30,86 30,60 Z"/>',
         '<path d="M36,54 L33,22 L52,38 Z"/>',
         '<path d="M84,54 L87,22 L68,38 Z"/>']
    for ex in (46, 74):            # Deco-Mandelaugen mit senkrechter Pupille
        p.append(f'<ellipse cx="{ex}" cy="58" rx="7.5" ry="4.5"/>')
        p.append(f'<ellipse cx="{ex}" cy="58" rx="1.6" ry="4"/>')
    p.append('<path d="M55,70 L65,70 L60,77 Z"/>')
    p.append('<path d="M60,77 C60,83 54,85 50,81"/>')
    p.append('<path d="M60,77 C60,83 66,85 70,81"/>')
    for wy, dy in ((72, -4), (77, 0), (82, 4)):
        p.append(f'<path d="M48,{wy} L12,{wy + dy}"/>')
        p.append(f'<path d="M72,{wy} L108,{wy + dy}"/>')
    p.append('<path d="M34,88 C20,110 14,140 16,170 L104,170 '
             'C106,140 100,110 86,88"/>')
    p.append('<path d="M37,95 C49,107 71,107 83,95"/>')          # Halsband
    p.append('<path d="M60,104 L64,110 L60,116 L56,110 Z"/>')
    p.append('<path d="M46,142 L46,170"/>')
    p.append('<path d="M74,142 L74,170"/>')
    p.append('<ellipse cx="34" cy="166" rx="14" ry="6"/>')
    p.append('<ellipse cx="86" cy="166" rx="14" ry="6"/>')
    p.append('<path d="M104,168 C124,164 130,142 118,130 '
             'C112,124 103,127 104,136"/>')                       # Schwanz
    return "".join(p)


def raspberry_pi():
    """Platine von oben, lokal 300 x 210. Geometrisch, kein Fotorealismus."""
    p = ['<path d="M14,0 L286,0 L300,14 L300,196 L286,210 L14,210 '
         'L0,196 L0,14 Z"/>']
    for y in (12, 24):                       # 40-poliger GPIO-Header
        for i in range(20):
            p.append(f'<rect x="{28 + i * 12}" y="{y}" width="7" height="7"/>')
    p.append('<rect x="112" y="84" width="66" height="66"/>')      # SoC
    p.append('<rect x="126" y="98" width="38" height="38"/>')
    p.append('<path d="M126,98 L164,136 M164,98 L126,136"/>')
    p.append('<rect x="196" y="92" width="40" height="26"/>')      # RAM
    for y in (48, 104, 160):                 # Anschluesse rechts
        p.append(f'<rect x="252" y="{y}" width="48" height="42"/>')
        p.append(f'<rect x="260" y="{y + 8}" width="32" height="26"/>')
    for x in (26, 78, 128):                  # HDMI und Strom unten
        p.append(f'<rect x="{x}" y="196" width="30" height="14"/>')
    for hx, hy in ((20, 20), (280, 20), (20, 190), (280, 190)):
        p.append(f'<circle cx="{hx}" cy="{hy}" r="5"/>')
    p.append('<path d="M40,60 L100,60 L112,72"/>')                 # Leiterbahnen
    p.append('<path d="M40,72 L94,72 L106,84"/>')
    p.append('<path d="M178,116 L196,116"/>')
    return "".join(p)


def sun_fan(c):
    """Halbrunder Strahlenfaecher ueber der Szene — Deco-Sonnentor."""
    cx, cy = W / 2, SCENE_GROUND
    r_in, r_out = 236, 268
    out = [f'<g opacity="0.32" stroke="{c["gold"]}" stroke-width="1.4">']
    n = 23
    for i in range(n):
        ang = math.radians(202 + i * (136 / (n - 1)))   # laesst die Katzen frei
        out.append(f'<line x1="{cx + r_in * math.cos(ang):.1f}" '
                   f'y1="{cy + r_in * math.sin(ang):.1f}" '
                   f'x2="{cx + r_out * math.cos(ang):.1f}" '
                   f'y2="{cy + r_out * math.sin(ang):.1f}"/>')
    out.append('</g>')
    return "".join(out)


def scene(c):
    """Die komplette Zeichnung in lokalen Koordinaten, als Gruppe skaliert."""
    o = [sun_fan(c)]
    o.append(f'<line x1="150" y1="{SCENE_GROUND}" x2="1050" '
             f'y2="{SCENE_GROUND}" stroke="{c["gold"]}" stroke-width="1.2" '
             f'opacity="0.55"/>')
    for dx in (150, 1050):
        o.append(f'<rect x="{dx - 4}" y="{SCENE_GROUND - 4}" width="8" '
                 f'height="8" transform="rotate(45 {dx} {SCENE_GROUND})" '
                 f'fill="{c["gold"]}" opacity="0.7"/>')
    o.append(f'<g fill="none" stroke="{c["gold"]}" stroke-width="1.5" '
             f'stroke-linejoin="round" '
             f'transform="translate(450 {SCENE_GROUND - 210})">'
             f'{raspberry_pi()}</g>')
    s = 1.12
    ty = SCENE_GROUND - 170 * s
    for tx, sx in ((196, s), (1004, -s)):
        o.append(f'<g fill="none" stroke="{c["gold"]}" stroke-width="1.6" '
                 f'stroke-linejoin="round" stroke-linecap="round" '
                 f'transform="translate({tx} {ty:.1f}) scale({sx} {s})">'
                 f'{cat()}</g>')
    o.append(f'<text x="{W / 2}" y="{SCENE_BOTTOM}" text-anchor="middle" '
             f'font-family="{MONO}" font-size="15" fill="{c["muted"]}">'
             f'{CAPTION}</text>')

    dx = (W - W * SCENE_SCALE) / 2
    dy = SCENE_Y - SCENE_TOP * SCENE_SCALE
    return (f'<g transform="translate({dx:.1f} {dy:.1f}) '
            f'scale({SCENE_SCALE})">' + "".join(o) + '</g>')


def measure():
    """Hoehe aus dem tatsaechlichen Umbruch bestimmen, nicht raten."""
    y = TOP
    for _, items in ROWS:
        lines = wrap(items, W - PAD_X - LABEL_W - PAD_X)
        y += max(1, len(lines)) * (PILL_H + 10) + (ROW_STEP - PILL_H - 10)
    return round(y + 44)


H = measure()


def build(theme_name):
    c = THEMES[theme_name]
    plain = "; ".join(f"{t.replace('&amp;', 'and').lower()}: "
                      + ", ".join(i.replace("&#8594;", "to") for i in items)
                      for t, items in ROWS)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" '
         f'aria-label="Homelab on one Raspberry Pi 5, shown as an Art Deco '
         f'line drawing of two cats flanking the board — {plain}">']
    o.append(card(c, W, H))
    o.append(f'<text x="{PAD_X}" y="50" font-family="{MONO}" font-size="20" '
             f'font-weight="700" fill="{c["fg"]}">$ docker ps</text>')

    o.append(scene(c))
    o.append(f'<line x1="{PAD_X}" y1="{RULE_Y}" x2="{W - PAD_X}" '
             f'y2="{RULE_Y}" stroke="{c["gold"]}" stroke-width="1" '
             f'opacity="0.3"/>')

    y = TOP
    for title, items in ROWS:
        o.append(f'<text x="{PAD_X}" y="{y + 21}" font-family="{MONO}" '
                 f'font-size="15" fill="{c["gold"]}">// {title}</text>')
        for line in wrap(items, W - PAD_X - LABEL_W - PAD_X):
            x = PAD_X + LABEL_W
            for label in line:
                o.append(pill(c, x, y, label))
                x += pill_width(label) + PILL_GAP
            y += PILL_H + 10
        y += ROW_STEP - PILL_H - 10

    o.append(f'<text x="{PAD_X}" y="{H - 26}" font-family="{MONO}" '
             f'font-size="13" fill="{c["muted"]}">{NOTE}</text>')
    o.append(corner_brackets(c, W, H))
    o.append('</svg>')
    return "".join(o)


def main():
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name in THEMES:
        out = assets / f"homelab-{name}.svg"
        out.write_text(build(name), encoding="utf-8")
        print(f"{out.name}  ({out.stat().st_size} B, {W}x{H})")


if __name__ == "__main__":
    main()
