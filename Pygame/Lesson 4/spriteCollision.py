import pygame
import random

screenWidth, screenHeight = 500, 400
movementSpeed = 5
fontSize = 72

pygame.init()

bgImage = pygame.transform.scale(pygame.image.load('bg.png'), (screenWidth, screenHeight))
font = pygame.font.SysFont("Times New Roman", fontSize)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screenWidth - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screenHeight - self.rect.height), 0)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sprite Collision")
allSprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screenWidth - sprite1.rect.width), random.randint(0, screenHeight - sprite1.rect.height)
allSprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = 375, 325
allSprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movementSpeed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movementSpeed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            allSprites.remove(sprite2)
            won = True
    screen.blit(bgImage, (0, 0))
    allSprites.draw(screen)
    if won:
        winText = font.render("You Win!", True, pygame.Color('black'))
        screen.blit(winText, ((screenWidth - winText.get_width()) // 2, (screenHeight - winText.get_height()) // 2))
    pygame.display.flip()
    clock.tick(90)

pygame.quit()