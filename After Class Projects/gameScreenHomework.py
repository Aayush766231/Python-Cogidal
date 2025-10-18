import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
running = True
color = (255, 255, 255)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.polygon(screen, color, ((200, 100), (100, 200), (150, 300), (250, 300), (300, 200)), 1)
    pygame.display.flip()