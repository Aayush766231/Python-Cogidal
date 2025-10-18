import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True
color = (0, 0, 0)

text = pygame.font.Font(None, 36).render("My first game screen", True, pygame.Color("black"))
textRect = text.get_rect(center=(500 // 2, 500 // 2 + 110))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 128, 128)) 
    pygame.draw.polygon(screen, color, ((250, 100), (125, 200), (187.5, 300), (312.5, 300), (375, 200)))
    screen.blit(text, textRect)
    pygame.display.flip()  