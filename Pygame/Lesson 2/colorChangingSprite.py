import pygame

def main():
    pygame.init()
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Color Changing Sprite")

    colors = {
        'red': pygame.Color('red'),
        'blue': pygame.Color('blue'),
        'green': pygame.Color('green'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    currentColor = colors['white']

    x, y = 30, 30
    spriteWidth, spriteHeight = 60, 60

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 10
        elif pressed[pygame.K_RIGHT]:
            x += 10
        elif pressed[pygame.K_UP]:
            y -= 10
        elif pressed[pygame.K_DOWN]:
            y += 10
        
        x = min(max(0, x), width - spriteWidth)
        y = min(max(0, y), height - spriteHeight)

        if x == 0:
            currentColor = colors['blue']
        elif x == (width - spriteWidth):
            currentColor = colors['red']
        elif y == 0:
            currentColor = colors['green']
        elif y == (height - spriteHeight):
            currentColor = colors['yellow']
        else:
            currentColor = colors['white']
        
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, currentColor, (x, y, spriteWidth, spriteHeight))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__ == "__main__":
    main()