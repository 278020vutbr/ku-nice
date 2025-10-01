import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# Funkce pro vykreslení kruhu s body
def plot_circle(center, radius, num_points, point_color):
    # Vytvoření osy
    fig, ax = plt.subplots()
    
    # Generování bodů na kruhu
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)

    # Vykreslení kruhu
    circle = plt.Circle(center, radius, edgecolor='black', facecolor='none', linestyle='--', linewidth=1)
    ax.add_artist(circle)
    
    # Vykreslení bodů
    ax.scatter(x, y, color=point_color, zorder=5)

    # Vykreslení číselných hodnot na osách
    ax.set_xticks(np.arange(center[0] - radius, center[0] + radius + 1, radius/2))
    ax.set_yticks(np.arange(center[1] - radius, center[1] + radius + 1, radius/2))
    ax.set_xticklabels([f'{i} m' for i in np.arange(center[0] - radius, center[0] + radius + 1, radius/2)])
    ax.set_yticklabels([f'{i} m' for i in np.arange(center[1] - radius, center[1] + radius + 1, radius/2)])

    # Osy
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)

    # Nastavení limitů a titulku
    ax.set_xlim(center[0] - radius - 1, center[0] + radius + 1)
    ax.set_ylim(center[1] - radius - 1, center[1] + radius + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Kruhová křivka s body")

    # Zobrazení grafu
    plt.grid(True)
    return fig

# Funkce pro generování PDF
def generate_pdf(center, radius, num_points, point_color):
    # Cesta k PDF souboru
    pdf_path = "/tmp/kruznice.pdf"
    pdf = PdfPages(pdf_path)

    # Vytvoření grafu
    fig = plot_circle(center, radius, num_points, point_color)
    pdf.savefig(fig)  # Uložení grafu do PDF

    # Vložení parametrů úlohy do PDF
    plt.figure(figsize=(6, 4))
    plt.text(0.1, 0.8, f"Střed: ({center[0]}, {center[1]})", fontsize=12)
    plt.text(0.1, 0.6, f"Poloměr: {radius} m", fontsize=12)
    plt.text(0.1, 0.4, f"Počet bodů: {num_points}", fontsize=12)
    plt.text(0.1, 0.2, f"Barva bodů: {point_color}", fontsize=12)
    plt.axis('off')  # Skrytí os
    pdf.savefig()  # Uložení parametrů do PDF

    pdf.close()
    return pdf_path

# Streamlit UI
st.title("Webová aplikace pro vykreslení kruhu s body")

# Parametry zadání
st.sidebar.header("Zadejte parametry kruhu")

center_x = st.sidebar.number_input("Střed X", value=0)
center_y = st.sidebar.number_input("Střed Y", value=0)
radius = st.sidebar.number_input("Poloměr (m)", min_value=1, value=5)
num_points = st.sidebar.slider("Počet bodů na kruhu", min_value=3, max_value=100, value=12)
point_color = st.sidebar.color_picker("Barva bodů", value="#FF0000")

# Vykreslení kruhu
center = (center_x, center_y)
fig = plot_circle(center, radius, num_points, point_color)
st.pyplot(fig)

# Možnost generování PDF
st.sidebar.header("Generování PDF")
if st.sidebar.button("Stáhnout PDF"):
    pdf_path = generate_pdf(center, radius, num_points, point_color)
    with open(pdf_path, "rb") as f:
        st.download_button("Stáhnout PDF", f, file_name="kruznice.pdf", mime="application/pdf")

# Informace o autorovi
st.sidebar.header("Informace o aplikaci")
st.sidebar.write("Tato aplikace byla vytvořena pro vizualizaci kruhu s parametry:")
st.sidebar.write("Použité technologie:")
st.sidebar.write("- Python")
st.sidebar.write("- Streamlit")
st.sidebar.write("- Matplotlib")
st.sidebar.write("- NumPy")

# Možnosti kontaktu
st.sidebar.write("Kontaktní informace:")
st.sidebar.write("Jméno: Tvé jméno")
st.sidebar.write("Email: tvuj@email.com")
