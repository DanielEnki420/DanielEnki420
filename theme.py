"""Gemeinsame Palette und Deco-Bausteine fuer alle Grafik-Generatoren.

Vorher trug jedes Skript seine eigenen Hex-Werte, teils dunkel festverdrahtet.
Dadurch schaltete nur der Banner mit dem GitHub-Theme um, waehrend Kennzahlen,
Illustration und Analyzer-Karte immer dunkel blieben — im Hellmodus standen
drei fast schwarze Bloecke unter einem hellen Kopf.

Python legt das Verzeichnis des Skripts an den Anfang von sys.path, deshalb
funktioniert `import theme` unabhaengig davon, aus welchem Ordner man startet.
"""

MONO = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
        "'Liberation Mono', monospace")
SERIF = "Georgia, 'Times New Roman', 'Iowan Old Style', serif"

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "grid": "#161B22",
        "border": "#30363D",
        "fg": "#E6EDF3",
        "muted": "#8B949E",
        "a1": "#7EE787",
        "a2": "#58A6FF",
        "a3": "#D2A8FF",
        "gold": "#C8973A",
        "alert": "#F85149",
    },
    "light": {
        "bg": "#FFFFFF",
        "grid": "#F0F3F6",
        "border": "#D1D9E0",
        "fg": "#1F2328",
        "muted": "#59636E",
        "a1": "#1A7F37",
        "a2": "#0969DA",
        "a3": "#8250DF",
        # Auf Weiss braucht das Gold mehr Tiefe, sonst verschwindet es.
        "gold": "#8A6A1F",
        "alert": "#CF222E",
    },
}


def corner_brackets(c, w, h, arms=(30, 18), inset0=20, step=7, width=1.3):
    """Gestufte Eckwinkel — das wiederkehrende Deco-Motiv aller Karten."""
    out = ['<g opacity="0.8">']
    for x0, y0, sx, sy in ((0, 0, 1, 1), (w, 0, -1, 1),
                           (0, h, 1, -1), (w, h, -1, -1)):
        for i, arm in enumerate(arms):
            o = inset0 + i * step
            ax, ay = x0 + sx * o, y0 + sy * o
            out.append(f'<path d="M{ax:.1f},{ay + sy * arm:.1f} '
                       f'L{ax:.1f},{ay:.1f} L{ax + sx * arm:.1f},{ay:.1f}" '
                       f'fill="none" stroke="{c["gold"]}" '
                       f'stroke-width="{width}" '
                       f'opacity="{0.9 if i == 0 else 0.5}"/>')
    out.append('</g>')
    return "".join(out)


def card(c, w, h):
    """Kartengrund mit Rahmen."""
    return (f'<rect width="{w}" height="{h}" rx="14" fill="{c["bg"]}" '
            f'stroke="{c["border"]}" stroke-width="1"/>')
