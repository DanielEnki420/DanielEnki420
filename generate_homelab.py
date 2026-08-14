#!/usr/bin/env python3
"""Erzeugt die Homelab-Karte als SVG.

Loest die Markdown-Tabelle ab, die als letzter Abschnitt der Seite noch im
grauen Standardlayout stand. Rubriken links, Dienste rechts als Pillen —
dieselben Bausteine wie auf der Stack-Karte.

    python3 generate_homelab.py

Schreibt assets/homelab-dark.svg und assets/homelab-light.svg.
"""

import pathlib

from theme import (MONO, PILL_GAP, PILL_H, THEMES, card, corner_brackets,
                   pill, pill_width, wrap)

W = 1200
PAD_X = 64
LABEL_W = 236       # Spalte der Rubriken
ROW_STEP = 46
TOP = 96

# Selbst berichtet, nicht aus einer API — die Zahl im Titel bleibt daher
# eine Naeherung, so wie auf der Kennzahlen-Karte.
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

NOTE = ("storage NVMe over Samba &#183; fan curve, watchdog and backup "
        "verification are scripted &#183; ~30 containers, self-reported")


def pill_x0():
    return PAD_X + LABEL_W


def measure():
    """Hoehe aus dem tatsaechlichen Umbruch bestimmen, nicht raten."""
    y = TOP
    for _, items in ROWS:
        lines = wrap(items, W - pill_x0() - PAD_X)
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
         f'aria-label="Homelab on one Raspberry Pi 5 — {plain}">']
    o.append(card(c, W, H))
    o.append(f'<text x="{PAD_X}" y="50" font-family="{MONO}" font-size="20" '
             f'font-weight="700" fill="{c["fg"]}">$ docker ps</text>')

    y = TOP
    for title, items in ROWS:
        # Rubrik auf der Grundlinie der ersten Pillenzeile
        o.append(f'<text x="{PAD_X}" y="{y + 21}" font-family="{MONO}" '
                 f'font-size="15" fill="{c["gold"]}">// {title}</text>')
        for line in wrap(items, W - pill_x0() - PAD_X):
            x = pill_x0()
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
        print(f"{out}  ({out.stat().st_size} B, {W}x{H})")


if __name__ == "__main__":
    main()
