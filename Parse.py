import tkinter as tk
from tkinter import filedialog
import pdfplumber

def seleccionar_pdf():
    # Abre un diálogo para seleccionar un archivo PDF
    ruta_pdf = filedialog.askopenfilename(
        title="Selecciona un PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    
    if ruta_pdf:  # Si se seleccionó un archivo
        print(f"\n--- Extrayendo texto de: {ruta_pdf} ---\n")
        extraer_texto_pdf(ruta_pdf)
        root.destroy()  # Cierra la ventana después de extraer el texto

def extraer_texto_pdf(ruta_pdf):
    try:
        # Abre el archivo PDF
        with pdfplumber.open(ruta_pdf) as pdf:
            texto_completo = ""
            
            # Itera sobre cada página del PDF
            for pagina in pdf.pages:
                # Extrae el texto de la página actual
                texto_pagina = pagina.extract_text()
                if texto_pagina:  # Si hay texto en la página
                    texto_completo += texto_pagina + "\n\n"  # Agrega saltos de línea entre páginas
            
            # Muestra el texto en la terminal
            print(texto_completo)
    
    except Exception as e:
        print(f"\n¡Error al procesar el PDF!: {e}\n")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Extractor de Texto de PDF")
root.geometry("400x200")

# Botón para seleccionar PDF
boton_seleccionar = tk.Button(
    root,
    text="Seleccionar PDF",
    command=seleccionar_pdf,
    font=("Arial", 14),
    padx=20,
    pady=10,
    bg="#041F05",
    fg="white"
)
boton_seleccionar.pack(pady=50)

# Inicia la aplicación
root.mainloop()