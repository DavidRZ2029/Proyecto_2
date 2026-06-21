"""
Graficador de Espacio en Disco
IC-1801 Taller de Programacion
Proyecto 2
Antonio Ye Lu 2025125809
David rodriguez Zuñiga 2026079873
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

Profundidad = 6   # Maximo nivel de carpetas a analizar
COLORES = [           # Lista de colores para el grafico de barras
    "FF0000", "#00FF00", "#0000FF", "#0000000",
    "#FFFFFF", "#", "#b07aa1", "#ff9da7",
    "#9c755f", "#bab0ac"
]
def convertir_tamano(bytes_totales):
  
    if bytes_totales < 1024:
        return f"{bytes_totales} B"
    
    kb = bytes_totales / 1024
    if kb < 1024:
        return f"{kb:.2f} KB"
   
    mb = kb / 1024
    if mb < 1024:
        return f"{mb:.2f} MB"
 
    gb = mb / 1024
    if gb < 1024:
        return f"{gb:.2f} GB"
   
    tb = gb / 1024
    return f"{tb:.2f} TB"
