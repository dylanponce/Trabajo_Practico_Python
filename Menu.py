import pygame
import sys
import os
from principal import main

# Define algunas constantes para los colores
BLANCO = (255, 255, 255)
GRIS = (128, 139, 150)
AZUL = (133, 193, 233)
ROJO = (255, 0, 0)
SALIR_ROJO= (183, 28, 28)
VERDE=(46, 204, 113)
JUGAR_VERDE= (34, 153, 84)

# Define una clase para los botones
#class se utiliza para definir una clase, que es una plantilla para crear objetos.
#Boton es una clase que define un botón para tu juego.
class Boton:
    def __init__(self, x, y, ancho, alto, texto=None, color=GRIS, color_destacado=AZUL, jugar_verde=VERDE ,salir_color=ROJO):
        self.x = x #self es una referencia al objeto actual. Se utiliza para acceder a las variables y métodos del objeto.
        self.y = y #self lo usamos como métodos de la clase Boton para referirse a la instancia actual del botón.
        self.ancho = ancho
        self.alto = alto
        self.texto = texto
        self.color = color
        self.color_destacado = color_destacado
        self.salir_color=salir_color
        self.jugar_verde=jugar_verde

    def dibujar(self, win, contorno=None):
        # método para dibujar el botón en la pantalla
        if contorno:
            pygame.draw.rect(win, contorno, (self.x-2, self.y-2, self.ancho+4, self.alto+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.ancho, self.alto), 0)

        if self.texto:
            fuente = pygame.font.SysFont('arial', 32)
            texto = fuente.render(self.texto, 1, BLANCO)
            win.blit(texto, (self.x + (self.ancho/2 - texto.get_width()/2), self.y + (self.alto/2 - texto.get_height()/2)))

    def esta_sobre(self, pos):
        # Pos es la posición del ratón o una tupla de coordenadas (x, y)
        if self.x < pos[0] < self.x + self.ancho:
            if self.y < pos[1] < self.y + self.alto:
                return True
        return False

def redibujar_ventana():
    # Dibuja la imagen de fondo
    #win es una superficie de Pygame en la que se dibuja el juego. Una variable que dibuja la pantalla
    win.blit(imagen_fondo, (0, 0))#blit es un método en Pygame que se utiliza para dibujar una imagen o una superficie sobre otra. Mi imagen de fondo

    boton_jugar.dibujar(win, BLANCO)
    boton_ranking.dibujar(win, BLANCO)
    boton_salir.dibujar(win, BLANCO)

pygame.init()
pygame.mixer.init()  # Inicializa el módulo mixer

# Cargar la música de fondo
pygame.mixer.music.load('Soundtrack_Menu.mp3')
pygame.mixer.music.play(-1) # Reproduce la música infinitamente
pygame.mixer.music.set_volume(0.2) # Establece el volumen al 50%

# Carga los sonidos
sonido1 = pygame.mixer.Sound('Seleccion Menu.mp3')
sonido2 = pygame.mixer.Sound('Seleccion Aceptar Menu.mp3')

sonido1.set_volume(0.15) #Para cambiar volumen
sonido2.set_volume(1)

def menu_juego():
    ejecutar = True
    while ejecutar:
        redibujar_ventana()
        pygame.display.update()

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if evento.type == pygame.QUIT:#type es una función incorporada en Python que devuelve el tipo de un objeto.
                ejecutar = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.esta_sobre(pos):
                    sonido2.play()  # Reproduce el sonido cuando se hace clic en el botón
                    print('botón jugar presionado')
                    main()
                if boton_ranking.esta_sobre(pos):
                    sonido2.play()  # Reproduce el sonido cuando se hace clic en el botón
                    pygame.mixer.music.pause()  # Pausa la música de fondo
                    os.system('Ranking.py') #ejecutar el script Ranking.py
                    print('botón ranking presionado')
                    pygame.mixer.music.unpause()  # Reanuda la música de fondo
                if boton_salir.esta_sobre(pos):
                    ejecutar = False
                    pygame.quit()
                    sys.exit() # terminar la ejecución del script.
            if evento.type == pygame.MOUSEMOTION:
                if boton_jugar.esta_sobre(pos):
                    boton_jugar.color = boton_jugar.jugar_verde
                    sonido1.play()  # Reproduce el sonido cuando el mouse está sobre el botón
                else:
                    boton_jugar.color = JUGAR_VERDE
                if boton_ranking.esta_sobre(pos):
                    boton_ranking.color = boton_ranking.color_destacado
                    sonido1.play()
                else:
                    boton_ranking.color = GRIS
                if boton_salir.esta_sobre(pos):
                    boton_salir.color = boton_salir.salir_color
                    sonido1.play()
                else:
                    boton_salir.color = SALIR_ROJO

pygame.init()
win = pygame.display.set_mode((800, 600))

# Ancho y alto de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

ANCHO_BOTON = 225
ALTO_BOTON = 35

# Calcula la posición x para centrar los botones
x = ANCHO_PANTALLA // 2 - ANCHO_BOTON // 2

# Carga la imagen de fondo
imagen_fondo = pygame.image.load('Menu_Picture.png')

# Crea los botones
boton_jugar = Boton(x-260, 290, ANCHO_BOTON, ALTO_BOTON, 'Jugar')
boton_ranking = Boton(x-260, 335, ANCHO_BOTON, ALTO_BOTON, 'Ranking')
boton_salir = Boton(x-260, 380, ANCHO_BOTON, ALTO_BOTON, 'Salir')

menu_juego()

