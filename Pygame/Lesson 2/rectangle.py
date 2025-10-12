import pygame
#Initialize
pygame.init()
#set display up
screen = pygame.display.set_mode((400, 300))
done = False
#loop for screen 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #draw the rectangle
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    #update the screen
    pygame.display.flip()