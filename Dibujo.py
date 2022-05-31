import pygame
import sys
pygame.init()

# Definir colores
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

size = (600, 500)


# Crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(WHITE)
    # ----- ZONA DE DIBUJO

    pygame.draw.circle(screen, RED, (300, 200), 60)
    pygame.draw.rect(screen, GREEN, (100, 100, 80, 80))

    # ----- ZONA DE DIBUJO
    # Actualizar la pantalla
    pygame.display.flip()
