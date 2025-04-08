import pygame

pygame.init()# Inicia Pygame
ventana = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
fuente = pygame.font.Font(None, 25) # Tipo de letra y tamaño
boton_atras = pygame.Rect(50, 50, 90, 25) # Rectángulo para el botón ATRAS (x,y,ancho,alto)
color_boton_atras = (128, 139, 150) # Color inicial del botón ATRAS
imagen_fondo = pygame.image.load('Ranking_Picture.png')# Carga la imagen de fondo

pygame.mixer.init() # Inicializa el mezclador de música
pygame.mixer.music.load('Soundtrack_Ranking.mp3') # Carga el sonido de ambiente
pygame.mixer.music.play(-1) # Reproduce el sonido de ambiente en bucle

sonido_boton = pygame.mixer.Sound('Seleccion Menu.mp3') # Carga el sonido del botón
sonido_click = pygame.mixer.Sound('Seleccion Aceptar Menu.mp3') # Carga el sonido del click

#Ajustes de Volumen
pygame.mixer.music.set_volume(0.2) # El volumen va de 0.0 a 1.0
sonido_boton.set_volume(0.1)
sonido_click.set_volume(0.5)

puntos = [] # Lee los datos del archivo
try:
    with open('puntos.txt', 'r') as archivo:
        for linea in archivo:
            puntos.append(int(linea.strip()))
except FileNotFoundError:
    # Si el archivo no existe, creamos una lista vacía
    puntos = [0 for _ in range(10)]

# Ordenamos la lista de puntos de mayor a menor
puntos.sort(reverse=True)#sort es un método en Python que se utiliza para ordenar los elementos de una lista en un orden específico (ascendente, por defecto)

ejecutando = True # Bucle principal
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hace clic en el botón ATRAS, volvemos a la pantalla principal
            if boton_atras.collidepoint(evento.pos):
                sonido_click.play() # Reproduce el sonido del click
                ejecutando = False
        elif evento.type == pygame.MOUSEMOTION:
            # Si el usuario pasa el mouse por encima del botón ATRAS, cambiamos su color a rojo
            if boton_atras.collidepoint(evento.pos):
                color_boton_atras = (133, 193, 233)
                sonido_boton.play() # Reproduce el sonido del botón
            else:
                color_boton_atras = (128, 139, 150)
    ventana.blit(imagen_fondo, (0, 0)) # Dibuja la imagen de fondo

    # Dibujamos el borde del botón ATRAS
    pygame.draw.rect(ventana, (255, 255, 255), boton_atras.inflate(5, 5))#Modifico el borde Blanco de ATRAS
    # Dibujamos el botón ATRAS
    pygame.draw.rect(ventana, color_boton_atras, boton_atras)
    texto_boton = fuente.render("ATRAS", True, (255, 255, 255))
    ventana.blit(texto_boton, (boton_atras.x + 15, boton_atras.y + 5))

    # Dibujamos las puntuaciones
    for i, puntuacion in enumerate(puntos[:10]):#enumerate es una función incorporada en Python que permite iterar sobre algo y tener un contador automático. Devuelve un objeto enumerado
        if i == 0:  # Primer lugar
            color = (218, 165, 32)  # Dorado
        elif i in [1, 2]:  # Segundo y tercer lugar
            color = (255, 0, 0)  # Rojo
        else:  # Otros lugares
            color = (0, 0, 0)  # Negro
        texto = fuente.render(f"{i+1}. {puntuacion}", True, color)
        ventana.blit(texto, (250, 145 + i*30))

    pygame.display.flip()# Actualizamos la pantalla. flip es un método en Pygame que se utiliza para actualizar la pantalla completa.

pygame.quit()# Salimos de Pygame




