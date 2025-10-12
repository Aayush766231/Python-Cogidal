import pygame

pygame.init()
#Variable Setup
window = pygame.display.set_mode((400, 600))
GREEN = (0, 255, 0)
#White Background
window.fill((255, 255, 255))
#Two Balls
pygame.draw.circle(window, GREEN, (200, 300), 50)
pygame.draw.circle(window, GREEN, (300, 400), 50, 3)
#Triangle
pygame.draw.polygon(window, GREEN, ((10, 20), (35, 50), (60, 20)), 5)
#Line
pygame.draw.line(window, GREEN, (50, 500), (100, 50), 4)
#update screen (if parameter, then updates only one thing)
pygame.display.update()
#running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()