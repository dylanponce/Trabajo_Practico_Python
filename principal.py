#! /usr/bin/env python
import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesORIGINAL import * #Cambiar a funcionesORIGINAL (Estan no repetidas)
from extras import *


def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()  # Inicializa el mixer de pygame

    # Carga y reproduce la música
    pygame.mixer.music.load('Soundtrack_Play.mp3')
    pygame.mixer.music.play(-1)  # El -1 hará que la canción se repita indefinidamente
    pygame.mixer.music.set_volume(0.06)  # 50% del volumen Es para ajustar el volumen
    acierto_sound = pygame.mixer.Sound('Correcto.mp3')
    acierto_sound.set_volume(0.04) #Ajustar Volumen
    error_sound = pygame.mixer.Sound('Incorrecto.mp3')
    error_sound.set_volume(0.03) #Ajustar Volumen

    # Preparar la ventana
    pygame.display.set_caption("Prcio Justo")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
    print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    product_rects = dibujar(screen, productos_en_pantalla, producto,
            producto_candidato, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            if e.type == QUIT:
                pygame.quit()
                return ()
            elif e.type == MOUSEBUTTONDOWN:
                # Obtén la posición del mouse
                pos = pygame.mouse.get_pos()

                for i, rect in enumerate(product_rects[1:], start=1):#Con el 1, solo toma los valores para Clickear desde 1 a 5
                    if rect.collidepoint(pos):
                        # El mouse fue presionado sobre el producto i
                        # Aquí puedes manejar la lógica de tu juego cuando se selecciona un producto
                        puntos += procesar(producto, productos_en_pantalla[i], MARGEN,acierto_sound,error_sound)
                        producto_candidato = ""
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                        break
        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
        screen.fill(COLOR_FONDO)
        product_rects = dibujar(screen, productos_en_pantalla, producto,
                producto_candidato, puntos, segundos)
        pygame.display.flip()
    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
        if segundos <= 0:
            print(f"Tu puntuación final es: {puntos}")
            with open('puntos.txt', 'a') as archivo:
                archivo.write(f"{puntos}\n")
            pygame.quit()
            sys.exit()
if __name__ == "__main__":
    main()

