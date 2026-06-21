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



# =============================================================
# FUNCION 2: analizar_directorio  (RECURSIVA)
# =============================================================



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



# =============================================================
# FUNCION 7: pedir_carpeta
# =============================================================



# =============================================================
# FUNCION 8: construir_reportes
# =============================================================



# =============================================================
# FUNCION 9: main  (FUNCION PRINCIPAL)
# =============================================================





# =============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================
if __name__ == "__main__":
    main()
