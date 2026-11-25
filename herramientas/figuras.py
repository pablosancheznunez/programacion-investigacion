"""Genera las figuras del libro (SVG) en figuras/.

Uso, desde la raíz del libro:   python3 herramientas/figuras.py [--png]
Paleta categórica validada (orden fijo): azul, naranja, aguamarina, amarillo, magenta.
"""
import pathlib, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "figuras"; OUT.mkdir(exist_ok=True)

S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
TINTA, TINTA2, GRIS, SUP = "#0b0b0b", "#52514e", "#d9d8d4", "#ffffff"
CAJA, CAJA2 = "#eef0f6", "#c9cfe0"

plt.rcParams.update({
    "font.family": ["Inter", "DejaVu Sans"], "font.size": 11,
    "svg.fonttype": "path", "figure.facecolor": SUP, "axes.facecolor": SUP,
})


def lienzo(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def guardar(fig, nombre):
    fig.savefig(OUT / nombre, format="svg", bbox_inches="tight", pad_inches=0.15)
    if "--png" in sys.argv:
        pathlib.Path("/tmp/figpng").mkdir(exist_ok=True)
        fig.savefig(pathlib.Path("/tmp/figpng") / nombre.replace(".svg", ".png"), dpi=100, bbox_inches="tight")
    plt.close(fig); print("ok", nombre)


def caja(ax, x, y, w, h, texto, fc=CAJA, ec=CAJA2, tc=TINTA, fs=10, r=0.08, lw=1.2, peso="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw))
    if texto:
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=tc,
                linespacing=1.2, fontweight=peso)


def flecha(ax, a, b, color=TINTA2, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, color=color, lw=1.3,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2))


def pagina(ax, x, y, w, h, titulo):
    caja(ax, x, y, w, h, None, fc=SUP, ec=TINTA2, r=0.06)
    ax.add_patch(FancyBboxPatch((x, y + h - 0.35), w, 0.35, boxstyle="round,pad=0,rounding_size=0.06",
                                fc=CAJA, ec=TINTA2, lw=1.2))
    ax.text(x + 0.15, y + h - 0.175, titulo, ha="left", va="center", fontsize=9, color=TINTA2)
    for i in range(5):
        ax.plot([x + 0.2, x + w - 0.2 - (0.5 if i % 2 else 0)], [y + h - 0.7 - i * 0.32] * 2,
                color=GRIS, lw=3, solid_capstyle="round")





def p3_etl():
    fig, ax = lienzo(10, 4.2, (0, 15), (-0.4, 5.6))
    cols = [(0.3, "Extraer", ["CSV", "API (JSON)", "Base de datos"], S[0]), (5.3, "Transformar", ["Normalizar", "Validar", "Deduplicar", "Unir"], S[1]), (10.3, "Cargar", ["SQLite", "CSV limpio"], S[2])]
    for x, t, items, c in cols:
        ax.add_patch(FancyBboxPatch((x, 1.0), 4.4, 4.4, boxstyle="round,pad=0,rounding_size=0.15", fc=c, ec="none", alpha=0.15))
        ax.text(x + 2.2, 4.95, t, ha="center", fontsize=13, fontweight="bold", color=TINTA)
        for i, it in enumerate(items):
            caja(ax, x + 0.5, 3.75 - i * 0.82, 3.4, 0.64, it, fs=10.5)
    flecha(ax, (4.75, 3.2), (5.25, 3.2)); flecha(ax, (9.75, 3.2), (10.25, 3.2))
    ax.add_patch(FancyBboxPatch((0.3, -0.2), 14.4, 0.85, boxstyle="round,pad=0,rounding_size=0.1", fc=CAJA, ec=CAJA2))
    ax.text(7.5, 0.22, "Todo es código versionado · los datos brutos no se modifican · registro de cambios y validación", ha="center", va="center", fontsize=10, color=TINTA)
    guardar(fig, "p3_etl.svg")


def p6_mcp():
    fig, ax = lienzo(10.5, 4.8, (0, 16), (0, 7.2))
    ax.add_patch(FancyBboxPatch((0.2, 0.4), 4.6, 6.4, boxstyle="round,pad=0,rounding_size=0.15", fc=S[0], ec="none", alpha=0.13))
    ax.text(2.5, 6.35, "Anfitrión", ha="center", fontsize=13, fontweight="bold", color=TINTA)
    caja(ax, 0.6, 4.6, 3.8, 1.1, "Modelo de lenguaje", fs=10.5)
    caja(ax, 0.6, 2.9, 3.8, 0.9, "Cliente 1", fs=10.5); caja(ax, 0.6, 1.0, 3.8, 0.9, "Cliente 2", fs=10.5)
    servs = [(4.65, "Servidor local (stdio)", "Herramientas · recursos · plantillas", "Archivos del proyecto", 3.35), (0.75, "Servidor remoto (HTTP)", "Herramientas · recursos · plantillas", "API de OpenAlex", 1.45)]
    for y, t, st, fuente, yc in servs:
        ax.add_patch(FancyBboxPatch((6.6, y), 5.0, 1.9, boxstyle="round,pad=0,rounding_size=0.12", fc=S[2], ec="none", alpha=0.18))
        ax.text(9.1, y + 1.35, t, ha="center", fontsize=11, fontweight="bold", color=TINTA); ax.text(9.1, y + 0.6, st, ha="center", fontsize=9.5, color=TINTA2)
        ax.add_patch(FancyArrowPatch((4.45, yc), (6.55, y + 0.95), arrowstyle="<|-|>", mutation_scale=11, color=TINTA2, lw=1.3))
        caja(ax, 12.6, y + 0.45, 3.1, 1.0, fuente, fs=10)
        flecha(ax, (11.65, y + 0.95), (12.55, y + 0.95))
    ax.text(5.2, 4.75, "JSON-RPC", ha="center", fontsize=9, color=TINTA2, rotation=47); ax.text(5.5, 1.85, "JSON-RPC", ha="center", fontsize=9, color=TINTA2, rotation=7)
    guardar(fig, "p6_mcp.svg")


if __name__ == "__main__":
    p3_etl(); p6_mcp()
