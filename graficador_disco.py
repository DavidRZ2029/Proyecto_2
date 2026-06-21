import os
import pygame


anchodelaventana = 1200          
altodelaventana = 750           
profundidadpermitidadanalizar = 6     

BLANCO = (255, 255, 255)
NEGRO = (20, 20, 20)
GRIS = (240, 240, 240)
GRIS_OSCURO = (44, 62, 80)
VERDE = (39, 174, 96)
GRIS_TEXTO = (90, 90, 90)

PALETA = [
    (78, 121, 167), (242, 142, 43), (225, 87, 89), (118, 183, 178), (89, 161, 79), (237, 201, 72),
    (176, 122, 161), (255, 157, 167), (156, 117, 95), (186, 176, 172), (109, 204, 218), (255, 110, 110),
]


# =============================================================
# FUNCION 1: convertir_tamano
# =============================================================
def convertir_tamano(bytes_totales):
    """
    Descripcion: Convierte un tamano en bytes a la unidad mas legible (B, KB, MB, GB o TB).
    Entradas:  bytes_totales (int) -> tamano en bytes.
    Salidas:   (str) -> texto con el tamano y su unidad. Ej: "3.50 MB".
    Restricciones: bytes_totales debe ser un entero mayor o igual a 0.
    """
    if bytes_totales < 1024:
        return str(bytes_totales) + " B"

    valor = bytes_totales / 1024
    for unidad in ["KB", "MB", "GB"]:
        if valor < 1024:
            return f"{valor:.2f} {unidad}"
        valor = valor / 1024

    return f"{valor:.2f} TB"


# =============================================================
# FUNCION 2: analizar_directorio  (RECURSIVA)
# =============================================================
def analizar_directorio(ruta, profundidad, archivos_grandes, dirs_con_archivos):
    """
        Descripcion: Recorre una carpeta y todas sus subcarpetas usando recursion. Suma el tamano de los archivos y baja a las subcarpetas hasta MAX_PROFUNDIDAD niveles. Tambien guarda informacion para los reportes top-10.
        Entradas:
        ruta              (str)  -> ruta absoluta de la carpeta a analizar.
        profundidad       (int)  -> nivel actual de recursion (inicia en 0).
        archivos_grandes  (list) -> lista compartida donde se acumulan
                                    tuplas (ruta_archivo, tamano).
        dirs_con_archivos (list) -> lista compartida donde se acumulan
                                    tuplas (ruta_dir, cantidad_archivos).
        Salidas: (int) -> tamano total en bytes de la carpeta y sus subcarpetas.
        Restricciones: profundidad no debe superar MAX_PROFUNDIDAD.
    """
    tamano_total = 0
    cantidad_archivos = 0

    try:
        elementos = os.listdir(ruta)
    except (PermissionError, OSError):
        return 0

    for nombre in elementos:
        ruta_elemento = os.path.join(ruta, nombre)

        if os.path.isfile(ruta_elemento):
            try:
                tam = os.path.getsize(ruta_elemento)
                tamano_total += tam
                cantidad_archivos += 1
                archivos_grandes.append((ruta_elemento, tam))
            except OSError:
                pass
            
        elif os.path.isdir(ruta_elemento) and profundidad < MAX_PROFUNDIDAD:
            tam_sub = analizar_directorio(
                ruta_elemento,
                profundidad + 1,
                archivos_grandes,
                dirs_con_archivos
            )
            tamano_total += tam_sub

    dirs_con_archivos.append((ruta, cantidad_archivos))

    return tamano_total


# =============================================================
# FUNCION 3: obtener_subdirectorios
# =============================================================



# =============================================================
# FUNCION 4: dibujar_texto
# =============================================================
def dibujar_texto(pantalla, fuente, texto, x, y, color=NEGRO, alinear_derecha=False):
    """
    Descripcion: Dibuja una linea de texto en la pantalla.
    Entradas:
        pantalla                  -> superficie de Pygame donde dibujar.
        fuente                    -> fuente de Pygame a usar.
        texto           (str)     -> texto a mostrar.
        x, y            (int)     -> posicion donde colocar el texto.
        color           (tuple)   -> color RGB del texto.
        alinear_derecha (bool)    -> si True, el texto termina en x.
    Salidas: Ninguna (dibuja directamente en pantalla).
    Restricciones: la fuente debe estar inicializada.
    """
    imagen = fuente.render(texto, True, color)
    rect = imagen.get_rect()
    if alinear_derecha:
        rect.topright = (x, y)
    else:
        rect.topleft = (x, y)
    pantalla.blit(imagen, rect)


# =============================================================
# FUNCION 5: dibujar_barras
# =============================================================



