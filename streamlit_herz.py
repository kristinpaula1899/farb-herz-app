# ------------------------------------------------------------
# Dateiname: streamlit_herz.py
# Autorin:   Kristin & Gemmy
# Datum:     23.06.2025
#
# Beschreibung: Eine Streamlit Web-App, die ein Herz aus Farbfeldern
#               anzeigt. Ein Button wechselt durch vordefinierte,
#               harmonische Farbpaletten zu verschiedenen Themen.
# ------------------------------------------------------------
import streamlit as st
from PIL import Image, ImageDraw
import random

# --- 1. Das GRÖSSERE Herz-Layout definieren ---
HERZ_LAYOUT = [
    "    XXX   XXX    ",
    "  XXXXXX XXXXXX  ",
    " XXXXXXXXXXXXXXX ",
    " XXXXXXXXXXXXXXX ",
    " XXXXXXXXXXXXXXX ",
    "  XXXXXXXXXXXXX  ",
    "   XXXXXXXXXXX   ",
    "    XXXXXXXXX    ",
    "     XXXXXXX     ",
    "       XXX       ",
    "        X        ",
]

# --- 2. Die Farb-Paletten (unverändert) ---
FARB_PALETTEN = {
    "Sommer am Mittelmeer": ["#00A5CF", "#0077B6", "#90E0EF", "#CAF0F8", "#F5F5DC"],
    "Lichtenberg": ["#C78B3D", "#9A3E2A", "#A4B6C5", "#E5E4E2", "#36454F"],
    "Hochgebirge im Winter": ["#FFFFFF", "#E0E1DD", "#A2A392", "#6D6A75", "#2B2A2F"],
    "Farben des Abendhimmels": ["#001F54", "#40E0D0", "#FFBF00", "#FF6F61", "#FF7F50"],
    "Kladow": ["#C5D664", "#F8F47E", "#53A78D", "#234984", "#79D3F1"],
    "Afrikanische Savanne": ["#A68A64", "#7F5539", "#B08968", "#DDBEA9", "#E6CCB2"],
    "Prenzlberg": ["#FDB813", "#2E7D32", "#B85C38", "#9EADBD", "#495057"],
    "Tropischer Regenwald": ["#004B23", "#006400", "#38B000", "#FFC300", "#C70039"],
    "Kirschblüte in Teltow": ["#F7A8B8", "#6EB5FF", "#78B446", "#6B4F43", "#C3A984"],
    "Tokyo bei Nacht": ["#F94144", "#F3722C", "#F9C74F", "#43AA8B", "#277DA1", "#080708"]
}
THEMEN = list(FARB_PALETTEN.keys())

# --- 3. Eine Funktion, die das Herz-Bild erzeugt ---
def erstelle_herz_bild(palette, zell_groesse=30, abstand=3):
    """Erstellt mit Pillow ein Bild des Herzens basierend auf der Farbpalette."""
    breite = len(HERZ_LAYOUT[0]) * (zell_groesse + abstand)
    hoehe = len(HERZ_LAYOUT) * (zell_groesse + abstand)
    
    # Erstelle eine leere, transparente Leinwand
    bild = Image.new('RGBA', (breite, hoehe), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)

    for zeilen_index, zeile in enumerate(HERZ_LAYOUT):
        for spalten_index, charakter in enumerate(zeile):
            if charakter == "X":
                # Wähle eine zufällige Farbe aus der aktuellen Palette
                farbe = random.choice(palette)
                
                # Berechne die Position für das nächste Farbfeld
                x0 = spalten_index * (zell_groesse + abstand)
                y0 = zeilen_index * (zell_groesse + abstand)
                x1 = x0 + zell_groesse
                y1 = y0 + zell_groesse
                
                # Zeichne ein Rechteck auf die Leinwand
                zeichner.rectangle([x0, y0, x1, y1], fill=farbe, outline="black", width=1)
    return bild

# --- 4. Streamlit App-Logik ---

# Seitenkonfiguration (wird als Erstes ausgeführt)
st.set_page_config(page_title="Herz der Farben", page_icon="💖", layout="centered")

# Haupttitel der Web-App
st.title("💖 Herz der Farben")

# --- 5. Zustandsverwaltung mit st.session_state ---
# Initialisiere den Theme-Index, falls er noch nicht existiert.
# Das ist der Weg, wie Streamlit sich Dinge zwischen Klicks "merkt".
if 'theme_index' not in st.session_state:
    st.session_state.theme_index = 0

# Button, um das Thema zu wechseln
if st.button("Nächstes Thema", use_container_width=True):
    # Erhöhe den Index und sorge mit Modulo (%) für einen Kreislauf
    st.session_state.theme_index = (st.session_state.theme_index + 1) % len(THEMEN)

# Hole das aktuelle Thema und die Palette basierend auf dem gespeicherten Index
aktuelles_thema_name = THEMEN[st.session_state.theme_index]
aktuelle_palette = FARB_PALETTEN[aktuelles_thema_name]

# Zeige den Namen des aktuellen Themas an
st.header(aktuelles_thema_name, divider="rainbow")

# Erzeuge und zeige das Herz-Bild an
herz_bild = erstelle_herz_bild(aktuelle_palette)
st.image(herz_bild)
