import random
import pygame
from pygame.locals import *
from configuracion import *

imagen_fondo = pygame.image.load('Fondo_Juego_Picture.png')# Carga la imagen de fondo

def dibujar(screen, productos_en_pantalla, producto_principal, producto_candidato, puntos, segundos):

    defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 30)

    screen.blit(imagen_fondo, (0, 0)) # Dibuja la imagen de fondo

    ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if (segundos < 15):
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    x_pos = 110
    y_pos = ALTO - (ALTO-230)

    product_rects = []  # Lista para guardar los rectángulos de los productos

    for producto in productos_en_pantalla:
        nombre_en_pantalla = "*"+producto[0]+producto[1]+"*"  # Para modificar el diseño de los presentado en imagen, anteriormente 0-5
        if producto[0] == producto_principal[0] and producto[1]== producto_principal[1]:
            text_surface = defaultFontGrande.render(nombre_en_pantalla,
                        1, COLOR_TIEMPO_FINAL)
            screen.blit(text_surface, (x_pos, y_pos))
        else:
            text_surface = defaultFontGrande.render(
                nombre_en_pantalla, 1, COLOR_LETRAS)
            screen.blit(text_surface, (x_pos, y_pos))

        # Crea un rectángulo para este producto y lo añade a la lista
        product_rects.append(pygame.Rect(x_pos, y_pos, text_surface.get_width(), text_surface.get_height()))

        y_pos += ESPACIO

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (600, 10))#Modifico la posicion de mis PUNTOS
    screen.blit(ren3, (10, 10))#Modifico la posicion de mi TIEMPO

    return product_rects  # Devuelve la lista de rectángulos