# =============================================================
# FUNCION 6: dibujar_lista
# =============================================================
def dibujar_lista(pantalla, fuente, fuente_titulo, titulo, lineas, x, y, ancho):
    """
    Descripcion: Dibuja un panel con un titulo y una lista de lineas de texto (se usa para los dos reportes top-10).
    Entradas:
        pantalla                -> donde se dibuja.
        fuente                  -> fuente para las lineas.
        fuente_titulo           -> fuente para el titulo.
        titulo        (str)     -> titulo del panel.
        lineas        (list)    -> lista de strings a mostrar.
        x, y          (int)     -> esquina superior izquierda del panel.
        ancho         (int)     -> ancho del panel.
    Salidas: Ninguna (dibuja directamente en pantalla).
    Restricciones: ninguna.
    """
    dibujar_texto(pantalla, fuente_titulo, titulo, x, y, GRIS_OSCURO)
    pygame.draw.line(pantalla, GRIS_OSCURO, (x, y + 24), (x + ancho, y + 24), 1)

    linea_y = y + 32
    for texto in lineas:
        maximo_caracteres = ancho // 7
        if len(texto) > maximo_caracteres:
            texto = "..." + texto[-(maximo_caracteres - 3):]
        dibujar_texto(pantalla, fuente, texto, x, linea_y, NEGRO)
        linea_y += 18


# =============================================================
# FUNCION 7: pedir_carpeta
# =============================================================
def pedir_carpeta():
    """
    Descripcion: Abre una ventana del sistema para que el usuario elija una carpeta. Si tkinter no esta disponible, pide la ruta por la consola.
    Entradas: Ninguna.
    Salidas: (str) -> ruta de la carpeta elegida, o cadena vacia si se cancela.
    Restricciones: ninguna.
    """
    try:
        import tkinter
        from tkinter import filedialog
        raiz = tkinter.Tk()
        raiz.withdraw()
        ruta = filedialog.askdirectory(title="Seleccione una carpeta para analizar")
        raiz.destroy()
        return ruta
    except Exception:
        try:
            return input("Escriba la ruta de la carpeta a analizar: ").strip()
        except Exception:
            return ""


# =============================================================
# FUNCION 8: construir_reportes
# =============================================================
def construir_reportes(archivos_grandes, dirs_con_archivos):
    """
    Descripcion: A partir de las listas recolectadas durante el analisis, construye las lineas de texto para los dos reportes: top 10 archivos mas grandes y top 10 directorios con mas archivos directos.
    Entradas:
        archivos_grandes  (list) -> tuplas (ruta_archivo, tamano).
        dirs_con_archivos (list) -> tuplas (ruta_dir, cantidad).
    Salidas: (tuple) -> (lineas_archivos, lineas_dirs), dos listas de strings.
    Restricciones: ninguna.
    """
    top_archivos = sorted(archivos_grandes, key=lambda x: x[1], reverse=True)[:10]
    lineas_archivos = []
    for i, (ruta_arch, tam) in enumerate(top_archivos, 1):
        nombre = os.path.basename(ruta_arch)
        lineas_archivos.append(f"{i:2}. {nombre}  [{convertir_tamano(tam)}]")
        lineas_archivos.append(f"     {ruta_arch}")

    top_dirs = sorted(dirs_con_archivos, key=lambda x: x[1], reverse=True)[:10]
    lineas_dirs = []
    for i, (ruta_dir, cantidad) in enumerate(top_dirs, 1):
        nombre = os.path.basename(ruta_dir)
        lineas_dirs.append(f"{i:2}. {nombre}  [{cantidad} archivos]")
        lineas_dirs.append(f"     {ruta_dir}")

    return lineas_archivos, lineas_dirs


# =============================================================
# FUNCION 9: main  (FUNCION PRINCIPAL)
# =============================================================
def main():
    """
    Descripcion: Funcion principal. Inicializa Pygame, pide la carpeta, ejecuta el analisis y dibuja en bucle el grafico y los reportes hasta que el usuario cierra la ventana.
    Entradas: Ninguna.
    Salidas: Ninguna.
    Restricciones: requiere que Pygame este instalado.
    """
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Graficador de Espacio en Disco")
    reloj = pygame.time.Clock()

    fuente = pygame.font.SysFont("consolas", 14)
    fuente_titulo = pygame.font.SysFont("arial", 16, bold=True)
    fuente_boton = pygame.font.SysFont("arial", 16, bold=True)

    ruta_actual = ""
    datos = []
    lineas_archivos = []
    lineas_dirs = []
    mensaje = "Presione el boton para seleccionar una carpeta."

    boton_rect = pygame.Rect(20, 15, 220, 36)

    # =====================================================
    # FUNCION INTERNA: ejecutar_analisis
    # =====================================================
    pass



# =============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================
if __name__ == "__main__":
    main()
