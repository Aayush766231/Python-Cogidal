import pygame
import random

pygame.init()
movementSpeed = 5

screenWidth, screenHeight = 500, 400
bgImage = pygame.transform.scale(pygame.image.load('bg.png'), (screenWidth, screenHeight))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('green'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screenWidth - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screenHeight - self.rect.height), 0)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sprite Homework + Movement")
allSprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = 125, 325
allSprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = 375, 325
allSprites.add(sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movementSpeed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movementSpeed
    sprite1.move(x_change, y_change)
    x_new = (keys[pygame.K_d] - keys[pygame.K_a]) * movementSpeed
    y_new = (keys[pygame.K_s] - keys[pygame.K_w]) * movementSpeed
    sprite2.move(x_new, y_new)

    screen.blit(bgImage, (0, 0))
    allSprites.draw(screen)

    pygame.display.flip()
    clock.tick(90)
pygame.quit()