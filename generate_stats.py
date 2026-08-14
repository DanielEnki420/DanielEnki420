#!/usr/bin/env python3
"""Erzeugt die Kennzahlen-Karte als SVG.

BEWUSST KEIN LIVE-DIENST. Die Zahlen werden beim Lauf dieses Skripts einmal
von der GitHub-API geholt und fest ins SVG geschrieben; die Karte traegt
sichtbar das Datum ihres Standes. Eine "Echtzeit"-Karte braeuchte einen
dauerhaft laufenden Endpunkt samt Token — und wuerde bei jedem Ausfall eine
Fehlermeldung auf dem Profil hinterlassen.

    python3 generate_stats.py          # Zahlen frisch von der API holen
    python3 generate_stats.py --offline  # zuletzt bekannte Zahlen verwenden

Schreibt assets/stats-dark.svg und assets/stats-light.svg.
"""

import datetime
import json
import pathlib
import subprocess
import sys

from theme import MONO, THEMES, card, corner_brackets

W, H = 1200, 300

# Stand, falls die API nicht erreichbar ist (--offline oder Netzfehler).
FALLBACK = {"repos_total": 30, "repos_public": 7, "stars": 8, "date": "2026-08-13"}

# Der Heimserver-Block ist selbst berichtet, nicht aus einer API — deshalb
# stehen hier bewusst Naeherungen ("~30") statt exakter Zahlen.
HOMELAB = [
    ("containers", "~30"),
    ("host", "1x Raspberry Pi 5"),
    ("storage", "NVMe / Samba"),
    ("backup", "nightly, off-site"),
    ("cloud services", "0"),
]


def fetch():
    """Repos und Sterne von der GitHub-API. Faellt bei Fehlern auf FALLBACK."""
    try:
        repos = json.loads(subprocess.run(
            ["gh", "api", "users/DanielEnki420/repos?per_page=100&type=owner",
             "--jq", "[.[] | {private, stars: .stargazers_count}]"],
            capture_output=True, text=True, check=True, timeout=30).stdout)
        user = json.loads(subprocess.run(
            ["gh", "api", "users/DanielEnki420",
             "--jq", "{public_repos}"],
            capture_output=True, text=True, check=True, timeout=30).stdout)
        priv = json.loads(subprocess.run(
            ["gh", "api", "graphql", "-f", "query="
             '{user(login:"DanielEnki420"){repositories(privacy:PRIVATE)'
             "{totalCount}}}", "--jq",
             ".data.user.repositories.totalCount"],
            capture_output=True, text=True, check=True, timeout=30).stdout)
        pub = user["public_repos"]
        return {
            "repos_total": pub + priv,
            "repos_public": pub,
            "stars": sum(r["stars"] for r in repos if not r["private"]),
            "date": datetime.date.today().isoformat(),
        }
    except Exception as exc:                      # noqa: BLE001
        print(f"  API nicht erreichbar ({exc.__class__.__name__}), "
              f"nutze Fallback-Zahlen", file=sys.stderr)
        return FALLBACK


def column(c, x, title, rows, value_color):
    """Eine Spalte: Ueberschrift, dann Label/Wert-Paare mit Punktfuehrung."""
    out = [f'<text x="{x}" y="86" font-family="{MONO}" font-size="15" '
           f'fill="{c["gold"]}">// {title}</text>']
    col_w = 460
    for i, (label, value) in enumerate(rows):
        y = 124 + i * 30
        out.append(f'<text x="{x}" y="{y}" font-family="{MONO}" '
                   f'font-size="15" fill="{c["muted"]}">{label}</text>')
        out.append(f'<text x="{x + col_w}" y="{y}" text-anchor="end" '
                   f'font-family="{MONO}" font-size="16" font-weight="700" '
                   f'fill="{value_color}">{value}</text>')
        # Punktfuehrung zwischen Label und Wert
        out.append(f'<line x1="{x + len(label) * 9 + 12}" y1="{y - 5}" '
                   f'x2="{x + col_w - len(str(value)) * 10 - 12}" '
                   f'y2="{y - 5}" stroke="{c["border"]}" stroke-width="1" '
                   f'stroke-dasharray="2 4"/>')
    return "".join(out)


def build(d, theme_name):
    c = THEMES[theme_name]
    github = [
        ("repositories", str(d["repos_total"])),
        ("public", str(d["repos_public"])),
        ("stars received", str(d["stars"])),
        ("forks of my work", "0"),
        ("account since", "Feb 2026"),
    ]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" '
         f'aria-label="Figures: {d["repos_total"]} repositories, '
         f'{d["stars"]} stars, around 30 containers on one Raspberry Pi 5">']
    o.append(card(c, W, H))
    o.append(f'<text x="64" y="50" font-family="{MONO}" font-size="20" '
             f'font-weight="700" fill="{c["fg"]}">$ stat --all</text>')
    o.append(column(c, 64, "GITHUB", github, c["a1"]))
    o.append(column(c, 676, "HOMELAB", HOMELAB, c["gold"]))
    # Der Hinweis ist Teil der Aussage, nicht Kleingedrucktes: die Karte
    # behauptet nirgends, live zu sein.
    o.append(f'<text x="64" y="272" font-family="{MONO}" font-size="13" '
             f'fill="{c["muted"]}">snapshot &#183; {d["date"]} &#183; regenerated '
             f'by generate_stats.py, not live &#183; homelab figures are '
             f'self-reported</text>')
    o.append(corner_brackets(c, W, H))
    o.append('</svg>')
    return "".join(o)


def main():
    d = FALLBACK if "--offline" in sys.argv else fetch()
    assets = pathlib.Path(__file__).parent / "assets"
    assets.mkdir(exist_ok=True)
    for name in THEMES:
        out = assets / f"stats-{name}.svg"
        out.write_text(build(d, name), encoding="utf-8")
        print(f"{out}  ({out.stat().st_size} B)")
    print(f"  Zahlen: {d}")


if __name__ == "__main__":
    main()
