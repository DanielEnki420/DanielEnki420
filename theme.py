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


# --- Schlagwort-Pillen, geteilt von Stack- und Homelab-Karte -------------
CHAR_W = 8.4        # Vorschub der Monospace bei 14px
PILL_FONT = 14
PILL_H = 32
PILL_PAD = 14       # Innenabstand je Seite
PILL_GAP = 10


def pill_width(label):
    return round(len(label) * CHAR_W + 2 * PILL_PAD)


def wrap(items, max_w):
    """Bricht Schlagworte in Zeilen um, die in die verfuegbare Breite passen."""
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


def pill(c, x, y, label):
    """Rechteckig, nicht abgerundet: Deco setzt auf Kanten."""
    w = pill_width(label)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{PILL_H}" fill="none" '
            f'stroke="{c["gold"]}" stroke-width="1" opacity="0.75"/>'
            f'<text x="{x + w / 2:.0f}" y="{y + 21}" text-anchor="middle" '
            f'font-family="{MONO}" font-size="{PILL_FONT}" '
            f'fill="{c["fg"]}">{label}</text>')
